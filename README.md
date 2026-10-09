<div align="center">

<img src="assets/icon.svg" width="80" alt="PurePin icon" />

# PurePin

### Capture. Edit. Pin.

A small, native screenshot app for macOS.

English · [简体中文](README.zh-CN.md)

For those tired of signing in, dismissing upgrade prompts,<br />
and digging through features just to take a screenshot.

</div>

<br />

| Capture | Edit | Pin |
| :--- | :--- | :--- |
| Capture a region, a window area, or the whole screen. Adjust the selection down to the pixel. | Annotate a capture or clipboard image with arrows, text, and freehand strokes. Undo and redo as you go. | Keep a screenshot or clipboard image on top. Move, resize, hide, and restore it. |

No account or cloud history. Screenshots and image processing stay on your Mac. [Privacy →](PRIVACY.md)

## Memory

Three scenarios, 20 captures each. Median memory use during the final 20 seconds of idle time: **35.1–35.7 MiB**.

<img src="assets/memory-report.svg" width="960" alt="PurePin v0.9.0 memory after each of 20 capture cycles in three scenarios. Final idle medians range from 35.13 to 35.74 MiB." />

Measured with an instrumented Release build. The chart shows memory after each capture closes; the highest samples while capturing were 101–105 MiB. [Method and data →](docs/memory-report.md)

### Pinning a large image: PurePin, Shottr, Snipaste

A 4096 × 4096 px color test image, pinned on screen. One observation per app, using the versions shown below.

<img src="assets/competitor-memory.svg" width="960" alt="Exploratory Pin memory observations: PurePin v0.9.0, 122.19 MiB; Shottr 1.9.1 build 128, 200.09 MiB; Snipaste 2.10.8, 697.58 MiB. Display sizes, import paths, and prior app states differ." />

Measured as total Dirty memory in macOS `footprint`. Display sizes, import paths, and prior app states differed, so treat these as exploratory observations. [Conditions and full records →](docs/competitor-memory-observations.md)

## Download

[Download PurePin →](https://github.com/easyrev/PurePin/releases)

**macOS 26+** · Apple Silicon / Universal (Apple Silicon + Intel)

## Installation and first launch

Open the DMG, drag PurePin to Applications, and open it from there. For a release marked **not notarized**, macOS may block the first launch. After attempting to open PurePin, go to **System Settings → Privacy & Security**, find the message about PurePin near the bottom, and choose **Open Anyway**. Confirm the system prompt. See [Apple's instructions](https://support.apple.com/102445).

On first launch, PurePin shows screen capture setup if permission is missing. Choose **Allow Screen Recording** and finish the macOS prompt. If needed, **Open System Settings** takes you to **Privacy & Security → Screen & System Audio Recording**. Enable PurePin; quit and reopen it if macOS asks. Once setup says you're ready, choose **Done**, then press **F1** yourself. Setup does not start or queue a screenshot.

PurePin uses this permission for still screenshots. It does not record audio or require Accessibility, Camera, or Microphone access.

## Shortcuts

| Action | Default shortcut |
| :--- | :--- |
| Start a capture | <kbd>F1</kbd> |
| Edit an image from the clipboard | <kbd>⌥</kbd> + <kbd>F1</kbd> |
| Pin an image from the clipboard | <kbd>F3</kbd> |
| Hide / restore all pins | <kbd>⇧</kbd> + <kbd>F3</kbd> |
| Copy the capture and finish editing | <kbd>Return</kbd> or <kbd>⌘</kbd> + <kbd>C</kbd> |
| Pin the current capture | <kbd>⌘</kbd> + <kbd>T</kbd> |
| Save a PNG | <kbd>⌘</kbd> + <kbd>S</kbd> |
| Undo / redo | <kbd>⌘</kbd> + <kbd>Z</kbd> / <kbd>⇧</kbd> + <kbd>⌘</kbd> + <kbd>Z</kbd> |

If macOS uses the function keys for system controls, hold <kbd>fn</kbd> / Globe or choose another shortcut in Settings.

To annotate an existing image, copy the image itself and choose **Edit Clipboard Image** from the menu bar. Zooming and panning only change the view; copying, saving, and pinning preserve the original pixel dimensions unless you crop the image. Cropping changes the output area and dimensions. Clipboard editing does not require screen recording permission.

Drag a pin to move it, scroll to resize it, and double-click to close it. Right-click to copy, save, or restore its original size.

---

<div align="center">

[Download](#download) · [Privacy](PRIVACY.md) · [Help & feedback](SUPPORT.md)

<sub>PurePin is currently closed source. This repository hosts downloads and feedback. Copyright © 2026 PurePin.</sub>

</div>
