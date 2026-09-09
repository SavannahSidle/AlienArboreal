---
layout: page
title: Lineage
eyebrow: Family histories
description: Parentage and offspring across Alien Arboreal lines.
permalink: /lineage/
---
<div class="lineage-list">
{% for family in site.data.lineage.pairings %}
<details class="lineage-family">
  <summary>
    <span class="lineage-pair">{{ family.pairing }}</span>
    <span class="lineage-preview">{% for animal in family.offspring %}{{ animal.id }}{% unless forloop.last %} · {% endunless %}{% endfor %}</span>
  </summary>

  <div class="lineage-family-body">
    {% if family.notes != "" %}<p class="lineage-note">{{ family.notes }}</p>{% endif %}
    {% if family.photos and family.photos.size > 0 %}
    <div class="lineage-gallery">
      {% for photo in family.photos %}<img src="{{ photo | relative_url }}" alt="{{ family.pairing }}">{% endfor %}
    </div>
    {% endif %}

    <div class="lineage-offspring">
    {% for animal in family.offspring %}
      <div class="lineage-record">
        {% if animal.photos and animal.photos.size > 0 %}
          <img class="lineage-thumb" src="{{ animal.photos[0] | relative_url }}" alt="{{ family.pairing }} {{ animal.id }}">
        {% endif %}
        <div class="lineage-record-copy">
          <strong>{{ animal.id }}</strong>
          <span>{{ animal.date }}{% if animal.sex != "" %} · {{ animal.sex }}{% endif %}</span>
          {% if animal.notes != "" %}<small>{{ animal.notes }}</small>{% endif %}
        </div>
      </div>
    {% endfor %}
    </div>
  </div>
</details>
{% endfor %}
</div>

<h2 class="lineage-section-title">Outside-source lineage</h2>
<div class="lineage-source-list">
{% for animal in site.data.lineage.outside_source %}
  <div class="lineage-source-record">
    {% if animal.photos and animal.photos.size > 0 %}<img class="lineage-thumb" src="{{ animal.photos[0] | relative_url }}" alt="{{ animal.lineage }}">{% endif %}
    <div>
      <strong>{{ animal.lineage }}</strong>
      <span>{{ animal.source }} · {{ animal.hatch_date }}</span>
      {% if animal.notes != "" %}<small>{{ animal.notes }}</small>{% endif %}
    </div>
  </div>
{% endfor %}
</div>
