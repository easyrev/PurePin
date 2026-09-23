#!/usr/bin/env python3
"""Render the published memory figure from its checked-in measurements.

Requires matplotlib==3.10.8. Run from any working directory:
    python script/render_memory_report.py
    python script/render_memory_report.py --png /tmp/purepin-memory.png
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import xml.etree.ElementTree as ET

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs/data/memory-2026-09-21.json"
OUTPUT = ROOT / "assets/memory-report.svg"
COLORS = {"cancel": "#2864E8", "copy": "#088D96", "vector": "#424D5B"}
PAPER = "#FAFAF7"
INK = "#242C35"
MUTED = "#64707D"


def render(png: Path | None = None) -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    expected_cycles = list(range(1, data["protocol"]["cycles_per_session"] + 1))
    for scenario in data["scenarios"]:
        if [item["cycle"] for item in scenario["cycles"]] != expected_cycles:
            raise ValueError(f"Incomplete cycle sequence: {scenario['id']}")
    if data["metric"]["unit"] != "MiB" or data["plot"]["smoothing"]:
        raise ValueError("Figure expects unsmoothed MiB measurements")

    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "svg.fonttype": "path",
        "svg.hashsalt": "purepin-memory-2026-09-21",
        "axes.unicode_minus": False,
    })
    fig = plt.figure(figsize=(14.4, 8.2), dpi=100, facecolor=PAPER)
    fig.text(0.066, 0.915, "Memory, measured.", color=INK, fontsize=31, weight="bold")
    fig.text(0.068, 0.863, "20 consecutive captures · memory after each close", color=MUTED, fontsize=16)
    fig.text(0.967, 0.925, "PUREPIN v0.9.0", color=MUTED, fontsize=10.5, ha="right")

    ax = fig.add_axes((0.076, 0.355, 0.89, 0.415), facecolor=PAPER)
    for scenario in data["scenarios"]:
        samples = scenario["cycles"]
        ax.plot(
            [item["cycle"] for item in samples],
            [item["last_closed_mib"] for item in samples],
            color=COLORS[scenario["id"]], label=scenario["label"],
            linewidth=2.8, marker="o", markersize=4.8,
            markeredgewidth=0.7, markeredgecolor=PAPER,
            solid_capstyle="round", zorder=3,
        )
    ax.set_xlim(0.6, 20.4)
    ax.set_ylim(0, 45)
    ax.set_xticks([1, 5, 10, 15, 20])
    ax.set_yticks([0, 10, 20, 30, 40])
    ax.set_xlabel("Capture cycle", fontsize=13, color=MUTED, labelpad=11)
    ax.set_ylabel("Physical footprint · MiB", fontsize=13, color=MUTED, labelpad=15)
    ax.tick_params(axis="both", length=0, labelsize=12.5, colors=MUTED, pad=9)
    ax.set_axisbelow(True)
    ax.grid(axis="y", color="#E1E5E7", linewidth=0.8)
    for side in ["top", "right", "left"]:
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color("#CED4D8")
    ax.legend(
        loc="lower left", bbox_to_anchor=(-0.006, 1.026), ncol=3,
        frameon=False, fontsize=13.5, labelcolor=INK,
        handlelength=2.0, columnspacing=2.8, borderaxespad=0,
    )

    fig.text(0.068, 0.233, "FINAL IDLE MEDIAN", color=MUTED, fontsize=10.5, weight="bold")
    fig.text(0.967, 0.233, "Final 20 seconds, after all captures", color=MUTED, fontsize=11, ha="right")
    for x, scenario in zip((0.068, 0.377, 0.688), data["scenarios"], strict=True):
        color = COLORS[scenario["id"]]
        fig.text(x, 0.19, scenario["label"], color=color, fontsize=13.5, weight="bold")
        fig.text(x, 0.137, f"{scenario['final_idle_median_mib']:.2f} MiB", color=INK, fontsize=25)
        fig.text(x, 0.094, f"Visible sampled peak: {scenario['visible_sampled_max_mib']:.2f} MiB", color=MUTED, fontsize=10.5)
    fig.text(
        0.068, 0.033,
        "2026-09-21 · M1 Pro / 32 GiB · macOS 27.0 · 3456 × 2234 px · PurePin v0.9.0",
        color=MUTED, fontsize=11,
    )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, format="svg", facecolor=PAPER, metadata={
        "Title": "Memory, measured. — PurePin Release benchmark, 2026-09-21",
        "Description": "Three separate 20-cycle sessions. Each plotted point is the final physical footprint sample after that capture closes. Final idle medians and visible sampled peaks are shown separately. This is an instrumented Release build, not a distribution-binary benchmark or product ranking.",
        "Creator": "PurePin / Matplotlib",
        "Date": data["recorded_local_date"],
    })
    # Keep Matplotlib's vector paths and coordinate system; use a natural README size.
    ET.register_namespace("", "http://www.w3.org/2000/svg")
    tree = ET.parse(OUTPUT)
    root = tree.getroot()
    root.set("width", "1440")
    root.set("height", "820")
    root.set("role", "img")
    title = ET.Element("{http://www.w3.org/2000/svg}title")
    title.text = "Memory, measured. — 20 capture cycles, Release benchmark"
    root.insert(0, title)
    tree.write(OUTPUT, encoding="unicode", xml_declaration=False)
    OUTPUT.write_text("\n".join(line.rstrip() for line in OUTPUT.read_text().splitlines()) + "\n")
    if png:
        png.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(png, dpi=100, facecolor=PAPER)
    plt.close(fig)
    print(OUTPUT)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--png", type=Path, help="Optional local preview; SVG is always generated")
    render(parser.parse_args().png)
