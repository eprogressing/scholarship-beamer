# Scholarship Beamer

用于奖学金评审、评优答辩与个人展示的中文 LaTeX Beamer 模板，也可按面试要求改为保研、夏令营的自我介绍。

[![在 Overleaf 中打开](preview/open-in-overleaf.svg)](https://www.overleaf.com/docs?snip_uri=https%3A%2F%2Fgithub.com%2Feprogressing%2Fscholarship-beamer%2Freleases%2Flatest%2Fdownload%2Fscholarship-beamer-overleaf.zip&engine=xelatex&main_document=main.tex)

[下载源码](https://github.com/eprogressing/scholarship-beamer/releases/latest/download/scholarship-beamer-overleaf.zip) · [查看完整 PDF](https://github.com/eprogressing/scholarship-beamer/releases/latest/download/scholarship-beamer.pdf) · [换校教程](CUSTOMIZE.md) · [逐页填写指南](CONTENT_GUIDE.md)

## 效果预览

16:9 画幅，霞鹜文楷正文。封面保留校园建筑与渐变配色，正文提供个人介绍、科研图文、竞赛表格、证书墙和活动照片墙等版式。

![南开、中国农大、人大、厦大四校封面对照](preview/schools.jpg)

源码默认附南开版；中国农大、人大和厦大展示的是换校效果。学校名称、颜色、校徽和建筑都可以替换，方法见 [CUSTOMIZE.md](CUSTOMIZE.md)。

![个人介绍、科研、竞赛、学生工作、实践服务、总结与结尾](preview/pages.jpg)

## 快速开始

点击上方 **Open in Overleaf**，导入模板后修改内容即可。链接已指定 **XeLaTeX** 和主文件 **`main.tex`**，完整字体随项目提供，无需另外安装。

如果选择手动导入，下载 `scholarship-beamer-overleaf.zip`，在 Overleaf 中新建项目并上传 ZIP，编译器选择 XeLaTeX，主文件选择 `main.tex`。

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

默认 15 页按综合评优组织，不需要全部保留。用于保研或夏令营时，建议突出专业背景、研究经历、本人贡献与研究兴趣，再按需要删减其他章节。示例中的人物、场景、经历和成绩请替换为自己的真实材料。

<details>
<summary>本地编译</summary>

安装 XeLaTeX 和 latexmk 后，在项目目录运行：

```sh
latexmk -xelatex main.tex
```

生成 `main.pdf`。如需同时检查溢出、缺字与字体警告，可用 Python 3.9 或以上版本运行 `python3 scripts/build.py`，结果在 `build/main/main.pdf`。

</details>

## 导出 PDF 与 PPT

**LaTeX 编译得到的是 PDF。** 可以直接用 PDF 放映；如果需要交 `.pptx`，建议先在 LaTeX 中完成修改，再按下面的顺序转换：

**PDF → 每页一张高清 PNG → 按顺序铺满 16:9 空白幻灯片 → 保存为 PPTX**

图片建议长边至少 1920 像素。这样可以保留版式，但图片里的文字不能在 PowerPoint 中逐字编辑；需要改稿时，回到 LaTeX 修改并重新导出。具体操作见 [PDF 转 PPT](PDF_TO_PPT.md)。

## 许可与致谢

代码和文档使用 [MIT 许可](LICENSE)，字体遵循各自的 OFL 许可。建筑、学校标识、示例图片和联系二维码的权利说明分别见 [ASSETS.md](ASSETS.md) 与 [CREDITS.md](CREDITS.md)。这是非官方模板。

制作过程中参考了 [TemplateNKU](https://github.com/GrokCV/TemplateNKU) 等 Beamer 项目与演示案例。感谢[霞鹜文楷](https://github.com/lxgw/LxgwWenKai)等字体项目；图片作者与参考来源已列在素材署名中。

## 定制与联系

如果你不熟悉 LaTeX，或者希望尽快拥有一份这样的答辩 PPT，可以加我的微信，找我**付费排版或定制**。

可沟通内容排版、换校配色、校徽与封面建筑定制，以及 PDF、图片版 PPTX 的整理交付。添加时备注 **「PPT 定制」**，附上学校、用途、截止时间和已有材料，先沟通需求与报价。

源码免费使用；委托排版和定制另行收费。

<img src="preview/wechat-qr.png" alt="作者微信二维码，添加时请备注 PPT 定制" width="360">
