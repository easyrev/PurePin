#!/usr/bin/env python3
"""Render historical Pin observations; requires matplotlib==3.10.8.

python script/render_competitor_memory.py --png /tmp/purepin-comparison.png
"""

import argparse
import json
from pathlib import Path
import xml.etree.ElementTree as ET

from render_memory_report import INK, MUTED, PAPER, ROOT, plt


def render(png=None):
    data = json.loads((ROOT / "docs/data/competitor-memory-2026-09-12.json").read_text())
    samples = {item["sample"]: item for item in data["samples"]}
    selected = [samples[key] for key in (
        "purepin-manual-pin", "shottr-fixture-pin", "snipaste-import-attempt",
    )]
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "svg.fonttype": "path",
        "svg.hashsalt": "purepin-pin-observations-2026-09-12",
    })
    fig = plt.figure(figsize=(12, 5.8), dpi=100, facecolor=PAPER)
    fig.text(.055, .895, "Memory with a pinned image", fontsize=26, weight="bold", color=INK)
    fig.text(.057, .83, "4096 × 4096 px · One observation per app", fontsize=13, color=MUTED)
    ax = fig.add_axes((.23, .28, .70, .47), facecolor=PAPER)
    values = [item["dirty_bytes"] / 1048576 for item in selected]
    ax.barh(range(3), values, height=.42, color=["#2864E8", "#088D96", "#424D5B"], zorder=3)
    ax.set_ylim(2.6, -.6)
    ax.set_xlim(0, 820)
    ax.set_xticks([0, 200, 400, 600, 800])
    ax.set_yticks([])
    ax.tick_params(axis="x", length=0, labelsize=11, colors=MUTED, pad=9)
    ax.set_axisbelow(True)
    ax.grid(axis="x", color="#E1E5E7", linewidth=.8)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.axvline(0, color="#CED4D8", linewidth=1)
    for y, (sample, value) in enumerate(zip(selected, values)):
        ax.text(-.245, y-.06, sample["app"], transform=ax.get_yaxis_transform(),
                fontsize=16, weight="bold", color=INK, va="center", clip_on=False)
        if sample["app"] == "PurePin":
            version = "v0.9.0"
        else:
            version = sample["version"]
            if sample["build"] != version:
                version += f" · build {sample['build']}"
        ax.text(-.245, y+.21, version, transform=ax.get_yaxis_transform(),
                fontsize=10.5, color=MUTED, va="center", clip_on=False)
        ax.text(value+12, y, f"{value:.2f}", va="center", fontsize=14, color=INK)
    fig.text(.93, .19, "Dirty memory · MiB", ha="right", fontsize=12, color=MUTED)
    fig.text(.057, .105, "Exploratory records: display sizes, import paths, and prior app states differ.", fontsize=12, color=MUTED)
    fig.text(.057, .057, "macOS 26.5.2 · footprint Dirty total · Test conditions and all samples linked below", fontsize=10.5, color=MUTED)
    output = ROOT / "assets/competitor-memory.svg"
    fig.savefig(output, format="svg", facecolor=PAPER, metadata={
        "Title": "Pin memory observations — PurePin, Shottr, Snipaste",
        "Description": "Exploratory single observations with unmatched display sizes, import paths and prior app states. Snipaste's imported test image was visually confirmed after sampling. Not a controlled performance ranking.",
        "Date": data["date"],
    })
    ET.register_namespace("", "http://www.w3.org/2000/svg")
    tree = ET.parse(output)
    root = tree.getroot()
    root.set("width", "1200")
    root.set("height", "580")
    root.set("role", "img")
    title = ET.Element("{http://www.w3.org/2000/svg}title")
    title.text = "Exploratory Pin memory: PurePin 122.19, Shottr 200.09, Snipaste 697.58 MiB; conditions differ."
    root.insert(0, title)
    tree.write(output, encoding="unicode")
    output.write_text("\n".join(line.rstrip() for line in output.read_text().splitlines()) + "\n")
    if png:
        fig.savefig(png, dpi=100, facecolor=PAPER)
    plt.close(fig)
    print(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--png", type=Path)
    render(parser.parse_args().png)
