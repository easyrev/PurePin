# Pinning a large image: PurePin, Shottr, Snipaste

English · [简体中文](competitor-memory-observations.zh-CN.md)

These records come from a local investigation on September 12, 2026. They have not been rerun. Display sizes, prior process use, and import paths were not fully aligned, so they cannot establish product rankings or percentage savings.

## Setup

- macOS 26.5.2 (25F84); ARM64 standard release builds; one process session per app.
- PurePin v0.9.0; Shottr 1.9.1 build 128; Snipaste 2.10.8.
- A 4096 × 4096 px opaque RGBA color-tile image: 64 MiB of raw pixels, 1,418,239 bytes as PNG. SHA-256: `885602152f4da18b4b25a502e733d784a122f62c6eb7846ef55991aef1964c6c`.
- Metric: macOS `footprint` total Dirty memory. MiB = 1,048,576 bytes. Dirty includes Swapped; Wired is a subset. Do not add these columns together. This is not RSS or whole-system RAM cost.
- Sampling checked the PID and executable identity before and after each observation, retaining `footprint` and `vmmap` records. A successful sampling command does not establish successful UI interaction.

## Observed phases

| App and phase | Dirty memory | Verification |
| :--- | ---: | :--- |
| PurePin, before pinning | 29.44 MiB | Previously used resident process; no test pin yet |
| PurePin, pin visible | 122.19 MiB | User confirmed pinning with the physical shortcut |
| PurePin, after confirmed close | 58.67 MiB | User confirmed closure; exact close time unknown |
| PurePin, about 102 seconds later | 58.69 MiB | Same process, no intervening actions |
| Shottr, before import | 101.91 MiB | Previously used process with an earlier screenshot |
| Shottr, editing | 199.92 MiB | Test image visible |
| Shottr, pin visible | 200.09 MiB | Test image visible; UI showed 50% |
| Shottr, after Close All command | 198.83 MiB | Closure unverified; not a completed-close result |
| Snipaste, before import | 39.30 MiB | Fresh process; persisted pin state not fully checked |
| Snipaste, after import | 697.58 MiB | Window unverified at sampling; test image visually confirmed later |
| Snipaste, after close attempt | 699.44 MiB | Closure unverified; not a completed-close result |
| Snipaste, later observation | 699.47 MiB | No further imports; window state still unverified |

PurePin's visible ImageIO Dirty allocation was 64 MiB. That category disappeared after confirmed closure, supporting release of the original image storage; approximately 17.06 MiB of IOSurface remained. Snipaste's post-import sample included about 524.09 MiB of IOSurface Dirty. These categories describe the observed storage, not proof of a leak or framework defect.

## Limits

PurePin fitted the pin to the available screen area, Shottr showed 50%, and Snipaste's display size was not matched. Graphics-buffer costs can vary with display size. PurePin and Shottr had already been used, so subtracting their starting values would not produce comparable per-image costs.

Shottr and Snipaste used the original PNG. PurePin used a PNG re-encoded by Shottr's Copy Image command: still 4096 × 4096, but decoded pixel equality was not checked. The compressible tile image does not represent photos, noise, or ordinary screenshots; its pixel count also exceeded the display's screenshot size.

Shottr and Snipaste closure was not reliably verified. Their later samples cannot be labeled memory retained after a confirmed close. Snipaste also distinguishes hiding, restorable closure, and destruction; these retained-state features carry their own costs. See [Snipaste's instructions](https://github.com/Snipaste/feedback/wiki/Getting-Started).

These older versions and system cannot be combined with the [September 21 PurePin capture test](memory-report.md) as one comparative benchmark. That test used an instrumented Release, a different task, and a different measurement interface. This investigation did not measure latency, CPU, energy, or overall performance.

## Data and chart

The [bar chart](../assets/competitor-memory.svg) starts at zero and identifies each tested version or build. With `matplotlib==3.10.8` installed, run `python script/render_competitor_memory.py` to regenerate it from the JSON. It does not run apps or collect new samples.

[Sanitized sampling summary](data/competitor-memory-2026-09-12.json) preserves all 14 observations: timestamps, versions, byte counts, categories, and contemporaneous verification notes. This includes the unsuccessful Pin trigger and unverified close attempts. Later confirmation of Snipaste's image is recorded separately without rewriting the original status. The summary excludes screenshots, user paths, and raw heap dumps; it does not replace the complete local evidence.

[Back to PurePin](../README.md)
