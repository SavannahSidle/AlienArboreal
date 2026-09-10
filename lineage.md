---
layout: page
title: Lineage
eyebrow: Family histories
description: Parentage and offspring across Alien Arboreal lines.
permalink: /lineage/
---
<style>
.lineage-list{border-top:1px solid var(--line);margin-top:.5rem}.lineage-family{margin:0;padding:0;border:0;border-bottom:1px solid var(--line);background:transparent}.lineage-family summary{display:grid;grid-template-columns:minmax(180px,1fr) 2fr;gap:1rem;align-items:center;padding:.7rem .2rem;cursor:pointer;list-style:none}.lineage-family summary::-webkit-details-marker{display:none}.lineage-family summary:after{content:"+";grid-column:3;color:var(--acid);font:400 1rem "Space Mono",monospace}.lineage-family[open] summary:after{content:"−"}.lineage-pair{font-weight:700;color:var(--ink)}.lineage-pair a{color:var(--ink);text-decoration-color:var(--moss)}.lineage-pair a:hover{color:var(--acid)}.lineage-preview{font:400 .7rem "Space Mono",monospace;color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.lineage-family-body{padding:.15rem 0 .8rem}.lineage-note{margin:.2rem 0 .55rem;color:var(--muted);font-size:.85rem}.lineage-offspring{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:.35rem;margin:0}.lineage-record{display:flex;gap:.55rem;align-items:center;min-height:42px;padding:.45rem .55rem;background:var(--panel);border:1px solid var(--line);border-radius:4px}.lineage-record-copy{display:flex;flex-wrap:wrap;align-items:baseline;gap:.1rem .5rem;min-width:0}.lineage-record strong{font-size:.86rem}.lineage-record span,.lineage-source-record span{color:var(--muted);font:400 .66rem "Space Mono",monospace}.lineage-record small,.lineage-source-record small{display:block;flex-basis:100%;color:#c6d2c8;font-size:.72rem;line-height:1.35}.lineage-thumb{width:42px;height:42px;flex:0 0 42px;object-fit:cover;border-radius:3px;border:1px solid var(--line)}.lineage-gallery{display:flex;gap:.4rem;margin:.4rem 0 .65rem;overflow-x:auto}.lineage-gallery img{width:82px;height:62px;flex:0 0 auto;object-fit:cover}.lineage-section-title{margin:2rem 0 .5rem!important;font-size:1.15rem}.lineage-source-list{border-top:1px solid var(--line)}.lineage-source-record{display:flex;gap:.6rem;align-items:center;padding:.55rem .2rem;border-bottom:1px solid var(--line)}.lineage-source-record>div{display:flex;flex-wrap:wrap;gap:.1rem .65rem;align-items:baseline}.lineage-source-record strong{font-size:.86rem}
@media(max-width:760px){.lineage-family summary{grid-template-columns:1fr auto;gap:.15rem .5rem;padding:.65rem .1rem}.lineage-pair{grid-column:1}.lineage-preview{grid-column:1;grid-row:2}.lineage-family summary:after{grid-column:2;grid-row:1/3}.lineage-offspring{grid-template-columns:repeat(2,minmax(0,1fr))}.lineage-record{padding:.4rem}.lineage-record-copy{display:block}.lineage-record span{display:block}.lineage-record small{margin-top:.15rem}}
</style>

<div class="lineage-list">
{% for family in site.data.lineage.pairings %}
{% assign parents = family.pairing | split: ' × ' %}
<details class="lineage-family">
  <summary>
    <span class="lineage-pair"><a href="{{ '/geckos/' | append: (parents[0] | slugify) | append: '/' | relative_url }}">{{ parents[0] }}</a> × <a href="{{ '/geckos/' | append: (parents[1] | slugify) | append: '/' | relative_url }}">{{ parents[1] }}</a></span>
    <span class="lineage-preview">{% for animal in family.offspring %}{{ animal.id }}{% unless forloop.last %} · {% endunless %}{% endfor %}</span>
  </summary>
  <div class="lineage-family-body">
    {% if family.notes != "" %}<p class="lineage-note">{{ family.notes }}</p>{% endif %}
    {% if family.photos and family.photos.size > 0 %}<div class="lineage-gallery">{% for photo in family.photos %}<img src="{{ photo | relative_url }}" alt="{{ family.pairing }}">{% endfor %}</div>{% endif %}
    <div class="lineage-offspring">
    {% for animal in family.offspring %}
      <div class="lineage-record">
        {% if animal.photos and animal.photos.size > 0 %}<img class="lineage-thumb" src="{{ animal.photos[0] | relative_url }}" alt="{{ family.pairing }} {{ animal.id }}">{% endif %}
        <div class="lineage-record-copy"><strong>{{ animal.id }}</strong><span>{{ animal.date }}{% if animal.sex != "" %} · {{ animal.sex }}{% endif %}</span>{% if animal.notes != "" %}<small>{{ animal.notes }}</small>{% endif %}</div>
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
    <div><strong>{{ animal.lineage }}</strong><span>{{ animal.source }} · {{ animal.hatch_date }}</span>{% if animal.notes != "" %}<small>{{ animal.notes }}</small>{% endif %}</div>
  </div>
{% endfor %}
</div>
