# Home page: next round (from session of 2026-11-18)

Latest critique: `.impeccable/critique/2026-11-18T16-35-24Z__index-md.md` (15/24, detector 0 findings).

## Decisions already made by Iván
- Fix the narrow column AND the papers section in one pass.
- Identity: **bolder**, built around his X-ray survey work (detections, grids, selection), still calm and readable. Show the direction before building it.
- Scope: all five priority issues.
- Keep: daily quote (now English, label "A thought for today"), dark mode, **justified bio text** (deliberate), all six timeline entries, the closing contact panel.
- Ask before changing his copy (first bio sentence, one-line paper findings).
- ADS metrics GitHub Action: not now. The home page shows totals only if `_data/ads_metrics.yml` exists.
- Facts come from the new CV: `CV/v_munoz_rodriguez.pdf` (already copied to `assets/cv/cv_munoz_rodriguez.pdf`). It has no industry internship; don't add one.

## Run in order
1. `/impeccable layout index.md`: frame ~1100px with text kept at reading width; bigger hero photo column; "What I do" in one row of four; timeline dates in a margin with larger photos; one primary hero link (44px target); papers with first-author line, titles styled as links, ADS/DOI links ≥14px.
2. `/impeccable clarify index.md`: GitHub in hero links; equal weight for the ML/data item; "data scientist" in the JSON-LD jobTitle (`_includes/head.html:37`); optional copy rewrites, which need approval.
3. `/impeccable bolder index.md`: survey-inspired identity; timeline photos in colour; identity mark top-left (the home page currently hides the header name via `.site-logo--home`).
4. `/impeccable polish index.md`: section labels distinct from links; subtitle dangling "·"; footer floating on tall screens; drop unused Inter 500 if nothing uses it.

## Checking the page
Jekyll is usually already running at http://localhost:4000/. There is no browser tool, so take headless Chrome screenshots:
`"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --hide-scrollbars --window-size=1440,3000 --screenshot=<scratchpad>/x.png http://localhost:4000/`
(dark mode by default; add `--blink-settings=preferredColorScheme=1` for light; the minimum usable width is about 500px, so use 600px for the narrow layout).
