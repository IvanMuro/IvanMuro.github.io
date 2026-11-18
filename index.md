---
layout: home
show_title: false
---

<div class="landing">
  <header class="landing-head hero-head">
    <div class="hero-image-wrapper">
      <div class="sky" aria-hidden="true"></div>
      <img
        src="{{ '/assets/images/profile.jpg' | relative_url }}"
        alt="Portrait of Iván Muñoz Rodríguez"
        class="hero-image"
        width="800"
        height="800"
        fetchpriority="high"
      >
    </div>
    <div>
      <h1 class="hero-title" id="intro-name">Iván Muñoz Rodríguez</h1>
      <p class="hero-subtitle"><span class="hero-role">Postdoctoral researcher</span> <span class="hero-role"><span class="nowrap">X-ray astrophysics</span>, CosmoStat, CEA Paris-Saclay</span></p>
    </div>
  </header>

  <aside class="landing-note">
    {% include daily-quote.html %}
  </aside>

  <section class="intro" aria-label="About">
    <p class="hero-description">
      I work on getting reliable answers out of large, incomplete survey data, combining observations, simulations and statistical modelling to identify and characterise galaxies, Active Galactic Nuclei (AGN) and galaxy clusters. As an astrophysicist, I use this to study how supermassive black holes grow, how galaxies and AGN evolve across cosmic time and in different environments, and how galaxy clusters are found in X-ray surveys.
    </p>
    <p class="hero-description">
      Beyond research, I am deeply interested in physiology, nutrition and sport science. You can also find me running in the mountains or reading.
    </p>
    <p class="hero-description intro-open">Open to collaborations, talks, student projects, and research roles.</p>
    <p class="hero-links">
      <a class="button-primary" href="{{ '/assets/cv/cv_munoz_rodriguez.pdf' | relative_url }}" target="_blank" rel="noopener">CV (PDF)<span class="sr-only"> (opens in a new tab)</span></a>
      <a href="mailto:{{ site.author.email }}">Email</a>
      <a href="https://github.com/{{ site.author.github }}" target="_blank" rel="noopener">GitHub<span class="sr-only"> (opens in a new tab)</span></a>
      <a href="{{ site.author.linkedin }}" target="_blank" rel="noopener">LinkedIn<span class="sr-only"> (opens in a new tab)</span></a>
    </p>
  </section>

  <section class="landing-block landing-work" aria-labelledby="work-title">
    <h2 class="landing-title" id="work-title">What I do</h2>
    <ul class="source-list">
      <li class="source-item">
        <span class="source-mark" aria-hidden="true"></span>
        <details class="source-detail">
          <summary>X-ray surveys &amp; clusters</summary>
          <p>Finding galaxy clusters in XMM-Newton surveys and modelling which ones a survey detects. I lead this selection function for FornaX.</p>
          <a class="source-more" href="{{ '/research/#x-ray-cluster-surveys' | relative_url }}">More in Research →</a>
        </details>
      </li>
      <li class="source-item">
        <span class="source-mark" aria-hidden="true"></span>
        <details class="source-detail">
          <summary>AI &amp; large datasets</summary>
          <p>Machine learning for X-ray source classification and Euclid catalogues, in Python on HPC clusters.</p>
          <a class="source-more" href="{{ '/research/#machine-learning' | relative_url }}">More in Research →</a>
        </details>
      </li>
      <li class="source-item">
        <span class="source-mark" aria-hidden="true"></span>
        <details class="source-detail">
          <summary>Simulations &amp; forward modelling</summary>
          <p>Semi-empirical and forward models of what surveys observe, built on N-body and hydrodynamical simulations.</p>
          <a class="source-more" href="{{ '/research/#modelling' | relative_url }}">More in Research →</a>
        </details>
      </li>
      <li class="source-item">
        <span class="source-mark" aria-hidden="true"></span>
        <details class="source-detail">
          <summary>Black holes &amp; environment</summary>
          <p>How cluster environments trigger AGN, and how AGN contaminate X-ray cluster detection.</p>
          <a class="source-more" href="{{ '/research/#agn-in-clusters' | relative_url }}">More in Research →</a>
        </details>
      </li>
    </ul>
  </section>

  <section class="landing-block landing-papers" aria-labelledby="papers-title">
    <h2 class="landing-title" id="papers-title">Selected papers</h2>
    {% if site.data.ads_metrics %}
    <p class="paper-stats">{{ site.data.ads_metrics.refereed }} refereed papers · {{ site.data.ads_metrics.citations }} citations · h-index {{ site.data.ads_metrics.h_index }} <span class="paper-stats-source">(NASA ADS)</span></p>
    {% endif %}
    <ul class="source-list">
      <li class="source-item">
        <span class="source-mark" aria-hidden="true"></span>
        <div>
          <h3 class="paper-title"><a href="https://doi.org/10.1093/mnras/stae1465" target="_blank" rel="noopener">Scrutinizing evidence for the triggering of active galactic nuclei in the outskirts of massive galaxy clusters at z ≈ 1<span class="sr-only"> (opens in a new tab)</span></a></h3>
          <p class="paper-finding">The apparent excess of AGN in the outskirts of z ≈ 1 clusters is most likely background and foreground sources, so current data cannot yet show cluster infall switching black holes on.</p>
          <p class="paper-meta"><span class="author-highlight">Muñoz Rodríguez, I.</span>, et al. · MNRAS, 2024 · <a href="https://ui.adsabs.harvard.edu/abs/10.1093/mnras/stae1465/abstract" target="_blank" rel="noopener">ADS<span class="sr-only"> (opens in a new tab)</span></a></p>
        </div>
      </li>
      <li class="source-item">
        <span class="source-mark" aria-hidden="true"></span>
        <div>
          <h3 class="paper-title"><a href="https://doi.org/10.1093/mnras/stac3114" target="_blank" rel="noopener">Cosmic evolution of the incidence of Active Galactic Nuclei in massive clusters: Simulations versus observations<span class="sr-only"> (opens in a new tab)</span></a></h3>
          <p class="paper-finding">Compared with a model where environment plays no role, massive clusters boost black hole growth at z ≈ 1.2 and suppress it near the present day.</p>
          <p class="paper-meta"><span class="author-highlight">Muñoz Rodríguez, I.</span>, et al. · MNRAS, 2023 · <a href="https://ui.adsabs.harvard.edu/abs/2023MNRAS.518.1041M" target="_blank" rel="noopener">ADS<span class="sr-only"> (opens in a new tab)</span></a></p>
        </div>
      </li>
    </ul>
    <p class="section-more"><a href="{{ '/publications/' | relative_url }}">All publications →</a> <a href="{{ site.author.ads_library }}" target="_blank" rel="noopener">Full list on NASA ADS ↗<span class="sr-only"> (opens in a new tab)</span></a></p>
  </section>

</div>
