# Git 接入说明

## 当前用途

Git 用来保护 AI-Brain 的核心记忆、规则、Skill、项目笔记和系统配置，让重要修改可以回滚和迁移。

## 当前跟踪范围

优先跟踪：

- Markdown 笔记
- AI-Brain 系统规则
- Skill 文件
- 模板
- 轻量项目源码
- Codex/Agent 工作说明

默认忽略：

- `outputs/`
- `node_modules/`
- 临时 PDF 图片目录
- 视频渲染结果
- Obsidian 本地 workspace 状态

## 日常使用

查看状态：

```text
git status
```

提交一次快照：

```text
git add .
git commit -m "Update AI-Brain"
```

查看最近提交：

```text
git log --oneline -5
```

## 注意事项

- 大型 PPT、视频、音频和渲染输出先不进入 Git。
- 如果某个成品文件必须长期保存，建议单独放对象存储、网盘或后续接 Git LFS。
- 涉及原则库、自我模型、决策日志的大改，提交前先确认内容准确。

## 2026-06-07 初始接入策略

先建立本地 Git 仓库和第一版核心快照，不立即绑定远程仓库。远程仓库需要用户确认平台和仓库地址后再添加。
