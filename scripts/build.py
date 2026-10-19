#!/usr/bin/env python3
"""Compile a preset or diagnostic; fail on overflow, missing glyphs or bad fonts."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {"main": "main.tex", **{n: f"demos/{n}.tex" for n in ("nku",)},
           }
SCHOOLS = ("nku",)

def build(entry: str, output: Path) -> bool:
    out = output / entry
    out.mkdir(parents=True, exist_ok=True)
    command = ["latexmk", "-xelatex", "-interaction=nonstopmode", "-halt-on-error",
               f"-jobname={entry}", f"-outdir={out}", SOURCES[entry]]
    result = subprocess.run(command, cwd=ROOT, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, text=True)
    (out / "build-console.log").write_text(result.stdout, encoding="utf-8")
    log = out / f"{entry}.log"
    text = log.read_text(encoding="utf-8", errors="replace") if log.exists() else ""
    failures = re.findall(
        r"^(?:Overfull \\[hv]box|Missing character:|! |LaTeX Font Warning:|"
        r".*Package (?:Nankai|Campus|xeCJK|hyperref) Warning:).*$", text, re.M)
    pdf = out / f"{entry}.pdf"
    hashes = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in sorted(ROOT.rglob("*"))
              if p.suffix in (".tex", ".sty") and "build" not in p.relative_to(ROOT).parts
              and not p.is_relative_to(output)}
    report = {"entry": entry, "finished_utc": datetime.now(timezone.utc).isoformat(),
              "command": command, "process_exit": result.returncode,
              "layout_failures": failures, "pdf_exists": pdf.is_file(),
              "pdf_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest() if pdf.is_file() else None,
              "source_sha256": hashes}
    (out / "build-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    passed = result.returncode == 0 and not failures and pdf.is_file()
    if passed:
        print(f"PASS {entry}: {pdf}", flush=True)
    else:
        print(f"FAIL {entry}\n{result.stdout[-2200:]}", flush=True)
        for failure in failures:
            print("LAYOUT:", failure, flush=True)
    return passed

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("entry", nargs="?", choices=SOURCES, default="main")
    parser.add_argument("--all", action="store_true", help="Build all included school demos (nku).")
    parser.add_argument("--outdir", type=Path, default=ROOT / "build")
    args = parser.parse_args()
    if not all(shutil.which(name) for name in ("latexmk", "xelatex")):
        parser.error("Install XeLaTeX and latexmk, or use Overleaf with XeLaTeX.")
    entries = SCHOOLS if args.all else (args.entry,)
    results = [build(entry, args.outdir.resolve()) for entry in entries]
    return 0 if all(results) else 1

if __name__ == "__main__":
    raise SystemExit(main())
