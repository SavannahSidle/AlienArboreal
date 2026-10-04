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
  <a class="card" href="{{ '/lineage/' | relative_url }}"><div class="card-body"><h2 class="card-title">Lineage</h2><p class="card-summary">Family histories, parentage, offspring, and the visual Family Tree.</p></div></a>
</div>

<style>
.gecko-sex-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:.6rem;margin:.65rem 0 1.6rem}
.gecko-mini{display:flex;align-items:center;gap:.75rem;padding:.65rem;border:1px solid var(--line);border-radius:5px;background:var(--panel);text-decoration:none;color:var(--ink)}
.gecko-mini:hover{border-color:var(--moss)}
.gecko-mini-thumb{width:64px;height:64px;flex:0 0 64px;border-radius:4px;overflow:hidden;background:rgba(255,255,255,.03);border:1px solid var(--line)}
.gecko-mini-thumb img{width:100%;height:100%;object-fit:cover}
.gecko-mini-placeholder{width:100%;height:100%;display:grid;place-items:center;color:var(--muted);font:400 .6rem "Space Mono",monospace;text-align:center}
.gecko-mini-copy{min-width:0}
.gecko-mini-copy strong{display:block}
.gecko-mini-copy small{display:block;margin-top:.12rem;color:var(--muted);font:400 .66rem "Space Mono",monospace}
.gecko-mini-copy .available{color:var(--acid)}
.sex-heading{margin:1.25rem 0 .4rem!important;font-size:1.05rem}
@media(max-width:700px){.gecko-sex-grid{grid-template-columns:1fr}}
</style>

<h2 id="individuals">Individuals</h2>

{% assign with_us = site.geckos | where: "status", "with-us" %}
{% assign available = site.geckos | where: "status", "available" %}
{% assign current_geckos = with_us | concat: available | sort: "name" %}
{% assign current_males = current_geckos | where: "sex", "Male" %}
{% assign current_females = current_geckos | where: "sex", "Female" %}

{% if current_males.size > 0 %}
<h3 class="sex-heading">Males</h3>
<div class="gecko-sex-grid">
{% for gecko in current_males %}
{% assign card_photo = gecko.image %}
{% if card_photo == nil and gecko.photos and gecko.photos.size > 0 %}{% assign card_photo = gecko.photos[0] %}{% endif %}
<a href="{{ gecko.url | relative_url }}" class="gecko-mini">
  <div class="gecko-mini-thumb">{% if card_photo %}<img src="{{ card_photo | relative_url }}" alt="{{ gecko.name }}" loading="lazy">{% else %}<div class="gecko-mini-placeholder">photo<br>coming</div>{% endif %}</div>
  <div class="gecko-mini-copy"><strong>{{ gecko.name }}</strong>{% if gecko.identifier and gecko.identifier != gecko.name %}<small>{{ gecko.identifier }}</small>{% endif %}{% if gecko.morph %}<small>{{ gecko.morph }}</small>{% endif %}{% if gecko.status == "available" %}<small class="available">Available{% if gecko.placement_note %} · {{ gecko.placement_note }}{% endif %}</small>{% endif %}</div>
</a>
{% endfor %}
</div>
{% endif %}

{% if current_females.size > 0 %}
<h3 class="sex-heading">Females</h3>
<div class="gecko-sex-grid">
{% for gecko in current_females %}
{% assign card_photo = gecko.image %}
{% if card_photo == nil and gecko.photos and gecko.photos.size > 0 %}{% assign card_photo = gecko.photos[0] %}{% endif %}
<a href="{{ gecko.url | relative_url }}" class="gecko-mini">
  <div class="gecko-mini-thumb">{% if card_photo %}<img src="{{ card_photo | relative_url }}" alt="{{ gecko.name }}" loading="lazy">{% else %}<div class="gecko-mini-placeholder">photo<br>coming</div>{% endif %}</div>
  <div class="gecko-mini-copy"><strong>{{ gecko.name }}</strong>{% if gecko.identifier and gecko.identifier != gecko.name %}<small>{{ gecko.identifier }}</small>{% endif %}{% if gecko.morph %}<small>{{ gecko.morph }}</small>{% endif %}{% if gecko.status == "available" %}<small class="available">Available{% if gecko.placement_note %} · {{ gecko.placement_note }}{% endif %}</small>{% endif %}</div>
</a>
{% endfor %}
</div>
{% endif %}

{% assign current_unknown = current_geckos | where_exp: "g", "g.sex != 'Male' and g.sex != 'Female'" %}
{% if current_unknown.size > 0 %}
<h3 class="sex-heading">Sex not recorded</h3>
<div class="gecko-sex-grid">
{% for gecko in current_unknown %}
{% assign card_photo = gecko.image %}
{% if card_photo == nil and gecko.photos and gecko.photos.size > 0 %}{% assign card_photo = gecko.photos[0] %}{% endif %}
<a href="{{ gecko.url | relative_url }}" class="gecko-mini"><div class="gecko-mini-thumb">{% if card_photo %}<img src="{{ card_photo | relative_url }}" alt="{{ gecko.name }}" loading="lazy">{% else %}<div class="gecko-mini-placeholder">photo<br>coming</div>{% endif %}</div><div class="gecko-mini-copy"><strong>{{ gecko.name }}</strong>{% if gecko.morph %}<small>{{ gecko.morph }}</small>{% endif %}</div></a>
{% endfor %}
</div>
{% endif %}

## Placed

{% assign placed_geckos = site.geckos | where: "status", "placed" | sort: "name" %}
{% assign placed_males = placed_geckos | where: "sex", "Male" %}
{% assign placed_females = placed_geckos | where: "sex", "Female" %}

{% if placed_males.size > 0 %}
<h3 class="sex-heading">Males</h3>
<div class="gecko-sex-grid">
{% for gecko in placed_males %}
{% assign card_photo = gecko.image %}
{% if card_photo == nil and gecko.photos and gecko.photos.size > 0 %}{% assign card_photo = gecko.photos[0] %}{% endif %}
<a href="{{ gecko.url | relative_url }}" class="gecko-mini"><div class="gecko-mini-thumb">{% if card_photo %}<img src="{{ card_photo | relative_url }}" alt="{{ gecko.name }}" loading="lazy">{% else %}<div class="gecko-mini-placeholder">photo<br>coming</div>{% endif %}</div><div class="gecko-mini-copy"><strong>{{ gecko.name }}</strong>{% if gecko.morph %}<small>{{ gecko.morph }}</small>{% endif %}</div></a>
{% endfor %}
</div>
{% endif %}

{% if placed_females.size > 0 %}
<h3 class="sex-heading">Females</h3>
<div class="gecko-sex-grid">
{% for gecko in placed_females %}
{% assign card_photo = gecko.image %}
{% if card_photo == nil and gecko.photos and gecko.photos.size > 0 %}{% assign card_photo = gecko.photos[0] %}{% endif %}
<a href="{{ gecko.url | relative_url }}" class="gecko-mini"><div class="gecko-mini-thumb">{% if card_photo %}<img src="{{ card_photo | relative_url }}" alt="{{ gecko.name }}" loading="lazy">{% else %}<div class="gecko-mini-placeholder">photo<br>coming</div>{% endif %}</div><div class="gecko-mini-copy"><strong>{{ gecko.name }}</strong>{% if gecko.morph %}<small>{{ gecko.morph }}</small>{% endif %}</div></a>
{% endfor %}
</div>
{% endif %}
