"""Generate a mock pixelated X-ray counts image as an SVG include.

Usage (from the repository root):
    python3 scripts/make_xray_field.py > _includes/xray-field.svg

Change the random seed or the source list below for a different field.

A rectangular field (W x H pixels, drawn at 10 CSS px per pixel) with
Poisson background, a bright beta-model cluster at (CX, CY) that sits
behind the hero photo, a faint second cluster, and scattered point
sources, with a detection-region overlay. Counts are quantised into a few opacity levels, one <path> per
level, filled with currentColor so the site theme sets the colour.

The CSS in _sass/_layout.scss assumes CX is 18 pixels from the right edge
and CY is the vertical middle; keep them in sync if you change W, H, CX, CY.
"""
import math
import random
import sys

W, H = 120, 90
CX, CY = W - 18, H / 2
random.seed(11)


def poisson(lam):
    if lam <= 0:
        return 0
    L, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= random.random()
        if p <= L:
            return k
        k += 1


# Point sources: random, but none hidden under the photo (radius ~12 px)
sources = []
while len(sources) < 32:
    x, y = random.uniform(1, W - 1), random.uniform(1, H - 1)
    if (x - CX) ** 2 + (y - CY) ** 2 < 15 ** 2:
        continue
    sources.append((x, y, random.choice([3, 4, 5, 6, 8, 11, 15])))

# A few brighter sources in the open field around the photo, where the
# detection circles are drawn (the rest of the field sits under the text)
added = 0
while added < 10:
    x, y = random.uniform(84, W - 2), random.uniform(3, H - 3)
    if (x - CX) ** 2 + (y - CY) ** 2 < 17 ** 2:
        continue
    sources.append((x, y, random.choice([5, 6, 8, 11])))
    added += 1


def beta(x, y, cx, cy, amp, rc):
    return amp * (1 + ((x - cx) ** 2 + (y - cy) ** 2) / rc ** 2) ** -1.5


def rate(x, y):
    lam = 0.05                                   # background
    lam += beta(x, y, CX, CY, 16, 5)             # main cluster, behind photo
    lam += beta(x, y, 34, 26, 2.2, 3.5)          # a fainter, distant cluster
    for sx, sy, a in sources:                    # PSF, sigma ~0.9 px
        lam += 1.8 * a * math.exp(-((x - sx) ** 2 + (y - sy) ** 2) / (2 * 0.9 ** 2))
    return lam


levels = [(1, 0.10), (2, 0.24), (4, 0.38), (7, 0.56), (11, 0.78)]
paths = {op: [] for _, op in levels}
for y in range(H):
    for x in range(W):
        n = poisson(rate(x + 0.5, y + 0.5))
        op = None
        for thr, o in levels:
            if n >= thr:
                op = o
        if op:
            paths[op].append(f"M{x} {y}h1v1h-1z")

out = [
    f'<svg class="hero-field" viewBox="0 0 {W} {H}" width="{W * 10}" height="{H * 10}" '
    'shape-rendering="crispEdges" fill="currentColor" aria-hidden="true" focusable="false">'
]
for _, op in levels:
    if paths[op]:
        out.append(f'<path opacity="{op}" d="{"".join(paths[op])}"/>')

# Detection overlay, like ds9 regions on a photon image: thin circles around
# the sources bright enough to be "detected" (faint ones stay undetected),
# plus extent circles for the two clusters. 0.12 user units = 1.2 CSS px.
# (The main cluster's circle is drawn in CSS around the photo so it scales.)
regions = [(34, 26, 5.5)]
regions += [(x, y, 1.6 + 0.12 * a) for x, y, a in sources if a >= 5]
out.append("</svg>")
# Regions go in their own layer so CSS can fade them out under the text
out.append(
    f'<svg class="hero-field hero-regions" viewBox="0 0 {W} {H}" width="{W * 10}" '
    f'height="{H * 10}" fill="none" stroke="currentColor" stroke-width="0.12" '
    'aria-hidden="true" focusable="false">'
)
for x, y, r in regions:
    out.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}"/>')
out.append("</svg>")
sys.stdout.write("\n".join(out) + "\n")
