---
layout: page
title: Lineage
eyebrow: Family histories
description: Parentage and offspring across Alien Arboreal lines.
permalink: /lineage/
---
<style>
.lineage-list{border-top:1px solid var(--line);margin-top:.5rem}
.prose a.btn-primary{color:var(--dark)}
.lineage-family{margin:0;padding:0;border:0;border-bottom:1px solid var(--line);background:transparent}
.lineage-family summary{display:grid;grid-template-columns:minmax(180px,1fr) 2fr auto;gap:1rem;align-items:center;padding:.7rem .2rem;cursor:pointer;list-style:none}
.lineage-family summary::-webkit-details-marker{display:none}
.lineage-family summary:after{content:"+";color:#10140f;background:var(--acid);font:700 3.25rem/1 "Space Mono",monospace;width:3.75rem;height:3.75rem;min-width:3.75rem;display:grid;place-items:center;border-radius:5px;text-align:center;transition:transform .15s ease,background .15s ease}.lineage-family summary:hover:after{background:#d8ff45;transform:scale(1.04)}.lineage-family summary:focus-visible{outline:3px solid var(--acid);outline-offset:4px;border-radius:4px}
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
.tree-node small{display:block;margin-top:.15rem;color:var(--muted);font:400 .63rem "Space Mono",monospace}.tree-photo{height:66px;margin:-.1rem -.15rem .4rem;display:grid;place-items:center;overflow:hidden;border:1px dashed var(--line);border-radius:3px;background:rgba(255,255,255,.025);color:var(--muted);font:400 .58rem "Space Mono",monospace;text-transform:uppercase}.tree-photo img{width:100%;height:100%;object-fit:cover}
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
              <div class="tree-node{% unless matched_parent %} missing{% endunless %}">{% assign parent_photo = matched_parent.image %}{% if parent_photo == nil and matched_parent.photos and matched_parent.photos.size > 0 %}{% assign parent_photo = matched_parent.photos[0] %}{% endif %}<div class="tree-photo">{% if parent_photo %}<img src="{{ parent_photo | relative_url }}" alt="" loading="lazy">{% else %}Photo placeholder{% endif %}</div>{% if matched_parent %}<a href="{{ matched_parent.url | relative_url }}">{{ matched_parent.name }}</a>{% else %}{{ clean_parent }}{% endif %}</div>
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
                  <div class="tree-node">{% assign child_photo = child.image %}{% if child_photo == nil and child.photos and child.photos.size > 0 %}{% assign child_photo = child.photos[0] %}{% endif %}<div class="tree-photo">{% if child_photo %}<img src="{{ child_photo | relative_url }}" alt="" loading="lazy">{% else %}Photo placeholder{% endif %}</div><a href="{{ child.url | relative_url }}">{{ child.name }}</a>{% if child.hatch_date %}<small>{{ child.hatch_date }}</small>{% endif %}{% if child.sex %}<small>{{ child.sex }}</small>{% endif %}</div>
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


{% for pairing in site.data.lineage.pairings %}
  {% assign data_parts = pairing.pairing | replace: ' X ', '×' | replace: ' x ', '×' | split: '×' %}
  {% capture data_key_raw %}{% for part in data_parts %}{{ part | strip | downcase }}{% unless forloop.last %}|||{% endunless %}{% endfor %}{% endcapture %}
  {% assign data_key_parts = data_key_raw | split: '|||' | sort %}
  {% capture data_key %}|{% for part in data_key_parts %}{{ part }}{% unless forloop.last %}|||{% endunless %}{% endfor %}|{% endcapture %}
  {% unless seen_pairings contains data_key %}
    {% capture seen_pairings %}{{ seen_pairings }}{{ data_key }}{% endcapture %}
    <details class="lineage-family">
      <summary>
        <span class="lineage-pair">{{ pairing.pairing | escape }}</span>
        <span class="lineage-preview">{% for offspring in pairing.offspring %}{% unless forloop.first %} · {% endunless %}{{ offspring.id | escape }}{% endfor %}</span>
      </summary>
      <div class="lineage-family-body">
        <div class="family-tree">
          <div class="tree-parents">
          {% for parent_name in data_parts %}
            {% assign clean_parent = parent_name | strip %}
            {% assign parent_norm = clean_parent | downcase %}
            {% assign matched_parent = nil %}
            {% for candidate in geckos %}
              {% assign candidate_norm = candidate.name | strip | downcase %}
              {% if candidate_norm == parent_norm %}{% assign matched_parent = candidate %}{% break %}{% endif %}
            {% endfor %}
            {% assign parent_photo = matched_parent.image %}
            {% if parent_photo == nil and matched_parent.photos and matched_parent.photos.size > 0 %}{% assign parent_photo = matched_parent.photos[0] %}{% endif %}
            <div class="tree-node{% unless matched_parent %} missing{% endunless %}">
              <div class="tree-photo">{% if parent_photo %}<img src="{{ parent_photo | relative_url }}" alt="" loading="lazy">{% else %}Photo placeholder{% endif %}</div>
              {% if matched_parent %}<a href="{{ matched_parent.url | relative_url }}">{{ matched_parent.name }}</a>{% else %}{{ clean_parent | escape }}{% endif %}
            </div>
            {% unless forloop.last %}<div class="tree-cross">×</div>{% endunless %}
          {% endfor %}
          </div>
          <div class="tree-stem"></div><div class="tree-branch"></div>
          <div class="tree-children">
          {% for offspring in pairing.offspring %}
            <div class="tree-node">
              <div class="tree-photo">{% assign offspring_photo = offspring.photos[0] %}{% if offspring_photo %}<img src="{{ offspring_photo | relative_url }}" alt="" loading="lazy">{% else %}Photo placeholder{% endif %}</div>
              {{ offspring.id | escape }}
              {% if offspring.date %}<small>{{ offspring.date | escape }}</small>{% endif %}
              {% if offspring.sex %}<small>{{ offspring.sex | escape }}</small>{% endif %}
              {% if offspring.notes %}<small>{{ offspring.notes | escape }}</small>{% endif %}
            </div>
          {% endfor %}
          </div>
        </div>
        {% if pairing.notes %}<p>{{ pairing.notes | escape }}</p>{% endif %}
      </div>
    </details>
  {% endunless %}
{% endfor %}

{% for history in site.data.lineage.lineage_records %}
<details class="lineage-family">
  <summary>
    <span class="lineage-pair">{{ history.parents | escape }}</span>
    <span class="lineage-preview">{% if history.traits %}{{ history.traits | escape }}{% endif %}{% if history.hatch_date %}{% if history.traits %} · {% endif %}{{ history.hatch_date | escape }}{% endif %}</span>
  </summary>
  <div class="lineage-family-body">
    <div class="family-tree">
      <div class="tree-parents">
      {% assign history_parents = history.parents | split: '×' %}
      {% for parent_name in history_parents %}
        <div class="tree-node missing">
          <div class="tree-photo tree-photo-placeholder" aria-label="Photo placeholder">Photo placeholder</div>
          {{ parent_name | strip | escape }}
        </div>
        {% unless forloop.last %}<div class="tree-cross">×</div>{% endunless %}
      {% endfor %}
      </div>
      <div class="tree-stem"></div><div class="tree-branch"></div>
      <div class="tree-children">
        <div class="tree-node">
          <div class="tree-photo tree-photo-placeholder" aria-label="Photo placeholder">Photo placeholder</div>
          Offspring
          {% if history.traits %}<small>{{ history.traits | escape }}</small>{% endif %}
          {% if history.hatch_date %}<small>{{ history.hatch_date | escape }}</small>{% endif %}
          {% if history.source %}<small>{{ history.source | escape }}</small>{% endif %}
        </div>
      </div>
    </div>
    {% if history.notes %}<p>{{ history.notes | escape }}</p>{% endif %}
  </div>
</details>
{% endfor %}
</div>

