<div align="center">

<img src="assets/icon.svg" width="96" alt="PurePin 图标" />

# PurePin

### 截下来，标两笔，贴在手边。

一款专注截图、标注与贴图的原生 macOS 小工具。

[发布进度](#获取-purepin) · [快速上手](#快速上手) · [反馈问题](https://github.com/easyrev/PurePin/issues)

<br />

<img src="assets/hero.svg" width="960" alt="PurePin：截图、原地标注与贴图的功能示意" />

<sub>macOS 26+ · Swift + AppKit · 本机处理</sub>

</div>

<br />

我写 PurePin，是因为自己大多数时候只需要几件事：截一块屏幕，画个箭头，复制发出去；偶尔把一张图贴在旁边，方便对照。希望这些动作顺手、安静，做完就能回到手头的事。

PurePin 就围绕这条很短的工作流打磨。

## 留下需要的那一小块

按下 <kbd>F1</kbd>，拖出选区，或者直接点击窗口区域。需要更准确时，还可以微调边界。

**给别人看。** 在选区里直接加箭头、文字或方框。完成标注后，按 <kbd>Return</kbd> 复制，然后粘贴到聊天或文档。箭头、文字等标注可以重新选中、移动，也支持撤销和重做。

**留给自己看。** 按 <kbd>⌘</kbd> + <kbd>T</kbd> 把当前截图贴在屏幕上。对照设计稿、记住几行参数，或者把参考图放在正在做的事情旁边。贴图可以拖动、缩放，也可以一起隐藏，等需要时再恢复。

**已经有一张图。** 复制图片后按 <kbd>F3</kbd>，直接贴出来。需要留存时保存 PNG；只是临时参考，用完双击关闭即可。

## 少一点，也够用

标注工具有矩形、线条、箭头、画笔、文字、马赛克和模糊。它们围绕一张截图工作，不需要先把图片送进另一个编辑器。

PurePin 没有截图历史库、账户或云同步，也不做 OCR、AI、录屏和复杂图像编辑。这些功能各有用处，我想先把日常反复使用的几个动作做好。

截图、标注和贴图都在本机完成。没有分析 SDK，也不会自动上传截图或崩溃报告。[了解隐私与磁盘使用 →](PRIVACY.md)

## 获取 PurePin

**首个正式安装包还在准备中。** 发布后会放在 [GitHub Releases](https://github.com/easyrev/PurePin/releases)，目前尚无可下载版本。

需要 **macOS 26 或更新版本**。计划提供 Apple Silicon 与 Universal 安装包，最终以发布页列出的构建为准。

## 快速上手

首次截图时，需要在系统设置的 **隐私与安全性 → 屏幕与系统音频录制** 中允许 PurePin。这个权限用于获取静态截图；应用不录制音频，也不需要辅助功能、相机或麦克风权限。

| 想做什么 | 默认快捷键 |
| :--- | :--- |
| 开始截图 | <kbd>F1</kbd> |
| 贴出剪贴板中的图片 | <kbd>F3</kbd> |
| 隐藏 / 恢复全部贴图 | <kbd>⇧</kbd> + <kbd>F3</kbd> |
| 复制当前截图并结束编辑 | <kbd>Return</kbd> 或 <kbd>⌘</kbd> + <kbd>C</kbd> |
| 把当前截图贴在屏幕上 | <kbd>⌘</kbd> + <kbd>T</kbd> |
| 保存 PNG | <kbd>⌘</kbd> + <kbd>S</kbd> |
| 撤销 / 重做 | <kbd>⌘</kbd> + <kbd>Z</kbd> / <kbd>⇧</kbd> + <kbd>⌘</kbd> + <kbd>Z</kbd> |

功能键被系统占用时，试试加上 <kbd>fn</kbd> / 地球仪键，或在 Settings 中换成顺手的快捷键。

贴图可以拖动位置、滚动缩放，双击关闭；右键菜单里可以复制、保存或恢复原尺寸。

## 再多了解一点

<details>
<summary><strong>退出后，贴图还会回来吗？</strong></summary>

不会。Pin 是临时放在屏幕上的参考图，不会自动保存，退出应用后也不会恢复。需要留下的图片，请先保存。

</details>

<details>
<summary><strong>源码在哪里？</strong></summary>

PurePin 目前闭源。这个公开仓库用于提供文档、安装包和反馈入口，不包含应用源码。

</details>

<details>
<summary><strong>遇到问题，怎么反馈？</strong></summary>

欢迎在 [Issues](https://github.com/easyrev/PurePin/issues) 描述你做了什么、期望发生什么，以及实际发生了什么。菜单栏里的 **Help & Feedback… → Copy Support Info** 可以复制版本信息，之后由你决定是否贴到反馈中。

如果附图，请尽量用不包含私人或工作信息的示例。[详细反馈指南 →](SUPPORT.md)

</details>

<br />

---

<div align="center">

做一个自己每天愿意用的小工具。

[发布进度](https://github.com/easyrev/PurePin/releases) · [隐私说明](PRIVACY.md) · [使用与反馈](SUPPORT.md)

<sub>Copyright © 2026 PurePin. All rights reserved.</sub>

</div>
