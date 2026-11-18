# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Two primary audiences, weighted equally; neither should feel second-class:

- **Academic hiring**: search committees and PIs evaluating Iván for postdoc, fellowship or faculty roles. They scan for research focus, first-author output, funding and collaborations.
- **Industry hiring**: data-science / ML hiring managers evaluating a researcher moving toward industry. They look for applied data, modelling, Python and the industry experience listed on the CV.

Secondary: astronomers and collaborators who met him at a talk or read a paper, students looking for projects or supervision, and outreach/podcast organisers.

## Product Purpose

The personal academic website of Dr. Iván Muñoz Rodríguez, postdoctoral researcher in X-ray astrophysics at CEA Paris-Saclay (DAp). It presents research, publications and CV, and gives people a way to reach him.

Success means a visitor does all of the following:
- gets a sense of the person beyond the research (physiology, nutrition, sport science, mountain running, reading);
- reads or opens the papers (publication list, NASA ADS library);
- reads or downloads the CV;
- gets in touch by email about a collaboration, job, talk or supervision.

## Positioning

A researcher who works across observations, simulations and statistical modelling: AGN and supermassive black hole growth, galaxy clusters, X-ray cluster surveys (FornaX, Euclid Consortium). The same work reads as astrophysics expertise to academics and as applied data science to industry. The site should support both readings truthfully, without hiding either.

## Operating Context

- Visitors usually arrive from a CV link, an application, a conference talk, ORCID/ADS, LinkedIn or GitHub, and often skim before deciding whether to read further.
- Pages: About (home), Research, Publications, CV, Contact. A Blog page exists but is disabled.
- Content is edited by hand in Markdown/HTML pages; CV PDF at `assets/cv/cv_munoz_rodriguez.pdf`.

## Capabilities and Constraints

- Jekyll site deployed by GitHub Pages. Only GitHub Pages whitelisted plugins (`jekyll-seo-tag`, `jekyll-sitemap`, `jekyll-feed` in use).
- Custom SCSS in `_sass/`, entry point `assets/css/main.scss`; layouts in `_layouts/`, partials in `_includes/`.
- **Must keep:** the client-side daily quote (`_data/quotes.yml`, `_includes/daily-quote.html`), part of the site's character.
- **Must keep:** dark/light theme support (`features.dark_mode`).
- **Blog stays off:** do not design around a blog for now (`features.blog_enabled: false`).
- `reading_list` feature flag exists but is not implemented.

## Brand Commitments

- Name as displayed: "Iván Muñoz Rodríguez" (with accents); title "Dr." in site title.
- Identifiers: ORCID `0000-0001-7161-4112`, GitHub `IvanMuro`, NASA ADS library link, LinkedIn.
- Voice: first person, plain and friendly ("I'm always happy to discuss…").

## Evidence on Hand

- Profile photo `assets/images/profile.jpg`; career timeline photos in `assets/images/timeline/` (Salamanca, Granada, NOA, ESO, PhD, CEA).
- Real publication list (first-author, in preparation, co-authored) in `publications.md`; NASA ADS library.
- CV content in `cv.md` (positions, education, awards & funding incl. ESO-Garching Visitor Programme 2024, industry experience, collaborations, skills, supervision, outreach, talks, references) and the PDF.
- No testimonials, metrics or endorsements exist; do not invent any. Citation counts or impact numbers must come from ADS, not be made up.

## Product Principles

1. Serve both academic and industry readers equally: the same facts, framed so each can find what they need quickly.
2. Proof over claims: papers, ADS, CV and real projects carry the weight.
3. Let the person show: the interests outside research and the daily quote are part of the site, not filler.
4. Make contact easy: an email is never more than one step away.
5. Stay simple to maintain: hand-edited content on GitHub Pages, no build tooling beyond Jekyll.
