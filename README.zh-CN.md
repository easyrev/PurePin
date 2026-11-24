<div align="center">

<img src="assets/icon.svg" width="80" alt="PurePin 图标" />

# PurePin

### Capture. Edit. Pin.

极简、原生的 macOS 截图工具。

[English](README.md) · 简体中文

For those tired of signing in, dismissing upgrade prompts,<br />
and digging through features just to take a screenshot.

</div>

<br />

| Capture | Edit | Pin |
| :--- | :--- | :--- |
| 多屏区域、窗口区域或整屏截图。放大镜实时取色，支持像素级微调选区。 | 标注截图或剪贴板图片。矩形、直线、箭头、文字、画笔、模糊与马赛克，支持撤销与重做。 | 将截图或剪贴板图片置顶，支持透明图。拖动、缩放、调透明度、一键隐藏恢复或重新进入编辑。 |

无账户，无云端历史。截图和图像处理都在本机完成。[隐私说明 →](PRIVACY.zh-CN.md)

## 内存实测

三个场景，各连续截图 20 次；结束后 20 秒空闲阶段的内存中位数为 **21.5–32.7 MiB**。

<img src="assets/memory-report.svg" width="960" alt="PurePin v0.9.9 的 20 轮截图内存记录：三条曲线保留全部关闭后样本，末尾空闲中位数为 21.52–32.66 MiB" />

使用带测量插桩的 Release 构建。图中为每轮关闭后的内存；截图可见时，采样最高值为 22–41 MiB。[测试方法与数据 →](docs/memory-report.zh-CN.md)

### 大图贴图：PurePin、Shottr、Snipaste

4096 × 4096 px 彩色测试图，贴图时的进程内存。每款各记录一次，版本见图中标注。

<img src="assets/competitor-memory.svg" width="960" alt="大图贴图的单次探索记录：PurePin v0.9.0 为 122.19 MiB，Shottr 1.9.1 build 128 为 200.09 MiB，Snipaste 2.10.8 为 697.58 MiB。显示尺寸、导入路径和此前状态不同，仅供参考。" />

测量口径为 macOS `footprint` 的 Dirty 合计。三款的贴图显示尺寸、导入路径和此前使用状态不同，这组记录仅供参考。[测试条件与完整记录 →](docs/competitor-memory-observations.zh-CN.md)

## 获取 PurePin

[下载 PurePin →](https://github.com/easyrev/PurePin/releases)

**macOS 26+** · Apple Silicon 版 / Universal 版（Apple Silicon + Intel）

## 安装与首次启动

打开 DMG，把 PurePin 拖入「应用程序」，再从那里启动。对于标明 **未公证** 的版本，macOS 可能阻止首次启动。尝试打开后，进入 **系统设置 → 隐私与安全性**，在页面下方找到有关 PurePin 的提示，点击 **仍要打开**，再确认系统弹窗。具体步骤见 [Apple 的说明](https://support.apple.com/zh-cn/102445)。

首次启动时，如果尚未授权，PurePin 会显示截屏准备窗口。点击 **Allow Screen Recording**，先完成 macOS 的授权弹窗。需要手动开启时，点击 **Open System Settings** 进入 **隐私与安全性 → 屏幕与系统音频录制**，允许 PurePin；如果系统要求退出并重新打开，按提示操作。准备窗口显示已就绪后，点击 **Done** 关闭，再自己按 **F1** 开始截图。授权过程中不会启动或排队等待截图。

这个权限用于获取静态截图；应用不录制音频，也不需要辅助功能、相机或麦克风权限。

## 快捷键

| 想做什么 | 默认快捷键 |
| :--- | :--- |
| 开始截图 | <kbd>F1</kbd> |
| 编辑剪贴板中的图片 | <kbd>⌥</kbd> + <kbd>F1</kbd> |
| 贴出剪贴板中的图片 | <kbd>F3</kbd> |
| 隐藏 / 恢复全部贴图 | <kbd>⇧</kbd> + <kbd>F3</kbd> |
| 复制放大镜当前像素色值（`#RRGGBB`） | <kbd>C</kbd> |
| 全选当前屏幕 | <kbd>⌘</kbd> + <kbd>A</kbd> |
| 复制当前截图并结束编辑 | <kbd>Return</kbd>、<kbd>⌘</kbd> + <kbd>C</kbd> 或选区内双击 |
| 把当前截图贴在屏幕上 | <kbd>⌘</kbd> + <kbd>T</kbd> |
| 保存 PNG | <kbd>⌘</kbd> + <kbd>S</kbd> |
| 调节线宽、字号或模糊/马赛克强度 | <kbd>[</kbd> / <kbd>]</kbd> 或滚轮 |
| 撤销 / 重做 | <kbd>⌘</kbd> + <kbd>Z</kbd> / <kbd>⇧</kbd> + <kbd>⌘</kbd> + <kbd>Z</kbd> |

功能键被系统占用时，试试加上 <kbd>fn</kbd> / 地球仪键，或在 Settings 中更换、清空任意全局快捷键。

锁定选区前移动鼠标可直接在多块屏幕间切换，右键可回退步骤或解锁空选区。拖拽时按住 <kbd>Shift</kbd> 可约束正方形以及 45° 直线/箭头。

标注已有图片时，复制图片本身或在 Finder 中直接复制图片文件（支持 PNG、JPEG、HEIC、WebP、TIFF），再从菜单栏选择 **Edit Clipboard Image**。按住空格可拖动画布，最高支持 16× 缩放；缩放和平移只改变查看范围，未裁剪时复制、保存和贴图均保留原图像素尺寸。编辑剪贴板图片不需要屏幕录制权限。

贴图可以拖动位置、方向键微调、滚轮或双指捏合缩放，按住 <kbd>⌥</kbd> 滚动可调节透明度，双击关闭；右键菜单或 <kbd>⌘</kbd> + <kbd>E</kbd> 可复制、保存、恢复原尺寸或透明度，或直接重新进入标注编辑。

---

<div align="center">

[获取 PurePin](#获取-purepin) · [隐私](PRIVACY.zh-CN.md) · [使用与反馈](SUPPORT.zh-CN.md)

<sub>PurePin 目前闭源，此仓库用于分发与反馈。Copyright © 2026 PurePin.</sub>

</div>
