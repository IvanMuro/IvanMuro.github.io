---
layout: page
title: Blog
subtitle: Thoughts on science, research, and the journey
permalink: /blog/
---

<div class="page-content">

{% if site.features.blog_enabled %}

{% if site.posts.size > 0 %}
<ul class="blog-list">
  {% for post in site.posts %}
  <li class="blog-item">
    <time class="blog-item-date" datetime="{{ post.date | date_to_xmlschema }}">
      {{ post.date | date: "%B %d, %Y" }}
    </time>
    <h2 class="blog-item-title">
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    </h2>
    {% if post.excerpt %}
    <p class="blog-item-excerpt">{{ post.excerpt | strip_html | truncate: 200 }}</p>
    {% endif %}
  </li>
  {% endfor %}
</ul>
{% else %}
<p>No posts yet. Check back soon!</p>
{% endif %}

{% else %}

<p>Occasional posts about research, astrophysics, and the scientific journey will appear here.</p>

{% endif %}

</div>
