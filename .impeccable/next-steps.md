# Home page: next round (from session of 2026-11-18)

Latest critique: `.impeccable/critique/2026-11-18T16-35-24Z__index-md.md` (15/24, detector 0 findings).

## Decisions already made by Iván
- Fix the narrow column AND the papers section in one pass.
- Identity: **bolder**, built around his X-ray survey work (detections, grids, selection), still calm and readable. Show the direction before building it.
- Scope: all five priority issues.
- Keep: daily quote (now English, label "A thought for today"), dark mode, **justified bio text** (deliberate), all six timeline entries, the closing contact panel.
- Ask before changing his copy (first bio sentence, one-line paper findings).
- ADS metrics GitHub Action: not now. The home page shows totals only if `_data/ads_metrics.yml` exists.
- Facts come from the new CV: `CV/v_munoz_rodriguez.pdf` (already copied to `assets/cv/cv_munoz_rodriguez.pdf`).
- **Correction (2026-11-18):** the two industry internships on the web CV (OmegaLambdaTec 2022, Prewarp 2021, `cv.md:91–112`) are real and stay. Open question: should the PDF list them too?

## Run in order
1. `/impeccable layout index.md`: frame ~1100px with text kept at reading width; bigger hero photo column; "What I do" in one row of four; timeline dates in a margin with larger photos; one primary hero link (44px target); papers with first-author line, titles styled as links, ADS/DOI links ≥14px.
2. `/impeccable clarify index.md`: GitHub in hero links; equal weight for the ML/data item; "data scientist" in the JSON-LD jobTitle (`_includes/head.html:37`); optional copy rewrites, which need approval.
3. `/impeccable bolder index.md`: survey-inspired identity; timeline photos in colour; identity mark top-left (the home page currently hides the header name via `.site-logo--home`).
4. `/impeccable polish index.md`: section labels distinct from links; subtitle dangling "·"; footer floating on tall screens; drop unused Inter 500 if nothing uses it.

## Checking the page
Jekyll is usually already running at http://localhost:4000/. There is no browser tool, so take headless Chrome screenshots:
`"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --hide-scrollbars --window-size=1440,3000 --screenshot=<scratchpad>/x.png http://localhost:4000/`
(dark mode by default; add `--blink-settings=preferredColorScheme=1` for light; the minimum usable width is about 500px, so use 600px for the narrow layout).

## Status (2026-11-18, later)
Steps 1–4 done. Also done after step 4: dropped unused Source Serif 700; the quote's light bulb is now a luminance mask (`assets/images/light_bulb_mask.png`) drawn in `--color-text-secondary`, so it no longer inverts in dark mode. The original `light_bulb.png` is no longer referenced. The source is only 85px, so a sharper bulb would need a bigger or vector original.

## Next round (from critique 2026-11-18T18-38-44Z, 21/32)
Iván chose: all five issues. Daily quote becomes a **margin note in the hero** (small handwritten note under the photo on desktop; below the hero links on mobile).
1. `/impeccable clarify index.md`: industry evidence on home (submitted ML X-ray source classification paper, LinkedIn in hero links, optionally one internship line); proposals need his approval.
2. `/impeccable layout index.md`: quote into the hero as margin note; "What I do" 2x2 above 640px.
3. `/impeccable harden index.md`: timeline alt text (describe the photo or alt=""), hide thumbnails ≤640px, footer links 44px + new-tab notes.
4. `/impeccable polish index.md`.

### Done (2026-11-18, evening)
All four steps ran. Hero links: CV, GitHub, LinkedIn, Email (Publications stays in nav). AI card links the ML paper, now **accepted in A&A** (publications.md venue updated; add DOI/ADS when available). Quote is a margin note under the photo (≤900px: after the hero links). "What I do" is 2x2. Timeline photos alt="" and hidden ≤640px. Footer links 44px + new-tab notes.
Open: Iván will upload a separate industry CV (where to link it is not decided). Detector flags Inter at 52% of text (overused-font): a typeface decision for Iván, not changed.
- Phone version: below 640px the photo sits top right in its detection circle on a strip of the X-ray field (faded before the name). The hero is `isolation: isolate` with the backdrop at `z-index: -1`, because grid `order` changes paint order.
- `404.html`: "No source detected here" with an empty detection region. `jekyll serve` shows WEBrick's own 404 for missing paths; GitHub Pages serves this page. Preview it at /404.html.
