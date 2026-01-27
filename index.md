---
layout: home
title: Home
show_title: false
---

<section class="hero">
  <div class="hero-content">
    <p class="hero-tagline">Postdoctoral Researcher | Data Scientist</p>
    <h1 class="hero-title">Iván Muñoz Rodríguez</h1>
    <p class="hero-subtitle">X-ray Astrophysics · CEA Paris-Saclay</p>
    <p class="hero-description">
      I am an astrophysicist with expertise in the growth of supermassive black holes, the evolution of galaxies and Active Galactic Nuclei (AGN) across cosmic time and different environments, as well as X-ray cluster surveys. My work bridges observations, simulations, and statistical modelling to improve how galaxies, AGN, and galaxy clusters are identified and characterised.
    </p>
    <p class="hero-description">
      Beyond research, I find balance through rock climbing and trail running in the mountains—activities that mirror the patience and persistence required in science. I'm also drawn to philosophy of science and science communication, co-hosting the <a href="#">"Pilgrims of the Kosmos"</a> podcast.
    </p>
    <div class="hero-links">
      <a href="{{ '/research/' | relative_url }}" class="btn btn-primary">
        My Research
      </a>
      <a href="{{ '/publications/' | relative_url }}" class="btn btn-secondary">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
          <polyline points="14 2 14 8 20 8"></polyline>
          <line x1="16" y1="13" x2="8" y2="13"></line>
          <line x1="16" y1="17" x2="8" y2="17"></line>
        </svg>
        Publications
      </a>
    </div>
  </div>
  <div class="hero-image-wrapper">
    <img
      src="{{ '/assets/images/profile.jpg' | relative_url }}"
      alt="Dr. Iván Muñoz Rodríguez"
      class="hero-image"
      onerror="this.style.background='linear-gradient(135deg, var(--color-bg-subtle) 0%, var(--color-bg-alt) 100%)'"
    >
  </div>
</section>

{% include daily-quote.html %}

<section class="section">
  <h2 class="section-title">Research Interests</h2>
  <ul class="keyword-list">
    <li class="keyword-item">X-ray Astronomy</li>
    <li class="keyword-item">Active Galactic Nuclei</li>
    <li class="keyword-item">Galaxy Clusters</li>
    <li class="keyword-item">Supermassive Black Holes</li>
    <li class="keyword-item">Cluster Detection Algorithms</li>
    <li class="keyword-item">Semi-empirical Modelling</li>
    <li class="keyword-item">XMM-Newton</li>
    <li class="keyword-item">Statistical Modelling</li>
    <li class="keyword-item">Large-scale Simulations</li>
  </ul>
</section>

<section class="section">
  <h2 class="section-title">Current Projects</h2>
  <div class="project-grid">
    <article class="project-card">
      <h3 class="project-title">FornaX</h3>
      <p class="project-description">
        Building X-ray cluster and AGN catalogues of the FornaX Euclid deep field. Moderator of the ESA-datalabs & Slack channel, and LOC member for the 2025 Annual Meeting.
      </p>
      <div class="project-tags">
        <span class="tag">Euclid</span>
        <span class="tag">X-ray Catalogues</span>
      </div>
    </article>
    <article class="project-card">
      <h3 class="project-title">Euclid Consortium</h3>
      <p class="project-description">
        Active member of the Science Working Groups for Clusters of Galaxies and Galaxy Evolution, contributing to multi-wavelength cluster science.
      </p>
      <div class="project-tags">
        <span class="tag">Euclid</span>
        <span class="tag">Galaxy Evolution</span>
      </div>
    </article>
   <!--- <article class="project-card">
      <h3 class="project-title">The 300 Project</h3>
      <p class="project-description">
        Exploring the incidence of AGN in galaxy clusters using hydrodynamical simulations, bridging theory and observations.
      </p>
      <div class="project-tags">
        <span class="tag">Simulations</span>
        <span class="tag">AGN in Clusters</span>
      </div>
    </article>
    -->
  </div>
</section>

