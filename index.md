---
layout: home
show_title: false
---

<section class="hero">
  <div class="hero-backdrop" aria-hidden="true">{% include xray-field.svg %}</div>
  <div class="hero-content">
    <h1 class="hero-title">Iván Muñoz Rodríguez</h1>
    <p class="hero-subtitle"><span class="hero-role">Postdoctoral researcher &amp; data scientist</span> <span class="hero-role"><span class="nowrap">X-ray astrophysics</span>, CosmoStat, CEA Paris-Saclay</span></p>
    <p class="hero-description">
      I am an astrophysicist. I study how supermassive black holes grow, how galaxies and Active Galactic Nuclei (AGN) evolve across cosmic time and in different environments, and how galaxy clusters are found in X-ray surveys. My work bridges observations, simulations, and statistical modelling to improve how galaxies, AGN, and galaxy clusters are identified and characterised.
    </p>
    <p class="hero-description">
      Beyond research, I am deeply interested in physiology, nutrition and sport science. You can also find me running in the mountains or reading.
    </p>
    <p class="hero-links">
      <a class="button-primary" href="{{ '/assets/cv/cv_munoz_rodriguez.pdf' | relative_url }}">CV (PDF)</a>
      <a href="{{ '/publications/' | relative_url }}">Publications</a>
      <a href="https://github.com/{{ site.author.github }}" target="_blank" rel="noopener">GitHub<span class="sr-only"> (opens in a new tab)</span></a>
      <a href="mailto:{{ site.author.email }}">Email</a>
    </p>
  </div>
  <div class="hero-image-wrapper">
    <img
      src="{{ '/assets/images/profile.jpg' | relative_url }}"
      alt="Iván Muñoz Rodríguez"
      class="hero-image"
      width="800"
      height="800"
      fetchpriority="high"
    >
  </div>
</section>

{% include daily-quote.html %}

<section class="section">
  <h2 class="section-title">What I do</h2>
  <dl class="focus-list">
    <div class="focus-item">
      <dt>X-ray surveys &amp; clusters</dt>
      <dd>Finding galaxy clusters in XMM-Newton surveys and modelling which ones a survey detects, and why. I lead the FornaX selection function.</dd>
    </div>
    <div class="focus-item">
      <dt>AI &amp; large datasets</dt>
      <dd>Machine learning for X-ray source classification and Euclid catalogues, in Python (scikit-learn, JAX, TensorFlow) on HPC clusters.</dd>
    </div>
    <div class="focus-item">
      <dt>Simulations &amp; forward modelling</dt>
      <dd>Semi-empirical and forward models of observables on N-body simulations; hydrodynamical simulation analysis.</dd>
    </div>
    <div class="focus-item">
      <dt>Black holes &amp; environment</dt>
      <dd>How cluster environments trigger AGN, and how AGN contaminate X-ray cluster detection.</dd>
    </div>
  </dl>
</section>

<section class="section">
  <h2 class="section-title">Selected papers</h2>
  {% if site.data.ads_metrics %}
  <p class="paper-stats">{{ site.data.ads_metrics.refereed }} refereed papers · {{ site.data.ads_metrics.citations }} citations · h-index {{ site.data.ads_metrics.h_index }} <span class="paper-stats-source">(NASA ADS)</span></p>
  {% endif %}
  <ul class="publication-list publication-list--home">
    <li class="publication-item">
      <h3 class="publication-title">
        <a href="https://doi.org/10.1093/mnras/stae1465" target="_blank" rel="noopener">Scrutinizing evidence for the triggering of active galactic nuclei in the outskirts of massive galaxy clusters at z ≈ 1<span class="sr-only"> (opens in a new tab)</span></a>
      </h3>
      <p class="publication-finding">The apparent excess of AGN in the outskirts of z ≈ 1 clusters is most likely background and foreground sources, so current data cannot yet show cluster infall switching black holes on.</p>
      <p class="publication-authors"><span class="author-highlight">Muñoz Rodríguez, I.</span>, et al.</p>
      <p class="publication-venue">MNRAS, 2024</p>
      <div class="publication-links">
        <a href="https://doi.org/10.1093/mnras/stae1465" target="_blank" rel="noopener">DOI<span class="sr-only"> (opens in a new tab)</span></a>
        <a href="https://ui.adsabs.harvard.edu/abs/10.1093/mnras/stae1465/abstract" target="_blank" rel="noopener">ADS<span class="sr-only"> (opens in a new tab)</span></a>
      </div>
    </li>
    <li class="publication-item">
      <h3 class="publication-title">
        <a href="https://doi.org/10.1093/mnras/stac3114" target="_blank" rel="noopener">Cosmic evolution of the incidence of Active Galactic Nuclei in massive clusters: Simulations versus observations<span class="sr-only"> (opens in a new tab)</span></a>
      </h3>
      <p class="publication-finding">Compared with a model where environment plays no role, massive clusters boost black hole growth at z ≈ 1.2 and suppress it near the present day.</p>
      <p class="publication-authors"><span class="author-highlight">Muñoz Rodríguez, I.</span>, et al.</p>
      <p class="publication-venue">MNRAS, 2023</p>
      <div class="publication-links">
        <a href="https://doi.org/10.1093/mnras/stac3114" target="_blank" rel="noopener">DOI<span class="sr-only"> (opens in a new tab)</span></a>
        <a href="https://ui.adsabs.harvard.edu/abs/2023MNRAS.518.1041M" target="_blank" rel="noopener">ADS<span class="sr-only"> (opens in a new tab)</span></a>
      </div>
    </li>
  </ul>
  <p class="section-more"><a href="{{ '/publications/' | relative_url }}">All publications →</a></p>
