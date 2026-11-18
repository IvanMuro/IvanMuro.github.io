"""Generate the mock X-ray observation behind the home page.

Writes two files:
  assets/images/xray-sky.svg   the sky, 2600 x 2000 px, in 5px pixels
  _sass/_source-marks.scss     the pixel sources used as bullets on every page

The pointing is centred on the main cluster at CX, CY, which the home page
photo covers. Around it: background counts, point and extended sources with
their detection circles, vignetting (fewer and fainter counts outward) and
EPIC-pn style chips with gaps between them.

    python3 _scripts/make_sky.py
"""
import math, random

PX = 5                       # screen pixels per sky pixel
W, H = 2600 // PX, 2000 // PX
CX, CY = 720 // PX, 260 // PX  # main cluster (720px, 260px), as in the CSS
U = 10 / PX                  # sizes below were tuned in 10px units
LEVELS = [0.1, 0.24, 0.38, 0.56, 0.78]
OUT = 'assets/images/xray-sky.svg'
MARKS = '_sass/_source-marks.scss'
rng = random.Random(4112)
grid = {}

def put(x, y, level):
    if 0 <= x < W and 0 <= y < H:
        grid[(x, y)] = max(grid.get((x, y), 0), level)

# Vignetting: sensitivity falls off away from the aim point
def vignette(x, y):
    return math.exp(-(math.hypot(x - CX, y - CY) / (120 * U)) ** 2)

# 1. The main cluster: a beta-model surface brightness, bright core under the face
RC = 7 * U                     # core radius: broad, so the halo shows round the face
for y in range(int(CY - 28 * U), int(CY + 28 * U)):
    for x in range(int(CX - 28 * U), int(CX + 28 * U)):
        r = math.hypot(x + .5 - CX, y + .5 - CY)
        sb = (1 + (r / RC) ** 2) ** -1.5
        if rng.random() < min(1, sb * 5 + 0.12):
            put(x, y, max(0, min(4, round(6 * sb ** 0.4 + rng.uniform(-1, 0.3)))))

# 2. Background: mostly faint single counts
for y in range(H):
    for x in range(W):
        r = rng.random() / (0.45 + 0.55 * vignette(x, y))
        if r < 0.002: put(x, y, 2)
        elif r < 0.015: put(x, y, 1)
        elif r < 0.06: put(x, y, 0)

# 3. Sources, kept clear of the cluster and of each other
def profile(size, peak, rand):
    """Pixels of one source as {(dx, dy): level}: bright core, counts falling off."""
    px = {}
    reach = int(size * 2)
    for dy in range(-reach, reach + 1):
        for dx in range(-reach, reach + 1):
            d = math.hypot(dx, dy) / size
            p = math.exp(-d * d * 1.3)
            if rand.random() < p * 1.15:
                px[(dx, dy)] = max(0, min(4, round(peak * p + rand.uniform(-.6, .4))))
    return px

circles = []
def free(x, y, r):
    if math.hypot(x - CX, y - CY) < 22 * U + r: return False
    return all(math.hypot(x - a, y - b) > r + c + 1.5 * U for a, b, c in circles)

tries = 0
while len(circles) < 120 and tries < 40000:
    tries += 1
    x, y = rng.uniform(3, W - 3), rng.uniform(3, H - 3)
    if rng.random() > 0.25 + 0.75 * vignette(x, y): continue   # fewer detections outward
    kind = rng.random()
    if kind < 0.07:   size, peak, r = 3 * U, 3, rng.uniform(4.6, 5.8) * U   # extended
    elif kind < 0.40: size, peak, r = 2 * U, 4, rng.uniform(2.9, 3.4) * U   # bright point
    else:             size, peak, r = 1.2 * U, 3, rng.uniform(2.2, 2.6) * U  # faint point
    if not free(x, y, r): continue
    circles.append((x, y, r))
    peak *= 0.45 + 0.55 * vignette(x, y)
    for (dx, dy), lvl in profile(size, peak, rng).items():
        put(int(x) + dx, int(y) + dy, lvl)