<section class="section">
  <h2 class="section-title">Research Path</h2>
  <div class="research-timeline">
    <div class="timeline-item timeline-current timeline-major">
      <div class="timeline-content">
        <span class="timeline-date">Jan 2025 – Present</span>
        <h3 class="timeline-title">Postdoctoral Researcher</h3>
        <p class="timeline-location">CEA Paris-Saclay, Astrophysics Department</p>
        <p class="timeline-description">Building X-ray cluster and AGN catalogues for the FornaX Euclid deep field.</p>
      </div>
      <div class="timeline-image">
        <img src="{{ '/assets/images/timeline/cea.jpg' | relative_url }}" alt="CEA Paris-Saclay" onerror="this.parentElement.innerHTML='🔬'">
      </div>
    </div>
    <div class="timeline-item timeline-major">
      <div class="timeline-content">
        <span class="timeline-date">Aug 2024</span>
        <h3 class="timeline-title">PhD Defence</h3>
        <p class="timeline-location">NOA Athens & University of Southampton</p>
        <p class="timeline-description">Successfully defended thesis: "Semi-empirical models of X-ray AGN in galaxy clusters".</p>
      </div>
      <div class="timeline-image">
        <img src="{{ '/assets/images/timeline/phd.jpg' | relative_url }}" alt="PhD Defence" onerror="this.parentElement.innerHTML='🎓'">
      </div>
    </div>
    <div class="timeline-item">
      <div class="timeline-content">
        <span class="timeline-date">2022</span>
        <h3 class="timeline-title">Joined Euclid Consortium</h3>
        <p class="timeline-location">SWG Clusters & Galaxy Evolution</p>
        <p class="timeline-description">Contributing to multi-wavelength cluster science.</p>
      </div>
      <div class="timeline-image">
        <img src="{{ '/assets/images/timeline/euclid.jpg' | relative_url }}" alt="Euclid" onerror="this.parentElement.innerHTML='🛰️'">
      </div>
    </div>
    <div class="timeline-item">
      <div class="timeline-content">
        <span class="timeline-date">2022</span>
        <h3 class="timeline-title">ESO Visitor Programme</h3>
        <p class="timeline-location">European Southern Observatory, Garching</p>
        <p class="timeline-description">3-month research visit studying the radial distribution of AGN in ~80 clusters.</p>
      </div>
      <div class="timeline-image">
        <img src="{{ '/assets/images/timeline/eso.jpg' | relative_url }}" alt="ESO Garching" onerror="this.parentElement.innerHTML='🔭'">
      </div>
    </div>
    <div class="timeline-item timeline-major">
      <div class="timeline-content">
        <span class="timeline-date">Oct 2020</span>
        <h3 class="timeline-title">Marie Curie PhD Fellow</h3>
        <p class="timeline-location">NOA Athens & University of Southampton</p>
        <p class="timeline-description">Started PhD on semi-empirical models of X-ray AGN in galaxy clusters (BiD4BESt ITN).</p>
      </div>
      <div class="timeline-image">
        <img src="{{ '/assets/images/timeline/noa.jpg' | relative_url }}" alt="NOA Athens" onerror="this.parentElement.innerHTML='🇬🇷'">
      </div>
    </div>
    <div class="timeline-item">
      <div class="timeline-content">
        <span class="timeline-date">2019 – 2020</span>
        <h3 class="timeline-title">M.Sc. in Astronomy</h3>
        <p class="timeline-location">University of Granada, Spain</p>
        <p class="timeline-description">CARMENES collaboration. Thesis on exoplanet detectability and occurrence rates.</p>
      </div>
      <div class="timeline-image">
        <img src="{{ '/assets/images/timeline/granada.jpg' | relative_url }}" alt="Granada" onerror="this.parentElement.innerHTML='🌌'">
      </div>
    </div>
    <div class="timeline-item timeline-major">
      <div class="timeline-content">
        <span class="timeline-date">2014 – 2019</span>
        <h3 class="timeline-title">B.Sc. in Physics</h3>
        <p class="timeline-location">University of Salamanca, Spain</p>
        <p class="timeline-description">Thesis on astronomical bounds of Primordial Black Holes.</p>
      </div>
      <div class="timeline-image">
        <img src="{{ '/assets/images/timeline/salamanca.jpg' | relative_url }}" alt="Salamanca" onerror="this.parentElement.innerHTML='⚛️'">
      </div>
    </div>
  </div>
</section>
