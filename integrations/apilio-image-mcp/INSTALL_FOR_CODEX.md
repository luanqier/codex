# Codex 执行任务：接入 Apilio 图片模型

你是接手安装的 Codex。请直接执行本文件中的流程，不要只给用户解释步骤。

## 目标

在当前 Windows 电脑的 Codex 中注册一个本地 STDIO MCP 服务：

- MCP 名称：`apilio_image`
- 工具名称：`generate_image`
- 模型：`gemini-3.1-flash-lite-image`
- API Base URL：`https://api.apilio.ai`
- API Key 环境变量：`APILIO_API_KEY`

完成标准：重启 Codex 后，真实调用 `generate_image` 生成一张测试图，文件能打开且图片
预览正常。不要只以配置文件存在作为完成依据。

## 强制安全规则

1. 不得把 API Key 写进 Git、Markdown、脚本、Codex 回复、命令输出或 `config.toml`。
2. 不得执行会回显密钥的命令，例如 `echo $env:APILIO_API_KEY`。
3. 密钥只保存为 Windows 用户环境变量 `APILIO_API_KEY`。
4. 如果用户尚未提供密钥，暂停密钥和联网验收环节，明确请求用户通过安全输入提供。
5. 修改已有 `config.toml` 前先读取并保留其他配置；不得覆盖整个文件。

## 自动安装

在 PowerShell 中运行以下命令。先下载并审查脚本，再执行：

```powershell
$work = Join-Path $env:TEMP 'apilio-image-mcp-install'
New-Item -ItemType Directory -Force -Path $work | Out-Null
$base = 'https://raw.githubusercontent.com/luanqier/codex/main/integrations/apilio-image-mcp'
Invoke-WebRequest "$base/server.py" -OutFile (Join-Path $work 'server.py')
Invoke-WebRequest "$base/install.ps1" -OutFile (Join-Path $work 'install.ps1')
Get-Content -Raw (Join-Path $work 'install.ps1')
& (Join-Path $work 'install.ps1')
```

`install.ps1` 会：

- 检查 Python；
- 安装 `server.py` 到 `%USERPROFILE%\.codex\mcp\apilio-image\server.py`；
- 仅在缺失时向 `%USERPROFILE%\.codex\config.toml` 追加 MCP 配置；
- 若当前进程不存在 `APILIO_API_KEY`，用隐藏输入读取并保存到用户环境变量；
- 编译检查 `server.py`。

如果用户已经提前设置了用户环境变量，脚本不会要求再次输入。

## 应有的 Codex 配置

最终配置应等价于下面内容。路径会由安装脚本写成目标电脑的绝对路径：

```toml
[mcp_servers.apilio_image]
command = "python"
args = ["C:\\Users\\<用户>\\.codex\\mcp\\apilio-image\\server.py"]
env_vars = ["APILIO_API_KEY"]
startup_timeout_sec = 30
tool_timeout_sec = 240
```

注意：`env_vars` 只写变量名，不写变量值。

## 重启与验收

Codex 通常需要完全退出并重新打开，才能加载新 MCP 服务和新用户环境变量。安装脚本结束
后请明确提醒用户重启 Codex，然后在重启后的新任务里继续验收。

验收提示词：

```text
请使用 apilio_image 的 generate_image 工具生成一张 1:1 测试图：
一只橙色小猫坐在未来感工作台前，柔和电影光线，细节清晰，不要文字。
保存到我的 Pictures/Codex-Apilio 目录，并把生成图片展示给我。
```

验收时检查：

1. Codex 能看到 `apilio_image` / `generate_image`；
2. 请求确实使用 `gemini-3.1-flash-lite-image`；
3. 返回结果不是报错或空 URL；
4. 本地文件存在、大小大于 0，并能正常读取；
5. 在回复中显示图片的绝对路径和预览。

## 常见故障

- 找不到工具：完全退出并重启 Codex，随后检查 `config.toml` 的路径。
- 提示缺少密钥：确认密钥已设为“用户”环境变量，然后重启 Codex。
- Python 找不到：安装 Python 3.10+，或把配置中的 `command` 改为有效 Python 路径。
- 401/403：密钥无效、余额或账户权限问题；不要打印密钥排查。
- 超时：保持 `tool_timeout_sec = 240`，确认可访问 `api.apilio.ai`。
- 接口返回结构变化：只修改 `server.py` 的响应解析逻辑，保留 MCP 工具协议与密钥隔离。

## 完成回报格式

完成后向用户简短报告：安装路径、MCP 名称、测试图片路径、真实生成是否成功。不要回报或
部分展示密钥。若因为必须重启而暂时无法继续，应说明“安装已完成，等待重启后验收”，
不得声称已经跑通。
