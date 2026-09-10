---
layout: page
title: Placed
eyebrow: New homes
description: Animals who have moved on from Alien Arboreal into new homes.
permalink: /placed/
---
Animals who have moved into new homes are recorded here as **placed**, preserving their history as part of the site's lineage record.

{% assign placed_geckos = site.geckos | where: "status", "placed" | sort: "name" %}
{% if placed_geckos.size > 0 %}
<div class="grid grid-3">{% for gecko in placed_geckos %}<a href="{{ gecko.url | relative_url }}" class="card">{% if gecko.image %}<div class="card-image"><img src="{{ gecko.image | relative_url }}" alt="{{ gecko.name }}" loading="lazy"></div>{% endif %}<div class="card-body"><h2 class="card-title">{{ gecko.name }}</h2><div class="card-meta">{% if gecko.sex %}<span>{{ gecko.sex }}</span>{% endif %}{% if gecko.morph %}<span>{{ gecko.morph }}</span>{% endif %}</div>{% if gecko.summary %}<p class="card-summary">{{ gecko.summary }}</p>{% endif %}</div></a>{% endfor %}</div>
{% else %}
<div class="empty-state"><p>Placed profiles will appear here as records are added.</p></div>
{% endif %}
