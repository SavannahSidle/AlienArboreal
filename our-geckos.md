---
layout: page
title: Our Geckos
eyebrow: Individuals first
description: The geckos currently living with Alien Arboreal.
permalink: /our-geckos/
---
**Each animal is an individual first.** Pairing history, lineage, and availability are part of their story, not their definition.

{% assign current_geckos = site.geckos | where_exp: "gecko", "gecko.status == 'with-us' or gecko.status == 'available'" | sort: "name" %}
{% if current_geckos.size > 0 %}
<div class="grid grid-3">{% for gecko in current_geckos %}<a href="{{ gecko.url | relative_url }}" class="card">{% if gecko.image %}<div class="card-image"><img src="{{ gecko.image | relative_url }}" alt="{{ gecko.name }}" loading="lazy"></div>{% endif %}<div class="card-body"><h2 class="card-title">{{ gecko.name }}</h2><div class="card-meta">{% if gecko.sex %}<span>{{ gecko.sex }}</span>{% endif %}{% if gecko.morph %}<span>{{ gecko.morph }}</span>{% endif %}</div>{% if gecko.summary %}<p class="card-summary">{{ gecko.summary }}</p>{% endif %}</div></a>{% endfor %}</div>
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
