# 换校与替换素材

公开版以南开为默认示例，面向其他学校的同学使用。保留 `main.tex` 和默认加载语句，在 `settings.tex` 取消对应示例行的注释并修改即可；无需更换主文件或复制正文。设置写在 `\CampusSelect` 之后才会覆盖南开默认值。不要把南开的建筑换色后当作另一所学校。

1. 先填写 `CampusInfo` 中的题目、姓名、学院、专业和日期。
2. 配置学校中英文名、总结页校训与主题色。封面题目和总结校训分别设置。
3. 同时换掉彩色和白色两份校徽组合；没有标识时，显式清空两项，暂用文字校名。
4. 替换建筑及来源记录，更新个人页的成绩口径与实际经历。
5. 用 XeLaTeX 编译，检查封面、目录、章节、个人页、总结和结尾有无残留校名、标识或遮挡。

下面是一组覆盖配置，放在 `settings.tex` 原有配置之后。路径必须换成真实存在的文件，不能直接复制示例路径编译：

```tex
\CampusSetup{
 school={学校全称},english={UNIVERSITY NAME},motto={学校校训},
 primary=235C81,dark=163E59,accent=B78E60,
 logo={assets/my-mark.pdf},logo-white={assets/my-white-mark.pdf},
 landmark={建筑名称},artwork={assets/my-campus.png},
 artwork-trim={0 0 0 0}}
\CampusInfo{title={自己的汇报标题},subtitle={汇报用途},
 author={姓名},institute={学院名称},major={专业名称},date={年月}}
```

颜色填写六位十六进制值，不带 `#`；浅色和渐变由主题主色生成。校徽与建筑是独立图片，改主题色不会自动将它们重新着色。彩色校徽用于白底，白色校徽用于渐变底；两种标识均保持比例。

暂时没有可用标识时，可用以下配置替代上面的两条校徽路径，显示学校中英文名：

```tex
\CampusSetup{logo={},logo-white={}}
```

个人页满绩点和首门示例成绩分别来自 `\CampusGpaMax`、`\CampusCourseScore`，可在 `settings.tex` 覆盖；其余指标、课程与分数在 `examples/profile.tex` 填写，模板不会替不同学校换算成绩。

把自备PNG/JPG/PDF放进项目，路径使用项目内相对路径，不引用电脑的绝对路径。建筑插图建议约3.1:1，透明背景；两侧高、中间低，底边齐平。正文中的照片保留原比例，图注和来源单独编辑。封面中央文字区不应出现建筑主体。

`artwork-trim` 按左、下、右、上填写，单位默认bp；只用于裁透明留边，不能把主体裁没。替换后实际编译并检查封面、目录和结尾。透视双侧建筑是装饰性构图，不当作实景复原图。

维护者如需加入独立预设，可复制 `schools/nku.tex`，按真实信息改学校/学院/英文名/封面标题/校训/颜色/建筑路径/署名。随后将预设名加入 `beamerthemeCampus.sty` 的 `CampusSelect` 名单及 `scripts/build.py` 的入口映射，并提供对应演示入口。普通使用者直接覆盖 `settings.tex` 即可，不需要做这一步；正文始终只维护 `examples/` 中的一份。

默认头像为 `assets/student-portrait.jpg`；可在 `examples/profile.tex` 替换成自己的照片。照片建议约5:6，不将他人的照片或学校展示图片当作本人经历。各校计分制度不同，在 `NKUProfileMetrics` 中填写真实指标和分母，课程表可删减为0—10门。

每新增建筑请一并提供：原始来源链接、作者、许可证、修改说明、生成提示词（若使用AI）及校内标识使用依据（若附校徽）。不要只提供搜索引擎截图或一个GitHub链接。把建筑的作者和许可更新到 `CampusCredit`、`CampusSourceURL`、`CampusLicenseURL`，导出PDF会记录它们。

用于外发前，逐页检查没有占位成绩、原学校校名、误用图章或看不清的图注。默认五章针对评优/奖学金；毕业答辩应重组为背景、问题、方法、结果、总结，参考 CONTENT_GUIDE.md。

完整的自定义建筑署名可以在settings.tex里写：

```tex
\def\CampusCredit{Reference photo: AUTHOR; adapted drawing; LICENSE}
\def\CampusSourceURL{https://example.org/original-photo}
\def\CampusLicenseURL{https://creativecommons.org/licenses/by-sa/4.0/}
```

这里的示例URL和许可必须改成实际素材的来源与适用条款，不能把示例许可直接套给未知图片。
