---
title: ComfyUI API出图返回、下载地址与防重名方案
created: 2026-06-02
tags:
  - ComfyUI
  - API
  - 工作流
  - 图片转存
  - 自动化
status: reference
---

# ComfyUI API出图返回、下载地址与防重名方案

## 背景

通过 API 调用 ComfyUI 工作流已经可以成功提交任务、查询任务状态，并拿到返回结果。但返回数据通常不是一个完整的文件下载地址，而是类似下面这样的结构：

```json
{
  "code": 0,
  "msg": "查询成功",
  "data": {
    "prompt_id": "35340731-7c3c-4467-ac97-10c2191e2da2",
    "status": 3,
    "progress_num": 100,
    "outputs": {
      "201": {
        "images": [
          {
            "filename": "output_00001_.png",
            "subfolder": "",
            "type": "output"
          }
        ]
      }
    }
  }
}
```

这里有两个实际问题：

1. 返回的是 `filename/subfolder/type`，不是完整下载 URL。
2. 如果所有任务都叫 `output_00001_.png`，有重名或误取结果的风险。

## 核心结论

ComfyUI 的 `SaveImage` 节点天然只返回文件描述信息：

- `filename`
- `subfolder`
- `type`

完整下载地址需要由调用端拼接：

```text
http://COMFYUI_HOST/view?filename=文件名&subfolder=子目录&type=output
```

例如：

```text
http://127.0.0.1:8188/view?filename=output_00001_.png&subfolder=&type=output
```

如果 ComfyUI 部署在服务器，则把 `127.0.0.1:8188` 换成实际可访问的 ComfyUI 地址。

## 文件名防重复方案

不要让所有工作流都使用固定的：

```text
output
```

推荐每次 API 调用前动态设置 `SaveImage.filename_prefix`。

推荐格式：

```text
api/%year%-%month%-%day%/%hour%%minute%%second%/output
```

或者由调用端传入唯一任务 ID：

```text
api/{job_id}/output
```

这样即使文件名仍然是：

```text
output_00001_.png
```

实际保存路径也会变成：

```text
output/api/2026-06-02/204501/output_00001_.png
```

返回结构类似：

```json
{
  "filename": "output_00001_.png",
  "subfolder": "api/2026-06-02/204501",
  "type": "output"
}
```

重点是：文件名可以重复，但 `subfolder` 必须唯一。

## 推荐调用流程

1. 后端生成唯一 `job_id`。
2. 提交 ComfyUI 前，把工作流里 `SaveImage` 节点的 `filename_prefix` 改成 `api/{job_id}/output`。
3. 调用 `/prompt` 提交任务。
4. 轮询 `/history/{prompt_id}` 或自己的封装查询接口。
5. 从 `outputs` 里读取 `filename/subfolder/type`。
6. 拼接 `/view` 下载地址。
7. 后端下载图片二进制。
8. 上传到自己的业务系统或对象存储。
9. 返回业务系统自己的图片 URL。

## Python 示例

```python
from urllib.parse import urlencode
import datetime
import uuid
import requests

COMFY = "http://127.0.0.1:8188"

job_id = str(uuid.uuid4())
date = datetime.datetime.now().strftime("%Y%m%d")

# 假设 SaveImage 节点 id 是 201
prompt["201"]["inputs"]["filename_prefix"] = f"api/{date}/{job_id}/output"

# 1. 提交任务
resp = requests.post(f"{COMFY}/prompt", json={"prompt": prompt})
prompt_id = resp.json()["prompt_id"]

# 2. 查询结果
history = requests.get(f"{COMFY}/history/{prompt_id}").json()
outputs = history[prompt_id]["outputs"]

result_images = []

for node_id, node_output in outputs.items():
    for image in node_output.get("images", []):
        query = urlencode({
            "filename": image["filename"],
            "subfolder": image.get("subfolder", ""),
            "type": image.get("type", "output"),
        })

        download_url = f"{COMFY}/view?{query}"
        image_bytes = requests.get(download_url).content

        # 上传到自己的系统或 OSS
        # final_url = upload_to_your_system(image_bytes)

        result_images.append({
            "node_id": node_id,
            "filename": image["filename"],
            "subfolder": image.get("subfolder", ""),
            "type": image.get("type", "output"),
            "comfy_download_url": download_url,
            # "final_url": final_url,
        })
```

## 能否只靠工作流节点解决

### 可以解决：文件名和路径唯一性

可以直接通过 `SaveImage.filename_prefix` 解决。

方案一：直接在节点里写时间变量：

```text
api/%year%-%month%-%day%/%hour%%minute%%second%/output
```

方案二：通过调用端传入唯一字符串，连接到 `SaveImage.filename_prefix`。

### 不能完全解决：完整下载地址

原生 `SaveImage` 不会返回完整下载 URL，只返回 `filename/subfolder/type`。

下载 URL 应该由调用端拼：

```text
/view?filename=xxx&subfolder=xxx&type=output
```

### 如果想完全工作流化

可以写一个自定义节点：

```text
Save Image With URL
```

它做三件事：

1. 保存图片。
2. 返回 `filename/subfolder/type`。
3. 同时返回完整 `/view` URL。

如果业务上还要转存到其他系统，也可以写成：

```text
Save And Upload Image
```

这个节点负责：

1. 保存图片。
2. 读取本地文件。
3. 上传到目标系统或对象存储。
4. 返回最终业务图片 URL。

## 推荐架构

最稳的方案是：

```text
ComfyUI 只负责生成和保存图片
后端负责拼接 /view 下载地址
后端负责下载图片
后端负责上传到业务系统
后端返回最终图片 URL
```

不建议直接把 ComfyUI 的本地 `/view` 地址暴露给外部用户，因为它通常只是内部服务地址，也不适合承担长期文件托管。

## 检查清单

- [ ] 每次任务有唯一 `job_id`。
- [ ] `SaveImage.filename_prefix` 包含日期或 `job_id`。
- [ ] 返回结果读取的是 `filename/subfolder/type` 三个字段。
- [ ] 下载 URL 使用 `urlencode` 拼接，避免中文、空格、斜杠出错。
- [ ] 下载后转存到自己的系统或对象存储。
- [ ] 对外返回最终系统 URL，而不是 ComfyUI 内部 URL。

## 一句话结论

文件名重复靠 `filename_prefix` 解决；图片下载靠 `/view` 拼接解决；最终转存应该放在调用端或自定义保存节点里完成。
