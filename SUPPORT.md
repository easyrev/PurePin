# Help & feedback

English · [简体中文](SUPPORT.zh-CN.md)

PurePin focuses on capture, basic annotation, and pinning. Report bugs or describe problems with those tasks in [Issues](https://github.com/easyrev/PurePin/issues).

## Reporting a bug

Include steps to reproduce, what you expected, what happened, and the version details from **Help & Feedback… → Copy Support Info**. Copying this information replaces your clipboard. You decide whether to paste it into an issue.

For display problems, include the number of monitors, resolution, and scaling settings; serial numbers are unnecessary. Use example screenshots without private work in them. Issues are public: do not include passwords, tokens, private documents, customer data, or unchecked logs.

## Crash reports

PurePin has no additional crash collection SDK and does not upload reports automatically. Open **macOS Console → Crash Reports** and look for PurePin at the relevant time. Some exits do not generate a report, and macOS may have removed older reports.

Start with reproduction steps, the app version, and the crash time. If details are needed, check the report for private information first. You can initially share just the Exception Type, Termination Reason, and relevant crashed-thread section. Keep the original report for investigation, but do not upload an unchecked `.ips` file. If a complete report is needed, arrange a suitable way to share it with the maintainer.

## Common questions

- **Where is the app window?** PurePin lives in the menu bar. Opening it again shows Settings.
- **F1 does nothing.** Try `fn` / Globe + F1, or change the shortcut in Settings.
- **macOS blocks the first launch.** For a release marked not notarized, attempt to open it, then go to System Settings → Privacy & Security and choose Open Anyway beside the PurePin message. See [Apple's instructions](https://support.apple.com/102445).
- **Capture opens setup instead.** Finish screen recording setup, choose Done, then press F1 again. Setup never resumes the previous capture. If macOS asks you to quit and reopen PurePin, follow that prompt first.
- **How do I annotate an existing image?** Copy the image itself, then choose **Edit Clipboard Image** from the menu bar or press `⌥F1`. Copying a file in Finder or copying an image URL does not put image bytes on the clipboard. Zooming and panning only change the view. Copying, saving, and pinning preserve the original pixel dimensions unless you crop the image, which changes the output area and dimensions.
- **Pins disappear after quitting.** Pins are temporary references. Save images you want to keep.
- **I need to hide private information.** Blur and mosaic effects may leave information that can be inferred. Inspect the exported image before sharing; cover sensitive areas with an opaque shape or remove them when needed.

Feature requests should describe a specific capture, annotation, or pinning task. OCR, AI, GIF recording, advanced image editing, and cloud sync are outside the current scope.
