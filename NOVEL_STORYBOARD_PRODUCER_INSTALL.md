# Novel Storyboard Producer

这是一个把连载小说章节转换为连续分镜、角色与场景参考资产、中文 Seedance 风格提示词、音色档案、声画同步设计及章节压缩包的 Codex Skill。

## 推荐安装方式

把下面这段话直接发给 Codex：

```text
请使用 skill-installer，从下面的 GitHub 子目录安装 novel-storyboard-producer：
https://github.com/luanqier/codex/tree/main/.agents/skills/novel-storyboard-producer

这是单文件 Skill，安装目录中只能保留 SKILL.md。安装前检查内容安全；若已有同名 Skill，先把旧目录压缩成带日期的 ZIP 备份，再移出 Skills 目录，然后安装最新版。不要把备份 ZIP、分享压缩包或其他说明文件放进 Skills 目录。安装后验证 SKILL.md，并告诉我最终安装路径、文件数量和验证结果；如未立即显示，请重新打开 Codex 或新建一个任务。
```

## 手动安装位置

只下载仓库中的 `.agents/skills/novel-storyboard-producer` 文件夹，并将整个文件夹复制到：

- 已设置 `CODEX_HOME`：`$CODEX_HOME/skills/novel-storyboard-producer`
- 未设置 `CODEX_HOME`：`~/.codex/skills/novel-storyboard-producer`

当前版本已经优化为单文件 Skill。只需保留完整的 `novel-storyboard-producer` 文件夹及其中的 `SKILL.md`，不要把日期备份 ZIP 解压到 Skills 目录。安装后如未立即显示，请重新打开 Codex或新建一个任务。

## 使用示例

```text
使用 $novel-storyboard-producer。小说原文：[粘贴正文或文件路径]；画面风格：[可选]。新项目先让我确认每章预计时长等默认设定，再制作完整章节分镜包。
```

## 更新方式

将 GitHub 子目录的最新版重新交给 Codex，并要求先比较本地同名 Skill；确认后再更新，避免覆盖个人定制规则。

## V6：连续打斗与对白升级（2026-10-01）

V6独立保留V5的文戏、资产、续作、QA和章节封包，打斗强化动作余势衔接、速度对比、位移支撑、受力反馈与动作摄影。参战角色可以讲话，第三方解说、旁白和内心独白不出声。

将这段话交给Codex安装：

```text
请使用skill-installer，从 https://github.com/luanqier/codex/tree/main/.agents/skills/novel-storyboard-producer-v6 安装 novel-storyboard-producer-v6。必须安装完整目录，保留references和vendor及其LICENSE，不要按旧版单文件说明只保留SKILL.md。V6的打斗模块在目录内，不依赖V5或action-comic-drama。保留已有V5；有同名V6时先比较并保留个人修改，再升级。安装后验证入口和引用，报告永久安装位置。
```

调用：`使用 $novel-storyboard-producer-v6`。已有项目从生产索引继续，批准资产、已完成段落和时长不因升级重做。V5继续保留；旧版单文件安装说明不适用于V6。
