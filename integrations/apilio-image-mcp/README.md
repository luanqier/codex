# Apilio Image MCP for Codex

把 Apilio 的 `gemini-3.1-flash-lite-image` 接入 Codex，提供一个可直接调用的
`generate_image` MCP 工具。工具会生成图片、保存到本机，并把图片预览返回给 Codex。

## 交给另一个 Codex 自动安装

把下面这段话原样发给另一个 Codex：

```text
请读取并严格执行下面的接入文档：
https://raw.githubusercontent.com/luanqier/codex/main/integrations/apilio-image-mcp/INSTALL_FOR_CODEX.md

这是执行任务，不是咨询任务。请完成环境检查、文件安装、Codex MCP 配置、API Key
安全设置、重启提醒和真实图片生成验收。不要把 API Key 写入仓库、聊天回复、日志或
config.toml；如果缺少密钥，只向我索取密钥，然后使用安全输入或系统用户环境变量保存。
```

## 功能

- 模型：`gemini-3.1-flash-lite-image`
- 接口：`POST https://api.apilio.ai/v1/images/generations`
- MCP 工具：`generate_image`
- 运行依赖：Python 3.10+，仅使用标准库
- 默认输出：`~/Pictures/Codex-Apilio`
- 密钥来源：环境变量 `APILIO_API_KEY`

## 文件

- `server.py`：MCP 服务端
- `install.ps1`：Windows 安装脚本，不接收明文密钥参数
- `INSTALL_FOR_CODEX.md`：给 Codex 执行的完整交接说明

## 安全边界

本仓库不包含 API Key。安装脚本只配置 MCP 文件和 `config.toml`，密钥必须在目标电脑
上通过安全输入设置为 Windows 用户环境变量。公开仓库中的代码应在执行前由接手的
Codex 检查。
