# Novel Storyboard Producer

这是一个把连载小说章节转换为连续分镜、角色与场景参考资产、中文 Seedance 风格提示词、音色档案、声画同步设计及章节压缩包的 Codex Skill。

## 推荐安装方式

把下面这段话直接发给 Codex：

```text
请使用 skill-installer，从下面的 GitHub 子目录安装 novel-storyboard-producer：
https://github.com/luanqier/codex/tree/main/.agents/skills/novel-storyboard-producer

安装前检查目录与脚本安全；安装到个人 Skills 目录。若已有同名 Skill，先比较差异，不要直接覆盖。安装后验证 SKILL.md、agents/openai.yaml 和 scripts，并告诉我最终安装路径与验证结果。
```

## 手动安装位置

只下载仓库中的 `.agents/skills/novel-storyboard-producer` 文件夹，并将整个文件夹复制到：

- 已设置 `CODEX_HOME`：`$CODEX_HOME/skills/novel-storyboard-producer`
- 未设置 `CODEX_HOME`：`~/.codex/skills/novel-storyboard-producer`

不要只复制 `SKILL.md`；`agents`、`references` 和 `scripts` 都是必需组成部分。安装后如未立即显示，请重新打开 Codex 或新建一个任务。

## 使用示例

```text
使用 $novel-storyboard-producer。小说原文：[粘贴正文或文件路径]；画面风格：[可选]。新项目先让我确认每章预计时长等默认设定，再制作完整章节分镜包。
```

## 更新方式

将 GitHub 子目录的最新版重新交给 Codex，并要求先比较本地同名 Skill；确认后再更新，避免覆盖个人定制规则。
