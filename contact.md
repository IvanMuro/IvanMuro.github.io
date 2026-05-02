---
layout: page
title: Contact
subtitle: Get in touch for research collaborations or inquiries
permalink: /contact/
---

<div class="page-content" markdown="1">

I'm always happy to discuss potential collaborations, research ideas, or opportunities. Feel free to reach out through any of the channels below.

<div class="contact-grid" style="margin-top: var(--space-8);">

  <a href="mailto:{{ site.author.email }}" class="contact-card">
    <div class="contact-icon">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
        <polyline points="22,6 12,13 2,6"></polyline>
      </svg>
    </div>
    <div class="contact-info">
      <span class="contact-label">Email</span>
      <span class="contact-value">{{ site.author.email }}</span>
    </div>
  </a>

  <a href="https://orcid.org/{{ site.author.orcid }}" class="contact-card" target="_blank" rel="noopener">
    <div class="contact-icon">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
        <path d="M12 0C5.372 0 0 5.372 0 12s5.372 12 12 12 12-5.372 12-12S18.628 0 12 0zM7.369 4.378c.525 0 .947.431.947.947s-.422.947-.947.947a.95.95 0 0 1-.947-.947c0-.525.422-.947.947-.947zm-.722 3.038h1.444v10.041H6.647V7.416zm3.562 0h3.9c3.712 0 5.344 2.653 5.344 5.025 0 2.578-2.016 5.025-5.325 5.025h-3.919V7.416zm1.444 1.303v7.444h2.297c3.272 0 4.022-2.484 4.022-3.722 0-2.016-1.284-3.722-4.097-3.722h-2.222z"/>
      </svg>
    </div>
    <div class="contact-info">
      <span class="contact-label">ORCID</span>
      <span class="contact-value">{{ site.author.orcid }}</span>
    </div>
  </a>

  {% if site.author.github %}
  <a href="https://github.com/{{ site.author.github }}" class="contact-card" target="_blank" rel="noopener">
    <div class="contact-icon">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
        <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
      </svg>
    </div>
    <div class="contact-info">
      <span class="contact-label">GitHub</span>
      <span class="contact-value">@{{ site.author.github }}</span>
    </div>
  </a>
  {% endif %}

  {% if site.author.linkedin %}
  <a href="{{ site.author.linkedin }}" class="contact-card" target="_blank" rel="noopener">
    <div class="contact-icon">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
        <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
      </svg>
    </div>
    <div class="contact-info">
      <span class="contact-label">LinkedIn</span>
      <span class="contact-value">Iván Muñoz Rodríguez</span>
    </div>
  </a>
  {% endif %}

  <a href="{{ site.author.ads_library }}" class="contact-card" target="_blank" rel="noopener">
    <div class="contact-icon">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="12" cy="12" r="10"></circle>
        <circle cx="12" cy="12" r="4"></circle>
        <line x1="4.93" y1="4.93" x2="9.17" y2="9.17"></line>
        <line x1="14.83" y1="14.83" x2="19.07" y2="19.07"></line>
        <line x1="14.83" y1="9.17" x2="19.07" y2="4.93"></line>
        <line x1="4.93" y1="19.07" x2="9.17" y2="14.83"></line>
      </svg>
    </div>
    <div class="contact-info">
      <span class="contact-label">NASA ADS</span>
      <span class="contact-value">Publication Library</span>
    </div>
  </a>

</div>

<section class="section">
<h2 class="section-title">Institutional Address</h2>
<div style="padding: var(--space-5); background-color: var(--color-bg-alt); border-radius: var(--radius-lg);">
  <p style="margin: 0; font-size: var(--text-sm);">
    <strong>{{ site.author.name }}</strong><br>
    {{ site.author.department }}<br>
    {{ site.author.affiliation }}<br>
    Orme des Merisiers, Bât. 709<br>
    91191 Gif-sur-Yvette, France
  </p>
</div>
</section>

<section class="section">
<h2 class="section-title">Research Collaboration</h2>
<p>I'm particularly interested in collaborations involving:</p>
<ul>
  <li><strong>AGN in galaxy clusters</strong> – environmental effects on SMBH growth, AGN triggering mechanisms</li>
  <li><strong>X-ray cluster surveys</strong> – cluster detection, AGN contamination, selection functions</li>
  <li><strong>Semi-empirical modelling</strong> – connecting simulations to observations</li>
  <li><strong>Multi-wavelength studies</strong> – combining X-ray with optical/IR data (Euclid, etc.)</li>
</ul>
<p>If your work intersects with any of these areas, I'd be happy to discuss potential synergies.</p>
</section>

<section class="section">
<h2 class="section-title">For Students</h2>
<p>If you're a master's or PhD student interested in AGN, galaxy clusters, or data science applications in astronomy, feel free to reach out. I'm happy to discuss:</p>
<ul>
  <li>Potential research project ideas</li>
  <li>Career paths in astrophysics (including industry transitions)</li>
  <li>Technical questions about data analysis and statistical modelling</li>
</ul>
</section>

<section class="section">
<h2 class="section-title">Speaking & Outreach</h2>
<p>I'm available for:</p>
<ul>
  <li>Conference and seminar talks</li>
  <li>Public outreach events</li>
  <li>Podcast appearances (particularly on topics related to X-ray astronomy, cosmology, or the philosophy of science)</li>
  <li>Science communication collaborations</li>
</ul>
<p>Please get in touch via email to discuss opportunities.</p>
</section>

</div>