# 4. Chip gaps, as on the EPIC-pn camera: a 2 x 6 array of tall CCDs rotated
# by the roll angle, no counts in the gaps. The aim point falls inside a chip.
ROLL = math.radians(12)
OX, OY = CX + 10 * U, CY + 25 * U
CHIP_W, CHIP_H, GAP = 44 * U, 130 * U, 0.8
def on_gap(x, y):
    dx, dy = x + .5 - OX, y + .5 - OY
    u = dx * math.cos(ROLL) + dy * math.sin(ROLL)
    v = -dx * math.sin(ROLL) + dy * math.cos(ROLL)
    return (abs(u - CHIP_W * round(u / CHIP_W)) < GAP
            or abs(v - CHIP_H * round(v / CHIP_H)) < GAP)
for cell in [c for c in grid if on_gap(*c)]:
    del grid[cell]

# 5. Write the sky. Each level is one stroked path, one 1px-tall line per run
# of pixels, moving relatively along the row: far smaller than a rect per pixel
def paths(cells, w, h, q='"'):
    out = []
    for lvl, op in enumerate(LEVELS):
        d = []
        for y in range(h):
            x, end = 0, None
            while x < w:
                if cells.get((x, y)) == lvl:
                    x0 = x
                    while x < w and cells.get((x, y)) == lvl: x += 1
                    d.append(f'M{x0} {y}.5h{x - x0}' if end is None else f'm{x0 - end} 0h{x - x0}')
                    end = x
                else:
                    x += 1
        if d:
            out.append(f'<path opacity={q}{op}{q} d={q}{"".join(d)}{q}/>')
    return out

svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W * PX}" height="{H * PX}" shape-rendering="crispEdges">']
svg.append('<g fill="none" stroke="#000" stroke-width="1">')
svg += paths(grid, W, H)
svg.append('</g>')
# Each chip carries a faint even background, so its gaps read as clean lines
svg.append(f'<g opacity="0.06" transform="translate({OX:g} {OY:g}) rotate({math.degrees(ROLL):g})">')
for i in range(-6, 6):
    for j in range(-3, 3):
        svg.append(f'<rect x="{i * CHIP_W + GAP:g}" y="{j * CHIP_H + GAP:g}" width="{CHIP_W - 2 * GAP:g}" height="{CHIP_H - 2 * GAP:g}"/>')
svg.append('</g>')
svg.append(f'<g fill="none" stroke="#000" stroke-width="{0.12 * U:g}" shape-rendering="geometricPrecision">')
for x, y, r in circles:
    svg.append(f'<circle cx="{x + .5:.2f}" cy="{y + .5:.2f}" r="{r:.2f}" opacity="{0.3 + 0.6 * vignette(x, y):.2f}"/>')
svg.append('</g></svg>')
open(OUT, 'w').write('\n'.join(svg) + '\n')

# 6. Bullet sources: bright point sources on the same 5px grid, each different
N, SIDE = 6, 7               # variants; 7 x 7 sky pixels = 35px
marks = ['// Generated by _scripts/make_sky.py: bullet sources, drawn like the',
         '// sky\'s own sources on its 5px grid. Do not edit by hand.',
         '// --mark-1 ... --mark-N are the shapes; `@include varied-marks` on list',
         '// items gives each item its own (read through --mark).', '', ':root {']
mrng = random.Random(860744)
for k in range(N):
    while True:
        px = profile(1.5, 4, mrng)
        px = {(dx + 3, dy + 3): l for (dx, dy), l in px.items() if abs(dx) <= 3 and abs(dy) <= 3}
        px[(3, 3)] = 4                                    # always a bright centre
        if 9 <= len(px) <= 22: break
    body = ''.join(paths(px, SIDE, SIDE, q="'"))
    uri = (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {SIDE} {SIDE}' "
           f"shape-rendering='crispEdges'><g fill='none' stroke='%23000'>{body}</g></svg>").replace('<', '%3C').replace('>', '%3E')
    marks.append(f'  --mark-{k + 1}: url("data:image/svg+xml,{uri}");')
marks += ['}', '', '@mixin varied-marks {']
marks += [f'  &:nth-child({N}n + {k + 1}) {{ --mark: var(--mark-{k + 1}); }}' for k in range(N)]
marks.append('}')
open(MARKS, 'w').write('\n'.join(marks) + '\n')

print(len(circles), 'sources,', len(grid), 'sky pixels,', sum(map(len, svg)) // 1024, 'KB')
