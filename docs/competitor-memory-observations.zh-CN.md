# PurePin、Shottr 与 Snipaste：一次大图贴图观察

[English](competitor-memory-observations.md) · 简体中文

这份记录复用 2026-09-12 的本机调查，没有重新运行测试。它提供一个具体场景的参考：导入一张 4096 × 4096 px 图片时，三款工具分别保留了多少内存。显示尺寸、进程使用历史和导入路径未完全对齐，因此不能据此给产品排名或计算内存节省比例。

## 条件

- 系统：macOS 26.5.2（25F84），三款应用均运行 ARM64 普通发行构建；每款只有一个进程会话。
- 版本：PurePin v0.9.0；Shottr 1.9.1 build 128；Snipaste 2.10.8。
- 素材：4096 × 4096 px、不透明 RGBA 规则彩色块，原始像素 64 MiB。PNG 为 1,418,239 bytes，SHA-256 为 `885602152f4da18b4b25a502e733d784a122f62c6eb7846ef55991aef1964c6c`。
- 指标：macOS `footprint` 的 Dirty 合计。MiB = 1,048,576 bytes。Dirty 包含 Swapped，Wired 是其中的子集，不能重复相加；这里不采用 RSS，也不把它等同于整机实际 RAM 成本。
- 采样：按明确 PID 与执行文件定位，核对采样前后的进程身份，保留 `footprint` 和 `vmmap` 记录。采样命令成功不代表 UI 操作成功，两者分别记录。

## 观察到的阶段

| 工具与阶段 | Dirty 合计 | 观察状态 |
| :--- | ---: | :--- |
| PurePin，贴图前 | 29.44 MiB | 已使用的常驻进程，尚无测试贴图 |
| PurePin，贴图可见 | 122.19 MiB | 用户确认通过实际快捷键贴出测试图 |
| PurePin，确认关闭后 | 58.67 MiB | 用户确认关闭；具体关闭时刻未知 |
| PurePin，再过约 102 秒 | 58.69 MiB | 同一进程，无中间操作 |
| Shottr，导入前 | 101.91 MiB | 已使用的进程，之前打开过其他截图 |
| Shottr，图像编辑 | 199.92 MiB | 测试图可见 |
| Shottr，贴图可见 | 200.09 MiB | 测试图可见，界面显示 50% |
| Shottr，执行 Close All 后 | 198.83 MiB | 关闭状态未确认，不作关闭后成绩 |
| Snipaste，导入前 | 39.30 MiB | 新启动，持久化贴图状态未完整核验 |
| Snipaste，导入后 | 697.58 MiB | 采样时未核验窗口；后续目视确认测试图已贴出 |
| Snipaste，尝试关闭后 | 699.44 MiB | 关闭状态未确认，不作关闭后成绩 |
| Snipaste，后续观察 | 699.47 MiB | 没有再次导入，窗口状态仍未确认 |

PurePin 显示阶段的 ImageIO Dirty 为 64 MiB，确认关闭后该分类消失，支持原图存储已释放；IOSurface 仍保留约 17.06 MiB。Snipaste 导入后的约 697.58 MiB 中，IOSurface Dirty 约为 524.09 MiB。分类说明了本次内存由什么构成，不能单独证明泄漏或某个框架存在缺陷。

## 为什么只作为参考

PurePin 按可用屏幕范围拟合贴图，Shottr 界面显示 50%，Snipaste 的显示尺寸没有与另外两款统一。图形缓冲可能随显示尺寸变化。PurePin、Shottr 也不是从全新进程开始，导入前的状态不同，因此不能简单相减后把差值当作可比的单图成本。

Shottr、Snipaste 使用原始 PNG；PurePin 使用 Shottr 复制到剪贴板后重新编码的 PNG，尺寸仍为 4096 × 4096，但未做解码后逐像素一致性检查。素材是容易压缩的规则图，不代表照片、随机噪声或普通屏幕截图；这个方图的像素数也大于当时的单屏截图。

Shottr 和 Snipaste 的关闭动作没有可靠核验，不能把相关数值称为“关掉仍占用”。Snipaste 还区分隐藏、可恢复的关闭和销毁，其保留状态的功能成本需要单独考虑。[Snipaste 官方操作说明](https://github.com/Snipaste/feedback/wiki/Getting-Started)

这批旧版本、旧系统的数据也不能与 [9 月 21 日 PurePin 连续截图测试](memory-report.zh-CN.md) 拼成同一场横向测试。后者使用带插桩的 Release 构建，任务与测量口径均不同。这里没有测响应速度、CPU、能耗或总体性能。

## 数据

[横向条形图](../assets/competitor-memory.svg) 从零刻度绘制，并标出各产品当时测试的版本或 build。安装 `matplotlib==3.10.8` 后运行 `python script/render_competitor_memory.py` 可从下方 JSON 重新生成；该脚本不运行应用或重新采样。

[脱敏采样摘要](data/competitor-memory-2026-09-12.json) 保留全部 14 次探索采样的时间、版本、字节数、分类数值和采样时的状态说明，包括未成功触发贴图与关闭未确认的记录。Snipaste 导入窗口的后续确认单独标注，不改写采样时的核验状态。摘要不含截图像素、用户路径或原始堆转储，不能替代完整的本地原始记录。

[返回 PurePin](../README.zh-CN.md)
