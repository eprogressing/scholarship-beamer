#!/usr/bin/env python3
"""Create a local source ZIP and checksums; optionally copy a compiled PDF."""
from __future__ import annotations

import argparse
import hashlib
import os
from pathlib import Path
import shutil
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "build", "dist", "__pycache__"}
SKIP_NAMES = {".DS_Store", "build-console.log", "build-report.json"}
TEMP_SUFFIXES = (
    ".aux", ".log", ".nav", ".out", ".snm", ".toc", ".vrb", ".xdv",
    ".fls", ".fdb_latexmk", ".synctex.gz", ".pyc",
)


def source_files(output: Path) -> list[Path]:
    files = []
    for current, dirs, names in os.walk(ROOT):
        folder = Path(current)
        for name in dirs + names:
            candidate = folder / name
            if candidate.is_symlink():
                raise ValueError(f"Refusing symbolic link: {candidate.relative_to(ROOT)}")
        dirs[:] = sorted(name for name in dirs
                         if name not in SKIP_DIRS and folder / name != output)
        for name in sorted(names):
            path = folder / name
            if name in SKIP_NAMES or name.endswith(TEMP_SUFFIXES):
                continue
            if folder == ROOT and name in {"main.pdf", "nku.pdf"}:
                continue
            files.append(path)
    return sorted(files)


def sha256(path: Path) -> str:
    with path.open("rb") as stream:
        digest = hashlib.sha256()
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", type=Path, help="Existing PDF from the current build")
    parser.add_argument("--outdir", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    output = args.outdir.resolve()
    if ROOT.is_relative_to(output):
        parser.error("Output must not be the source root or an ancestor of it.")
    pdf = args.pdf.resolve() if args.pdf else None
    if pdf:
        if not pdf.is_file():
            parser.error(f"PDF does not exist: {pdf}")
        with pdf.open("rb") as stream:
            if stream.read(5) != b"%PDF-":
                parser.error("--pdf must point to an existing PDF file.")
    try:
        files = source_files(output)
    except ValueError as exc:
        parser.error(str(exc))
    if not (ROOT / "main.tex").is_file():
        parser.error("Missing main.tex")
    output.mkdir(parents=True, exist_ok=True)
    archive = output / "scholarship-beamer-overleaf.zip"
    # Fixed timestamps and sorted entries make identical inputs reproducible.
    with tempfile.TemporaryDirectory(prefix="scholarship-beamer-") as temporary:
        draft = Path(temporary) / archive.name
        with zipfile.ZipFile(draft, "w", compression=zipfile.ZIP_DEFLATED,
                             compresslevel=9) as bundle:
            for path in files:
                info = zipfile.ZipInfo(path.relative_to(ROOT).as_posix(),
                                       date_time=(1980, 1, 1, 0, 0, 0))
                info.create_system = 3
                info.external_attr = 0o100644 << 16
                info.compress_type = zipfile.ZIP_DEFLATED
                bundle.writestr(info, path.read_bytes(), compresslevel=9)
        if draft.stat().st_size >= 50_000_000:
            parser.error("ZIP exceeds the local 50 MB budget; reduce image sizes before release.")
        shutil.copyfile(draft, archive)
    artifacts = [archive]
    if pdf:
        target = output / "scholarship-beamer.pdf"
        if pdf != target:
            shutil.copyfile(pdf, target)
        artifacts.append(target)
    sums = output / "SHA256SUMS.txt"
    sums.write_text("".join(f"{sha256(path)}  {path.name}\n" for path in artifacts),
                    encoding="utf-8")
    print(f"Packaged {len(files)} files ({archive.stat().st_size:,} bytes)")
    for path in artifacts + [sums]:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
