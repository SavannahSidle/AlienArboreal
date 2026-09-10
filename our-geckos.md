---
layout: page
title: Our Geckos
eyebrow: Individuals first
description: Individual geckos, pairings, and family histories.
permalink: /our-geckos/
---
**Each animal is an individual first.** Pairing history, lineage, and availability are part of their story, not their definition.

<div class="grid grid-3" style="margin:1.5rem 0 2.5rem">
  <a class="card" href="#individuals"><div class="card-body"><h2 class="card-title">Individuals</h2><p class="card-summary">Profiles for the geckos themselves.</p></div></a>
  <a class="card" href="{{ '/pairings/' | relative_url }}"><div class="card-body"><h2 class="card-title">Pairings</h2><p class="card-summary">Past, present, and planned pairings.</p></div></a>
  <a class="card" href="{{ '/lineage/' | relative_url }}"><div class="card-body"><h2 class="card-title">Family Histories</h2><p class="card-summary">Parentage and offspring across generations.</p></div></a>
</div>

<h2 id="individuals">Individuals</h2>

{% assign with_us = site.geckos | where: "status", "with-us" %}
{% assign available = site.geckos | where: "status", "available" %}
{% assign current_geckos = with_us | concat: available | sort: "name" %}
{% if current_geckos.size > 0 %}
<div class="grid grid-3">{% for gecko in current_geckos %}<a href="{{ gecko.url | relative_url }}" class="card">{% if gecko.image %}<div class="card-image"><img src="{{ gecko.image | relative_url }}" alt="{{ gecko.name }}" loading="lazy"></div>{% endif %}<div class="card-body"><h3 class="card-title">{{ gecko.name }}</h3><div class="card-meta">{% if gecko.sex %}<span>{{ gecko.sex }}</span>{% endif %}{% if gecko.morph %}<span>{{ gecko.morph }}</span>{% endif %}</div>{% if gecko.summary %}<p class="card-summary">{{ gecko.summary }}</p>{% endif %}</div></a>{% endfor %}</div>
{% else %}
<div class="empty-state"><p>Profiles are being added.</p></div>
{% endif %}

## Placed

{% assign placed_geckos = site.geckos | where: "status", "placed" | sort: "name" %}
{% if placed_geckos.size > 0 %}
<div class="grid grid-3">{% for gecko in placed_geckos %}<a href="{{ gecko.url | relative_url }}" class="card">{% if gecko.image %}<div class="card-image"><img src="{{ gecko.image | relative_url }}" alt="{{ gecko.name }}" loading="lazy"></div>{% endif %}<div class="card-body"><h3 class="card-title">{{ gecko.name }}</h3><div class="card-meta">{% if gecko.sex %}<span>{{ gecko.sex }}</span>{% endif %}{% if gecko.morph %}<span>{{ gecko.morph }}</span>{% endif %}</div></div></a>{% endfor %}</div>
{% else %}
<p>No placed profiles have been added yet.</p>
{% endif %}