</section>

<section class="section">
  <h2 class="section-title">Research path</h2>
  <ul class="entry-list">
    <li class="entry">
      <span class="entry-date">Jan 2025 – present</span>
      <div class="entry-with-image">
        <div>
          <h3 class="entry-title">Postdoctoral Researcher</h3>
          <p class="entry-meta">CosmoStat, CEA Paris-Saclay</p>
          <p class="entry-body">Leading the FornaX cluster selection function and building its X-ray catalogues; co-lead of the FornaX AGN group. Euclid Consortium member since 2022.</p>
        </div>
        <img loading="lazy" decoding="async" src="{{ '/assets/images/timeline/cea.jpg' | relative_url }}" alt="CEA Paris-Saclay" width="168" height="112">
      </div>
    </li>
    <li class="entry">
      <span class="entry-date">Aug 2024</span>
      <div class="entry-with-image">
        <div>
          <h3 class="entry-title">PhD Defence</h3>
          <p class="entry-meta">National Observatory of Athens &amp; University of Southampton</p>
          <p class="entry-body">Thesis: “Semi-empirical models of X-ray AGN in galaxy clusters”.</p>
        </div>
        <img loading="lazy" decoding="async" src="{{ '/assets/images/timeline/phd.jpg' | relative_url }}" alt="PhD defence" width="168" height="112">
      </div>
    </li>
    <li class="entry">
      <span class="entry-date">2024</span>
      <div class="entry-with-image">
        <div>
          <h3 class="entry-title">ESO Visitor Programme</h3>
          <p class="entry-meta">European Southern Observatory, Garching</p>
          <p class="entry-body">Three-month visit studying the radial distribution of AGN in ~80 clusters.</p>
        </div>
        <img loading="lazy" decoding="async" src="{{ '/assets/images/timeline/eso.jpg' | relative_url }}" alt="ESO Garching" width="168" height="112">
      </div>
    </li>
    <li class="entry">
      <span class="entry-date">Oct 2020</span>
      <div class="entry-with-image">
        <div>
          <h3 class="entry-title">Marie Curie PhD Fellow</h3>
          <p class="entry-meta">National Observatory of Athens &amp; University of Southampton</p>
          <p class="entry-body">Started PhD on semi-empirical models of X-ray AGN in galaxy clusters (BiD4BESt ITN).</p>
        </div>
        <img loading="lazy" decoding="async" src="{{ '/assets/images/timeline/noa.jpg' | relative_url }}" alt="National Observatory of Athens" width="168" height="112">
      </div>
    </li>
    <li class="entry">
      <span class="entry-date">2019 – 2020</span>
      <div class="entry-with-image">
        <div>
          <h3 class="entry-title">M.Sc. in Astronomy</h3>
          <p class="entry-meta">University of Granada</p>
          <p class="entry-body">CARMENES collaboration. Thesis on exoplanet detectability and occurrence rates.</p>
        </div>
        <img loading="lazy" decoding="async" src="{{ '/assets/images/timeline/granada.jpg' | relative_url }}" alt="Granada" width="168" height="112">
      </div>
    </li>
    <li class="entry">
      <span class="entry-date">2014 – 2019</span>
      <div class="entry-with-image">
        <div>
          <h3 class="entry-title">B.Sc. in Physics</h3>
          <p class="entry-meta">University of Salamanca</p>
          <p class="entry-body">Thesis on astronomical bounds of primordial black holes.</p>
        </div>
        <img loading="lazy" decoding="async" src="{{ '/assets/images/timeline/salamanca.jpg' | relative_url }}" alt="Salamanca" width="168" height="112">
      </div>
    </li>
  </ul>
  <p class="section-more"><a href="{{ '/cv/' | relative_url }}">Full CV →</a></p>
</section>

<section class="section closing">
  <p>Open to collaborations, talks, and research or data-science roles. <a href="mailto:{{ site.author.email }}">Email me →</a></p>
</section>
