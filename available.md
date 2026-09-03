---
layout: page
title: Available Geckos
eyebrow: Current animals
description: Healthy, carefully raised animals placed with people prepared to care for them well.
permalink: /available/
---
{% assign available_geckos = site.geckos | where: "status", "available" %}
{% if available_geckos.size > 0 %}
<div class="grid grid-3">{% for gecko in available_geckos %}<a href="{{ gecko.url | relative_url }}" class="card">{% if gecko.image %}<div class="card-image"><img src="{{ gecko.image | relative_url }}" alt="{{ gecko.name }}" loading="lazy"></div>{% endif %}<div class="card-body"><h2 class="card-title">{{ gecko.name }}</h2><div class="card-meta"><span class="badge badge-available">Available</span>{% if gecko.morph %}<span>{{ gecko.morph }}</span>{% endif %}</div>{% if gecko.summary %}<p class="card-summary">{{ gecko.summary }}</p>{% endif %}</div></a>{% endfor %}</div>
{% else %}
<div class="empty-state"><p><strong>No animals are listed right now.</strong></p><p>Availability changes slowly and intentionally. New listings are shared on our social channels first.</p></div>
{% endif %}

## Before you inquire

Animals are matched carefully, not dispatched like socks. Each listing includes the information needed to understand the individual animal, its background, and its care. Please review our placement, deposit, shipping, and live-arrival terms before contacting us.
