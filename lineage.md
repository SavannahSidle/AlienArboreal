---
layout: page
title: Lineage
eyebrow: Family histories
description: Parentage, offspring, and genetic relationships across Alien Arboreal lines.
permalink: /lineage/
---
This is a living record of family relationships across generations. Dates or identities that are still being reconciled are marked rather than guessed.

{% for family in site.data.lineage.pairings %}
<section class="lineage-family">
  <h2>{{ family.pairing }}</h2>
  {% if family.notes != "" %}<p class="lineage-note">{{ family.notes }}</p>{% endif %}

  {% if family.photos and family.photos.size > 0 %}
  <div class="lineage-gallery">
    {% for photo in family.photos %}<img src="{{ photo | relative_url }}" alt="{{ family.pairing }}">{% endfor %}
  </div>
  {% endif %}

  <div class="lineage-offspring">
  {% for animal in family.offspring %}
    <article class="lineage-record">
      {% if animal.photos and animal.photos.size > 0 %}
      <div class="lineage-gallery">
        {% for photo in animal.photos %}<img src="{{ photo | relative_url }}" alt="{{ family.pairing }} {{ animal.id }}">{% endfor %}
      </div>
      {% endif %}
      <h3>{{ animal.id }}</h3>
      <p class="card-meta">{{ animal.date }}{% if animal.sex != "" %} · {{ animal.sex }}{% endif %}</p>
      {% if animal.notes != "" %}<p>{{ animal.notes }}</p>{% endif %}
    </article>
  {% endfor %}
  </div>
</section>
{% endfor %}

## Outside-source lineage

These records preserve known parentage for animals originating outside Alien Arboreal.

{% for animal in site.data.lineage.outside_source %}
<section class="lineage-record">
  {% if animal.photos and animal.photos.size > 0 %}
  <div class="lineage-gallery">
    {% for photo in animal.photos %}<img src="{{ photo | relative_url }}" alt="{{ animal.lineage }}">{% endfor %}
  </div>
  {% endif %}
  <h3>{{ animal.lineage }}</h3>
  <p class="card-meta">{{ animal.source }} · {{ animal.hatch_date }}</p>
  {% if animal.notes != "" %}<p>{{ animal.notes }}</p>{% endif %}
</section>
{% endfor %}
