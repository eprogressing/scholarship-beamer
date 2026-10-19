# Scholarship Beamer

一套用于奖学金评审、评优答辩与个人展示的中文 LaTeX Beamer 模板，也可以按面试要求，改成保研、夏令营的自我介绍。

[Prism 在线编辑](https://prism.openai.com/) · [下载源码](https://github.com/eprogressing/scholarship-beamer/releases/latest/download/scholarship-beamer-overleaf.zip) · [查看完整 PDF](https://github.com/eprogressing/scholarship-beamer/releases/latest/download/scholarship-beamer.pdf) · [换校教程](CUSTOMIZE.md) · [逐页填写指南](CONTENT_GUIDE.md)

**源码免费，推荐用 Prism 在线修改。** 当前完整 15 页示例已在 Prism、TeXPage 免费账号和本地 XeLaTeX 中编译通过。第一次使用可以按下面的 Prism 步骤操作，不需要安装软件；免费 Overleaf 账号实测会超时。

## 效果预览

16:9 画幅，霞鹜文楷正文，共 15 页，不含附录。封面采用校园建筑与渐变配色，正文包括个人介绍、科研图文、竞赛表格、证书墙、活动照片墙与总结。

![南开、中国农大、人大、厦大四校封面对照](preview/schools.jpg)

**源码默认附南开版。** 中国农大、人大和厦大展示的是换校效果，这三个学校的源码和单独素材没有包含在下载包中。学校名称、颜色、校徽和建筑可以在 [settings.tex](settings.tex) 中替换，方法见 [换校教程](CUSTOMIZE.md)。这是个人制作的非官方模板。

![个人介绍、科研、竞赛、学生工作、实践服务、总结与结尾](preview/pages.jpg)

## Beamer 是什么？

[Beamer](https://ctan.org/pkg/beamer) 是用 LaTeX 制作幻灯片的文档类。在 `.tex` 文件中修改文字、图片路径和数据，编译后得到 PDF；页眉、字体和配色由主题统一管理。这份模板的文字、表格和排版都可以在源码中修改，建筑与照片是独立图片素材。

**它不是在 PowerPoint 里直接改字的 `.pptx` 模板。** 如果你希望用鼠标拖动每个元素，需要另行制作原生 PPT；如果愿意通过改文字和数据生成演示文稿，也可以让 AI Agent 帮忙修改这套源码。

## 先编译出第一份 PDF

### Prism：免费在线编译，推荐

[Prism](https://prism.openai.com/) 是 OpenAI 提供的[免费 LaTeX 工作区](https://openai.com/prism/)，可以编辑源码、预览 PDF，也可以让内置 AI 帮忙修改。

1. 下载上方的**源码 ZIP**，打开 Prism，用个人 ChatGPT 账号登录。
2. 点击 **「导入 → 导入归档文件（.zip、.tar.gz）」**，选择 `scholarship-beamer-overleaf.zip`，等待项目创建完成。
3. 打开 **`main.tex`**，点击右侧 **「编译」**。文件第一行已指定 XeLaTeX，请保留这一行；不需要转换模板或重新制作页面。
4. 右侧出现 PDF 后，点击 **「下载 PDF」**。改姓名、学院和标题用 `settings.tex`，改正文用 `examples/`，每次修改后重新编译。

2026 年 10 月 19 日，上传完整发布版 ZIP，成功生成并下载 **15 页 PDF**，字体、图片和文字已核对。本次首次加载曾提示“编译成功，无法加载 PDF”，点击 **「重新编译」** 后恢复正常。若你的账号暂时无法访问 Prism，可以选下方的 TeXPage 或本地编译。

上方 Prism 链接进入工作区，需要自行导入 ZIP；不会自动复制模板到你的账号。

### TeXPage：另一种已实测的免费在线方式

1. 下载上方的**源码 ZIP**，不必解压；打开 [TeXPage](https://www.texpage.com/console) 并登录。
2. 在项目主页点击 **「新建 → 上传项目」**，上传 `scholarship-beamer-overleaf.zip`。要上传完整 ZIP，字体和图片都在里面。
3. 打开导入的项目，在右上角 **「设置 → 编译设置」** 确认：编译器为 **XeLaTeX**、TeX Live 为 **2026**、主文件为 **`main.tex`**，编译模式为**常规**。本次导入已自动选对这些设置，仍建议检查一遍。
4. 点击 **「编译」**，右侧显示 PDF 后，点击 PDF 工具栏的下载图标，再选 **「下载 PDF」**。后续修改 `settings.tex` 或 `examples/` 中的内容，再次编译即可。

2026 年 10 月 19 日，使用免费账号上传发布版完整 ZIP，成功生成并下载 **15 页 PDF**，字体、图片和文字已核对。TeXPage 当前免费编译时限为 [30 秒](https://www.texpage.com/zh/pricing)；如果添加内容后超时，可以改用下方的本地编译。

TeXPage 链接进入项目主页，需要按上述步骤上传 ZIP，不会自动复制模板到你的账号。

### 本地编译：免费

1. 下载并解压上方的源码 ZIP，进入能看到 `main.tex` 的文件夹。
2. 安装包含 **XeLaTeX 和 latexmk** 的 LaTeX 环境：Windows / Linux 可用 [TeX Live](https://tug.org/texlive/)，macOS 可用 [MacTeX](https://tug.org/mactex/)。已有环境的同学可以直接编译。字体随项目提供，不必另外安装到系统。
3. 在这个文件夹打开终端，运行：

```sh
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

生成的文件是 **`main.pdf`**。后续每次改完内容，重新运行同一条命令即可。项目在 TeX Live 2026 下测试；其他版本请以实际编译结果为准。

如果提示 `latexmk` 或 `xelatex` 找不到，先确认 LaTeX 环境安装完整，关闭终端后重新打开；这不是缺少项目里的字体。

### Overleaf：可以导入，注意编译时限

[![在 Overleaf 中打开](preview/open-in-overleaf.svg)](https://www.overleaf.com/docs?snip_uri=https%3A%2F%2Fgithub.com%2Feprogressing%2Fscholarship-beamer%2Freleases%2Flatest%2Fdownload%2Fscholarship-beamer-overleaf.zip&engine=xelatex&main_document=main.tex)

点击按钮可把完整源码导入自己的 Overleaf 项目。链接已指定 **XeLaTeX** 和主文件 **`main.tex`**；手动上传 ZIP 时，请在项目设置中选择这两项。

当前 15 页示例在免费账号中实测超时，正文换成占位图也没有解决。Overleaf 的免费编译时限为 **10 秒**，付费方案为 **240 秒**，见 [官方方案限制](https://docs.overleaf.com/getting-started/free-and-premium-plans/plan-limits)。**免费在线使用可先选上方已实测的 Prism 或 TeXPage，也可以本地编译。** 如果希望继续使用 Overleaf，可检查学校是否提供授权，或考虑更长编译时间的付费方案；本项目尚未在付费账号下测试。

Overleaf 会员费用与模板无关。本项目不销售会员；如通过淘宝、闲鱼等第三方渠道购买在线编译服务，请自行核实服务内容、期限与账号使用方式，作者不为第三方卖家作保证。

## 改成自己的内容

开始改稿时，先处理这三处：

1. **封面信息**：在 [settings.tex](settings.tex) 填写题目、姓名、学院、专业和日期。
2. **正文材料**：在 `examples/` 替换经历、成绩和照片；目录与章节顺序在 [examples/content.tex](examples/content.tex) 中调整。
3. **学校样式**：按 `settings.tex` 中的中文注释，修改学校、配色，并替换彩色与白色校徽、建筑插图。

<details>
<summary>各页面对应哪个文件？</summary>

| 内容 | 文件 |
| --- | --- |
| 个人介绍、绩点、排名、代表课程 | [examples/profile.tex](examples/profile.tex) |
| 科研项目 | [examples/research.tex](examples/research.tex) |
| 竞赛荣誉与证书 | [examples/competition.tex](examples/competition.tex) |
| 学生工作 | [examples/studentwork.tex](examples/studentwork.tex) |
| 社会实践、志愿服务 | [examples/practice-service.tex](examples/practice-service.tex) |
| 阶段总结与未来计划 | [examples/activities.tex](examples/activities.tex) |

</details>

默认大纲为「个人概况 → 科研竞赛 → 学生工作 → 实践服务 → 总结展望」，不必全部保留。用于保研或夏令营时，建议突出专业背景、研究经历、本人贡献与研究兴趣，再按要求删减其他章节。示例人物、AI 场景、虚构经历和演示成绩都请替换为本人的真实材料；科研样图也不代表使用者的研究成果。

<details>
<summary>想检查缺字、溢出与字体警告？</summary>

安装 Python 3.9 或以上版本后，在项目目录运行：

```sh
python3 scripts/build.py
```

Windows 上也可根据本机 Python 命令使用 `python` 或 `py -3`。生成的 PDF 在 `build/main/main.pdf`；这项检查仍需要已安装 XeLaTeX 和 latexmk。脚本通过以后，也请实际打开 PDF 检查每一页。

</details>

## 不熟悉 LaTeX，怎么让 Agent 帮忙？

Agent 可以理解为能在项目中读文件、修改代码并运行命令的 AI 助手。优先用你已经熟悉、**能打开整个文件夹并调用本地终端**的工具，例如 [Codex](https://learn.chatgpt.com/docs/codex/cli) 或 [Claude Code](https://code.claude.com/docs/en/overview)。模型先选工具中适合代码修改的常用档位；只有在反复排错或调整复杂版式时，再考虑能力更强的模型，不必为了换姓名和照片专门购买最高档套餐。

先安装好上面的 LaTeX 环境，用 Agent 打开解压后的整个项目文件夹，给它真实的文字材料、照片路径和需要修改的页码。可以直接使用下面这段话：

```text
请先读 README.md、settings.tex 和 examples/content.tex。
我要把模板改成自己的[奖学金答辩/保研面试]演示，材料如下：[填写材料]。
先保留现有版式、字体与配色，修改封面信息和第[页码]页。
照片在 assets/[文件名]。缺少的经历、成绩和照片请问我，不要编造。
请直接修改项目文件，用 XeLaTeX 编译，并打开生成的 PDF 检查对应页面。
如果不能编译或不能查看页面，请说明限制，不要把“文件已改”当成“效果已检查”。
```

一次先改一两页，看到 PDF 后再继续。普通聊天工具也可以解释代码或帮助改文字，但若不能访问文件和编译环境，需要你自己把修改保存回项目并编译。AI 服务可能另行收费，不是使用模板的必要条件；提供材料前，请自行确认工具的数据设置和材料是否适合上传。

## 导出 PDF 与 PPT

**LaTeX 编译得到的是 PDF。** 可以直接用 PDF 放映；如果需要交 `.pptx`，建议先在 LaTeX 中完成修改，再按下面的顺序转换：

**PDF → 每页一张高清 PNG → 按顺序铺满 16:9 空白幻灯片 → 保存为 PPTX**

图片建议长边至少 1920 像素。这样可以保留版式，但图片里的文字不能在 PowerPoint 中逐字编辑；需要改稿时，回到 LaTeX 修改并重新导出。具体操作见 [PDF 转 PPT](PDF_TO_PPT.md)。

## 许可与致谢

代码和文档使用 [MIT 许可](LICENSE)，允许按其条款修改与再分发。字体遵循各自的 OFL 许可；建筑、学校标识、示例图片和联系二维码有各自的权利范围，不能把整个仓库的图片一概当作 MIT 素材。具体说明见 [ASSETS.md](ASSETS.md) 与 [CREDITS.md](CREDITS.md)。

自行使用或换校时，请检查学校标识的使用要求与替换素材的授权，保留应有署名。发布问题或改进建议欢迎使用 [Issues](https://github.com/eprogressing/scholarship-beamer/issues)；提交复现材料前，请去掉学号、电话和未公开内容。

制作过程中参考了 [TemplateNKU](https://github.com/GrokCV/TemplateNKU) 等 Beamer 项目与演示案例。感谢[霞鹜文楷](https://github.com/lxgw/LxgwWenKai)等字体项目；图片作者与参考来源已列在素材署名中。

## 定制与联系

如果你不熟悉 LaTeX，或者希望尽快拥有一份这样的答辩 PPT，可以加我的微信，找我**付费排版或定制**。

可沟通内容排版、换校配色、校徽与封面建筑定制，以及 PDF、图片版 PPTX 的整理交付。添加时备注 **「PPT 定制」**，附上学校、用途、截止时间和已有材料，先沟通需求与报价。

**源码免费获取，不需要加微信领取。** 委托排版和定制另行收费，不以保证获奖或录取为服务内容。

<img src="preview/wechat-qr.png" alt="作者微信二维码，添加时请备注 PPT 定制" width="360">
