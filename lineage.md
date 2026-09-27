---
layout: page
title: Lineage
eyebrow: Family histories
description: Parentage and offspring across Alien Arboreal lines.
permalink: /lineage/
---
<style>
.lineage-list{border-top:1px solid var(--line);margin-top:.5rem}
.lineage-family{margin:0;padding:0;border:0;border-bottom:1px solid var(--line);background:transparent}
.lineage-family summary{display:grid;grid-template-columns:minmax(180px,1fr) 2fr;gap:1rem;align-items:center;padding:.7rem .2rem;cursor:pointer;list-style:none}
.lineage-family summary::-webkit-details-marker{display:none}
.lineage-family summary:after{content:"+";grid-column:3;color:var(--acid);font:400 1rem "Space Mono",monospace}
.lineage-family[open] summary:after{content:"−"}
.lineage-pair{font-weight:700;color:var(--ink)}
.lineage-pair a,.tree-node a{color:inherit;text-decoration-color:var(--moss)}
.lineage-pair a:hover,.tree-node a:hover{color:var(--acid)}
.lineage-preview{font:400 .7rem "Space Mono",monospace;color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.lineage-family-body{padding:.15rem 0 .9rem}
.lineage-note{margin:.2rem 0 .55rem;color:var(--muted);font-size:.85rem}
.lineage-offspring{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:.35rem;margin:.75rem 0 0}
.lineage-record{display:flex;gap:.55rem;align-items:center;min-height:42px;padding:.45rem .55rem;background:var(--panel);border:1px solid var(--line);border-radius:4px}
.lineage-record-copy{display:flex;flex-wrap:wrap;align-items:baseline;gap:.1rem .5rem;min-width:0}
.lineage-record strong{font-size:.86rem}
.lineage-record span{color:var(--muted);font:400 .66rem "Space Mono",monospace}
.lineage-record small{display:block;flex-basis:100%;color:#c6d2c8;font-size:.72rem;line-height:1.35}
.lineage-thumb{width:42px;height:42px;flex:0 0 42px;object-fit:cover;border-radius:3px;border:1px solid var(--line)}
.lineage-gallery{display:flex;gap:.4rem;margin:.4rem 0 .65rem;overflow-x:auto}
.lineage-gallery img{width:82px;height:62px;flex:0 0 auto;object-fit:cover}
.lineage-section-title{margin:2rem 0 .5rem!important;font-size:1.15rem}
.family-tree{margin:.55rem 0 .4rem;padding:.9rem;background:var(--panel);border:1px solid var(--line);border-radius:6px;overflow-x:auto}
.tree-parents{display:flex;justify-content:center;align-items:center;gap:.5rem;min-width:360px}
.tree-node{min-width:120px;max-width:190px;padding:.5rem .7rem;text-align:center;border:1px solid var(--line);border-radius:5px;background:rgba(0,0,0,.12);font-size:.82rem;font-weight:700}
.tree-node small{display:block;margin-top:.15rem;color:var(--muted);font:400 .63rem "Space Mono",monospace}
.tree-cross{color:var(--acid);font:700 1rem "Space Mono",monospace}
.tree-stem{width:1px;height:18px;background:var(--moss);margin:0 auto}
.tree-branch{height:1px;background:var(--moss);margin:0 auto 12px;max-width:72%;min-width:80px}
.tree-children{display:flex;justify-content:center;flex-wrap:wrap;gap:.45rem;min-width:360px}
.tree-child{min-width:105px;font-weight:600}
.tree-child small{font-weight:400}
.lineage-records{margin-top:2rem}
.lineage-record-family{padding:.9rem 0;border-top:1px solid var(--line)}
.lineage-record-meta{display:flex;flex-wrap:wrap;gap:.4rem .8rem;margin:.5rem 0 0;color:var(--muted);font:400 .68rem "Space Mono",monospace}
@media(max-width:760px){
  .lineage-family summary{grid-template-columns:1fr auto;gap:.15rem .5rem;padding:.65rem .1rem}
  .lineage-pair{grid-column:1}
  .lineage-preview{grid-column:1;grid-row:2}
  .lineage-family summary:after{grid-column:2;grid-row:1/3}
  .lineage-offspring{grid-template-columns:repeat(2,minmax(0,1fr))}
  .lineage-record{padding:.4rem}
  .lineage-record-copy{display:block}
  .lineage-record span{display:block}
  .lineage-record small{margin-top:.15rem}
}
</style>

<div class="lineage-list">
{% for family in site.data.lineage.pairings %}
{% assign parents = family.pairing | split: ' × ' %}
{% assign p1 = site.geckos | where: "name", parents[0] | first %}
{% assign p2 = site.geckos | where: "name", parents[1] | first %}
<details class="lineage-family">
  <summary>
    <span class="lineage-pair">{% if p1 %}<a href="{{ p1.url | relative_url }}">{{ parents[0] }}</a>{% else %}{{ parents[0] }}{% endif %} × {% if p2 %}<a href="{{ p2.url | relative_url }}">{{ parents[1] }}</a>{% else %}{{ parents[1] }}{% endif %}</span>
    <span class="lineage-preview">{% for animal in family.offspring %}{{ animal.id }}{% unless forloop.last %} · {% endunless %}{% endfor %}</span>
  </summary>
  <div class="lineage-family-body">
    {% if family.notes != "" %}<p class="lineage-note">{{ family.notes }}</p>{% endif %}
    {% if family.photos and family.photos.size > 0 %}<div class="lineage-gallery">{% for photo in family.photos %}<img src="{{ photo | relative_url }}" alt="{{ family.pairing }}">{% endfor %}</div>{% endif %}

    <div class="family-tree" aria-label="Family tree for {{ family.pairing }}">
      <div class="tree-parents">
        <div class="tree-node">{% if p1 %}<a href="{{ p1.url | relative_url }}">{{ parents[0] }}</a>{% else %}{{ parents[0] }}{% endif %}</div>
        <div class="tree-cross">×</div>
        <div class="tree-node">{% if p2 %}<a href="{{ p2.url | relative_url }}">{{ parents[1] }}</a>{% else %}{{ parents[1] }}{% endif %}</div>
      </div>
      <div class="tree-stem"></div>
      <div class="tree-branch"></div>
      <div class="tree-children">
      {% if family.linked_offspring %}{% for linked in family.linked_offspring %}{% assign linked_profile = site.geckos | where: "name", linked.name | first %}<div class="tree-node tree-child">{% if linked_profile %}<a href="{{ linked_profile.url | relative_url }}">{{ linked.name }}</a>{% else %}{{ linked.name }}{% endif %}<small>profile</small></div>{% endfor %}{% endif %}
      {% for animal in family.offspring %}
        <div class="tree-node tree-child">{{ animal.id }}{% if animal.date != "" %}<small>{{ animal.date }}</small>{% endif %}{% if animal.sex != "" %}<small>{{ animal.sex }}</small>{% endif %}</div>
      {% endfor %}
      </div>
    </div>

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

{% if site.data.lineage.lineage_records and site.data.lineage.lineage_records.size > 0 %}
<div class="lineage-records">
<h2 class="lineage-section-title">Additional family histories</h2>
{% for record in site.data.lineage.lineage_records %}
{% assign parents = record.parents | split: ' × ' %}
{% assign p1 = site.geckos | where: "name", parents[0] | first %}
{% assign p2 = site.geckos | where: "name", parents[1] | first %}
<div class="lineage-record-family">
  <div class="lineage-pair">{% if p1 %}<a href="{{ p1.url | relative_url }}">{{ parents[0] }}</a>{% else %}{{ parents[0] }}{% endif %} × {% if p2 %}<a href="{{ p2.url | relative_url }}">{{ parents[1] }}</a>{% else %}{{ parents[1] }}{% endif %}</div>
  <div class="family-tree" aria-label="Family tree for {{ record.parents }}">
    <div class="tree-parents">
      <div class="tree-node">{% if p1 %}<a href="{{ p1.url | relative_url }}">{{ parents[0] }}</a>{% else %}{{ parents[0] }}{% endif %}</div>
      <div class="tree-cross">×</div>
      <div class="tree-node">{% if p2 %}<a href="{{ p2.url | relative_url }}">{{ parents[1] }}</a>{% else %}{{ parents[1] }}{% endif %}</div>
    </div>
    <div class="tree-stem"></div>
    <div class="tree-branch"></div>
    <div class="tree-children">
      <div class="tree-node tree-child">{% if record.traits != "" %}{{ record.traits }}{% else %}Offspring{% endif %}{% if record.hatch_date != "" %}<small>{{ record.hatch_date }}</small>{% endif %}</div>
    </div>
  </div>
  <div class="lineage-record-meta">{% if record.source != "" %}<span>{{ record.source }}</span>{% endif %}{% if record.traits != "" %}<span>{{ record.traits }}</span>{% endif %}{% if record.hatch_date != "" %}<span>{{ record.hatch_date }}</span>{% endif %}</div>
  {% if record.notes != "" %}<p class="lineage-note">{{ record.notes }}</p>{% endif %}
</div>
{% endfor %}
</div>
{% endif %}
