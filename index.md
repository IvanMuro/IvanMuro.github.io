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
  <h2 class="section-title">Latest News</h2>
  <div class="cv-section">
    <div class="cv-item">
      <div class="cv-item-header">
        <span class="cv-item-title">Postdoctoral Researcher at CEA Paris-Saclay</span>
        <span class="cv-item-date">January 2025</span>
      </div>
      <p class="cv-item-subtitle">Astrophysics Department (DAp)</p>
      <p class="cv-item-description">Started a new position working on X-ray cluster surveys and AGN catalogues for the FornaX project.</p>
    </div>
    <div class="cv-item">
      <div class="cv-item-header">
        <span class="cv-item-title">PhD Defence</span>
        <span class="cv-item-date">August 2024</span>
      </div>
      <p class="cv-item-subtitle">National Observatory of Athens & University of Southampton</p>
      <p class="cv-item-description">Successfully defended PhD thesis on "Semi-empirical models of X-ray AGN in galaxy clusters".</p>
    </div>
    <div class="cv-item">
      <div class="cv-item-header">
        <span class="cv-item-title">ESO Visitor Programme</span>
        <span class="cv-item-date">2022</span>
      </div>
      <p class="cv-item-subtitle">European Southern Observatory, Garching</p>
      <p class="cv-item-description">Awarded 3-month funding to study the radial distribution of ~80 clusters at intermediate redshift and design an AGN follow-up program.</p>
    </div>
  </div>
</section>
