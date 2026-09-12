# PurePin

**Capture. Annotate. Pin.**

专注日常截图、基础标注与置顶的原生 macOS 工具。面向绝大部分时间只需要这三件事的用户：截下需要的内容，做一点标注，复制出去或贴在屏幕旁，然后回到手头的工作。

PurePin 使用 Swift 与 AppKit，截图和图像处理在本机完成。没有账户、云端历史、分析 SDK 或自动崩溃上报。

## 下载

**首个正式安装包仍在准备中。** 正式版本将通过 [GitHub Releases](https://github.com/easyrev/PurePin/releases) 提供。系统要求为 macOS 26 或更新版本，计划提供同时包含 Apple Silicon 与 Intel 的 Universal 安装包。

PurePin 当前闭源。公开仓库只提供用户文档、发布制品与反馈入口，不包含应用源码。

## 三件事

- **截图**：区域截图、窗口区域选择、整个显示器截图，支持像素级调整。
- **基础标注**：矩形、线条、箭头、画笔、文字、马赛克和模糊；直接选择与移动对象，支持撤销和重做。
- **置顶**：把截图或剪贴板图片贴在屏幕上，拖动、缩放、复制、保存；可以同时放多张，也可以一键隐藏和恢复。

## 快速使用

| 操作 | 默认快捷键 |
| --- | --- |
| 开始截图 | `F1` |
| 贴剪贴板图片 | `F3` |
| 隐藏 / 恢复全部贴图 | `Shift + F3` |
| 复制截图并结束 | `Return` 或 `⌘C` |
| 保存 PNG | `⌘S` |
| 将当前截图置顶 | `⌘T` |
| 撤销 / 重做 | `⌘Z` / `⇧⌘Z` |

功能键被系统占用时，加 `fn` / 地球仪键，或在 Settings 更改快捷键。截图时先拖动选区，也可以直接点击鼠标下的窗口区域。Pin 图片可拖动移动、滚动缩放，双击关闭；右键菜单提供复制、保存和恢复原尺寸。

首次截图需要在系统的 **Privacy & Security → Screen & System Audio Recording** 中允许 PurePin。应用使用静态截图接口，不录制音频。不需要 Accessibility、Camera 或 Microphone 权限。

## 保持专注

PurePin 不做 OCR、AI、录屏/GIF、复杂图像编辑、截图历史、云同步或插件系统。它们是其他工具擅长的工作；PurePin 把精力放在截图、基础标注与置顶的操作细节和资源使用上。

性能主张以具体构建和可复现测量为依据。当前不宣称“最快”“零内存占用”或固定的人群覆盖率。

## 隐私与反馈

应用不自建持续追加的日志文件。诊断使用 macOS 统一日志与系统崩溃报告，不自动上传；系统仍可能保留日志并占用磁盘。**Copy Support Info** 只在你点击时复制基本版本信息，供你自行提交。

[隐私与磁盘使用](PRIVACY.md) · [使用与反馈指南](SUPPORT.md) · [报告问题](https://github.com/easyrev/PurePin/issues)

Copyright © 2026 PurePin. All rights reserved.
