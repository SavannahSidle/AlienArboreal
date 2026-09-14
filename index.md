---
layout: home
title: null
description: "Crested geckos and select species raised with careful husbandry, biological curiosity, and respect for life."
---

<section class="hero">
  <div class="container">
    <h1 class="hero-title">Alien Arboreal</h1>
    <p class="hero-subtitle">Crested geckos and select species raised with careful husbandry, biological curiosity, and respect for life.</p>
    <div class="hero-actions">
      <a href="{{ '/available/' | relative_url }}" class="btn btn-primary">View Available Geckos</a>
      <a href="{{ '/observations/' | relative_url }}" class="btn btn-secondary">View Observation Log</a>
    </div>
  </div>
</section>

<section class="home-section">
  <div class="container">
    <p>Life is astonishing. We are animals among animals, built from the same ancient matter and sustained by the same land and water. Our work begins there: care deeply, stay curious, and keep improving the worlds we build around them.</p>
    <p><a href="{{ '/about/' | relative_url }}">More about what we do and why &rarr;</a></p>
  </div>
</section>

<section class="home-section">
  <div class="container">
    <div class="section-header">
      <h2>Currently Available</h2>
      <a href="{{ '/available/' | relative_url }}">View all &rarr;</a>
    </div>
    {% assign available_geckos = site.geckos | where: "status", "available" | sort: "name" %}
    {% if available_geckos.size > 0 %}
    <div class="grid grid-3">
      {% for gecko in available_geckos limit:3 %}
      {% assign card_photo = gecko.image %}
      {% if card_photo == nil and gecko.photos and gecko.photos.size > 0 %}
        {% assign card_photo = gecko.photos[0] %}
      {% endif %}
      <a href="{{ gecko.url | relative_url }}" class="card">
        {% if card_photo %}
        <div class="card-image">
          <img src="{{ card_photo | relative_url }}" alt="{{ gecko.name }}" loading="lazy">
        </div>
        {% endif %}
        <div class="card-body">
          <h3 class="card-title">{{ gecko.name }}</h3>
          <div class="card-meta">
            <span class="badge badge-available">Available</span>
            {% if gecko.morph %}<span>{{ gecko.morph }}</span>{% endif %}
          </div>
          {% if gecko.summary %}<p class="card-summary">{{ gecko.summary }}</p>{% endif %}
        </div>
      </a>
      {% endfor %}
    </div>
    {% else %}
    <div class="empty-state">
      <p>No animals are currently listed as available.</p>
    </div>
    {% endif %}
  </div>
</section>

<section class="home-section">
  <div class="container">
    <div class="section-header">
      <h2>Observation Log</h2>
      <a href="{{ '/observations/' | relative_url }}">View all &rarr;</a>
    </div>
    {% assign recent_obs = site.observations | sort: "date" | reverse %}
    {% if recent_obs.size > 0 %}
    <div class="grid grid-3">
      {% for obs in recent_obs limit:3 %}
      <a href="{{ obs.url | relative_url }}" class="card">
        <div class="card-body">
          <h3 class="card-title">{{ obs.title }}</h3>
          <div class="card-meta">
            <time datetime="{{ obs.date | date: '%Y-%m-%d' }}">{{ obs.date | date: "%B %-d, %Y" }}</time>
            {% if obs.type %}<span class="badge">{{ obs.type }}</span>{% endif %}
          </div>
          {% if obs.summary %}<p class="card-summary">{{ obs.summary }}</p>{% endif %}
        </div>
      </a>
      {% endfor %}
    </div>
    {% else %}
    <div class="empty-state">
      <p>Observation notes and research posts are in progress. Check back soon.</p>
    </div>
    {% endif %}
  </div>
</section>

<section class="home-section contact-strip">
  <div class="container">
    <p>Interested in an animal? Reach out directly.</p>
    <div class="contact-strip-links">
      <a href="{{ site.instagram }}">Instagram</a>
      <a href="{{ site.facebook }}">Facebook</a>
      <a href="mailto:{{ site.email }}">Email</a>
    </div>
  </div>
</section>
