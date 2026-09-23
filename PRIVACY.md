# Privacy and storage

English · [简体中文](PRIVACY.zh-CN.md)

PurePin captures, annotates, and pins images on your Mac. It has no analytics SDK, accounts, upload service, or automatic crash reporting. Its sandbox does not request network access. Clicking a help link opens GitHub in your browser; the browser and GitHub handle data under their own privacy policies.

## What gets saved

- **Preferences:** shortcuts, cursor inclusion, and annotation styles, stored in macOS preferences.
- **Images you save:** written to the location you select in the Save dialog. PurePin does not delete these files for you.
- **Content you copy:** captures, pinned images, and Support Info replace the current system clipboard. Universal Clipboard or other clipboard apps may process this content.
- **System logs and crash reports:** PurePin records a small number of operation events and errors through macOS unified logging. macOS may also create crash reports. The system manages their storage and retention. PurePin does not maintain its own growing log file; system logging can still use disk space.

PurePin does not create a screenshot library, persist pins, cache screenshots in its own disk directory, or scan for crash reports. It does not write screen pixels, annotation text, or clipboard contents to application logs. Error descriptions that may contain file paths use private log fields.

This describes the standard release. Separate maintainer benchmark builds write measurements when a benchmark is explicitly run; those entry points are excluded from the standard Release app.

## Feedback is optional

**Menu bar → Help & Feedback… → Copy Support Info** copies only the app version, build number, short source revision, build state, macOS version, and process architecture. It does not read existing clipboard contents, copy screenshots, collect logs, device serial numbers, usernames, or paths, or send anything automatically.

Before sharing a system crash report, inspect it in Console for personal paths, filenames, and other private information. See [Help & feedback](SUPPORT.md).

## Permissions

- Capturing the screen requires Screen & System Audio Recording permission. PurePin uses still-image capture APIs and does not record audio.
- Saving uses the destination you choose in the system Save dialog.
- Launch at Login is optional and off by default. macOS manages the login item.
- Accessibility, Camera, and Microphone permissions are not required.

## Uninstalling

Turn off Launch at Login, quit PurePin, and remove the app. Keep or delete your saved images as you choose. System preferences, unified logs, and system crash reports may remain. PurePin does not run a cleanup task after removal.
