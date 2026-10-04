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
.lineage-family summary{display:grid;grid-template-columns:minmax(180px,1fr) 2fr auto;gap:1rem;align-items:center;padding:.7rem .2rem;cursor:pointer;list-style:none}
.lineage-family summary::-webkit-details-marker{display:none}
.lineage-family summary:after{content:"+";color:var(--acid);font:400 1rem "Space Mono",monospace}
.lineage-family[open] summary:after{content:"−"}
.lineage-pair{font-weight:700;color:var(--ink)}
.lineage-pair a,.tree-node a{color:inherit;text-decoration-color:var(--moss)}
.lineage-pair a:hover,.tree-node a:hover{color:var(--acid)}
.lineage-preview{font:400 .7rem "Space Mono",monospace;color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.lineage-family-body{padding:.15rem 0 .9rem}
.family-tree{margin:.55rem 0 .4rem;padding:.9rem;background:var(--panel);border:1px solid var(--line);border-radius:6px;overflow-x:auto}
.tree-parents,.tree-children{display:flex;justify-content:center;align-items:center;flex-wrap:wrap;gap:.45rem;min-width:320px}
.tree-node{min-width:110px;max-width:190px;padding:.5rem .7rem;text-align:center;border:1px solid var(--line);border-radius:5px;background:rgba(0,0,0,.12);font-size:.82rem;font-weight:700}
.tree-node.missing{color:var(--muted)}
.tree-node small{display:block;margin-top:.15rem;color:var(--muted);font:400 .63rem "Space Mono",monospace}
.tree-cross{color:var(--acid);font:700 1rem "Space Mono",monospace}
.tree-stem{width:1px;height:18px;background:var(--moss);margin:0 auto}
.tree-branch{height:1px;background:var(--moss);margin:0 auto 12px;max-width:72%;min-width:80px}
@media(max-width:760px){
  .lineage-family summary{grid-template-columns:1fr auto;gap:.15rem .5rem}
  .lineage-pair,.lineage-preview{grid-column:1}
  .lineage-family summary:after{grid-column:2;grid-row:1/3}
}
</style>

{% assign geckos = site.geckos | sort: "name" %}
{% assign seen_pairings = "|" %}

<section class="section-block" style="margin-bottom:1.75rem">
  <p class="eyebrow">Visual lineage</p>
  <h2>Family Tree</h2>
  <p>Follow generations visually from parents to offspring.</p>
  <a class="btn btn-primary" href="{{ '/family-tree/' | relative_url }}">Open Family Tree</a>
</section>

<h2>Family Histories</h2>
<div class="lineage-list">
{% for seed in geckos %}
  {% if seed.parents %}
    {% assign seed_raw = seed.parents | replace: ' X ', '×' | replace: ' x ', '×' | replace: ',', '×' %}
    {% assign seed_parts = seed_raw | split: '×' %}
    {% capture seed_key_raw %}{% for part in seed_parts %}{{ part | strip | replace: '  ', ' ' | replace: '  ', ' ' | downcase }}{% unless forloop.last %}|||{% endunless %}{% endfor %}{% endcapture %}
    {% assign seed_key_parts = seed_key_raw | split: '|||' | sort %}
    {% capture seed_key %}|{% for part in seed_key_parts %}{{ part }}{% unless forloop.last %}|||{% endunless %}{% endfor %}|{% endcapture %}

    {% unless seen_pairings contains seed_key %}
      {% capture seen_pairings %}{{ seen_pairings }}{{ seed_key }}{% endcapture %}

      <details class="lineage-family">
        <summary>
          <span class="lineage-pair">
          {% for parent_name in seed_parts %}
            {% assign clean_parent = parent_name | strip | replace: '  ', ' ' | replace: '  ', ' ' %}
            {% assign parent_norm = clean_parent | downcase %}
            {% assign matched_parent = nil %}
            {% for candidate in geckos %}
              {% assign candidate_norm = candidate.name | strip | replace: '  ', ' ' | replace: '  ', ' ' | downcase %}
              {% if candidate_norm == parent_norm %}{% assign matched_parent = candidate %}{% break %}{% endif %}
            {% endfor %}
            {% if matched_parent %}<a href="{{ matched_parent.url | relative_url }}">{{ matched_parent.name }}</a>{% else %}{{ clean_parent }}{% endif %}{% unless forloop.last %} × {% endunless %}
          {% endfor %}
          </span>
          <span class="lineage-preview">
          {% assign first_child = true %}
          {% for child in geckos %}
            {% if child.parents %}
              {% assign child_raw = child.parents | replace: ' X ', '×' | replace: ' x ', '×' | replace: ',', '×' %}
              {% assign child_parts = child_raw | split: '×' %}
              {% capture child_key_raw %}{% for part in child_parts %}{{ part | strip | replace: '  ', ' ' | replace: '  ', ' ' | downcase }}{% unless forloop.last %}|||{% endunless %}{% endfor %}{% endcapture %}
              {% assign child_key_parts = child_key_raw | split: '|||' | sort %}
              {% capture child_key %}|{% for part in child_key_parts %}{{ part }}{% unless forloop.last %}|||{% endunless %}{% endfor %}|{% endcapture %}
              {% if child_key == seed_key %}{% unless first_child %} · {% endunless %}{{ child.name }}{% assign first_child = false %}{% endif %}
            {% endif %}
          {% endfor %}
          </span>
        </summary>

        <div class="lineage-family-body">
          <div class="family-tree">
            <div class="tree-parents">
            {% for parent_name in seed_parts %}
              {% assign clean_parent = parent_name | strip | replace: '  ', ' ' | replace: '  ', ' ' %}
              {% assign parent_norm = clean_parent | downcase %}
              {% assign matched_parent = nil %}
              {% for candidate in geckos %}
                {% assign candidate_norm = candidate.name | strip | replace: '  ', ' ' | replace: '  ', ' ' | downcase %}
                {% if candidate_norm == parent_norm %}{% assign matched_parent = candidate %}{% break %}{% endif %}
              {% endfor %}
              <div class="tree-node{% unless matched_parent %} missing{% endunless %}">{% if matched_parent %}<a href="{{ matched_parent.url | relative_url }}">{{ matched_parent.name }}</a>{% else %}{{ clean_parent }}{% endif %}</div>
              {% unless forloop.last %}<div class="tree-cross">×</div>{% endunless %}
            {% endfor %}
            </div>
            <div class="tree-stem"></div>
            <div class="tree-branch"></div>
            <div class="tree-children">
            {% for child in geckos %}
              {% if child.parents %}
                {% assign child_raw = child.parents | replace: ' X ', '×' | replace: ' x ', '×' | replace: ',', '×' %}
                {% assign child_parts = child_raw | split: '×' %}
                {% capture child_key_raw %}{% for part in child_parts %}{{ part | strip | replace: '  ', ' ' | replace: '  ', ' ' | downcase }}{% unless forloop.last %}|||{% endunless %}{% endfor %}{% endcapture %}
                {% assign child_key_parts = child_key_raw | split: '|||' | sort %}
                {% capture child_key %}|{% for part in child_key_parts %}{{ part }}{% unless forloop.last %}|||{% endunless %}{% endfor %}|{% endcapture %}
                {% if child_key == seed_key %}
                  <div class="tree-node"><a href="{{ child.url | relative_url }}">{{ child.name }}</a>{% if child.hatch_date %}<small>{{ child.hatch_date }}</small>{% endif %}</div>
                {% endif %}
              {% endif %}
            {% endfor %}
            </div>
          </div>
        </div>
      </details>
    {% endunless %}
  {% endif %}
{% endfor %}
</div>

