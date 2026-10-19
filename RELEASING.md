# 生成版本文件

本文件供维护者使用。打包命令仅生成本地文件，不创建 GitHub 仓库、不上传 Overleaf，也不发布 Release。

## 本地生成

先检查并编译当前内容，再打包：

```sh
python3 scripts/build.py
python3 scripts/package.py --pdf build/main/main.pdf
```

`dist/` 中将生成三个文件：

| 文件 | 用途 |
| --- | --- |
| `scholarship-beamer-overleaf.zip` | 一个完整源码包，可导入 Overleaf；含完整字体、素材、文档与预览 |
| `scholarship-beamer.pdf` | 独立的完整示例 PDF，不塞进源码 ZIP |
| `SHA256SUMS.txt` | ZIP 与 PDF 的 SHA-256 校验值 |

不传 `--pdf` 时只生成源码 ZIP 与对应校验值。脚本不会自动编译，也不会判断所传 PDF 是否来自当前源码；维护者应使用上面连续的构建与打包命令。脚本排除构建目录、版本控制目录、缓存及 TeX 临时文件，保留字体许可、素材记录和校徽 PDF。默认要求 ZIP 小于 50,000,000 字节；这个本地体积门槛不代表 Overleaf 在线编译已经通过。

## 发布前检查

1. 核对 README 的用途、文件名、预览与当前 PDF 一致；逐页检查没有遗漏的真实个人信息或未经说明的素材。
2. 将 ZIP 解压到干净目录，从该目录执行 `python3 scripts/build.py`，检查完整 PDF、缺字、图片和目录跳转。
3. 若更改了编译入口、TeX、字体或图片，从 README 的 Overleaf 按钮导入并检查编译。当前完整示例已知在免费账号超时，README 必须保留简短的使用限制与本地方案；详细日志留在内部报告。仅文档改动可以沿用相同有效源码的云端结果，不重复导入。不能把导入成功当作在线编译成功，也不能把增加付费时限当作已测试付费账号。
4. 核对代码 MIT、字体 OFL、建筑与示例图片的单独声明，以及学校标识的独立权利说明；替换素材时同步来源记录。
5. 按项目所有者对当前版本的授权进行 GitHub 推送和公开，不重复索取已有授权。每个版本上传上述三个文件；下载链接应指向实际存在的版本附件。保留旧版本，不覆盖其附件来伪装为新构建。

## Overleaf 按钮

README 使用以下版本附件地址：

- 源码：`https://github.com/eprogressing/scholarship-beamer/releases/latest/download/scholarship-beamer-overleaf.zip`
- PDF：`https://github.com/eprogressing/scholarship-beamer/releases/latest/download/scholarship-beamer.pdf`
- Overleaf：将源码附件地址 URL 编码后放入 `https://www.overleaf.com/docs` 的 `snip_uri` 参数，同时指定 `engine=xelatex` 与 `main_document=main.tex`。

这是 [Overleaf 官方提供的 ZIP 导入接口](https://www.overleaf.com/devs)，不要求先创建一个共享 Overleaf 模板。ZIP 必须能由 Overleaf 服务器通过公开 HTTP/HTTPS 地址读取；私有仓库的登录态或本机文件路径不能替代公开附件。不要将 GitHub 的附件预览页当成 ZIP 直链。

公开版本时，检查以上 ZIP、PDF 两个地址无需登录即可下载、内容正确，再检查按钮的导入结果。若仓库名称、附件文件名有变，同时更新下载链接和 Overleaf 的 `snip_uri`。不应在仍无公开附件时把按钮描述为已经可用；私有准备阶段应隐藏导入按钮，避免误点。

若后续修改源码，重新构建、打包并更新预览。本文所列发布检查不构成自动公开或上传的授权。
