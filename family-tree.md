---
layout: page
title: Family Tree
eyebrow: Visual lineage
description: Parent and offspring relationships across Alien Arboreal.
permalink: /family-tree/
---
<style>
.master-tree{display:grid;gap:1rem}
.master-family{padding:1rem;background:var(--panel);border:1px solid var(--line);border-radius:6px;overflow-x:auto}
.master-parents,.master-children{display:flex;justify-content:center;align-items:center;flex-wrap:wrap;gap:.5rem;min-width:320px}
.master-node{min-width:115px;max-width:190px;padding:.55rem .7rem;text-align:center;border:1px solid var(--line);border-radius:5px;background:rgba(0,0,0,.12);font-size:.82rem;font-weight:700}
.master-node a{color:inherit}
.master-node.missing{color:var(--muted)}
.master-node small{display:block;margin-top:.15rem;color:var(--muted);font:400 .62rem "Space Mono",monospace}
.master-cross{color:var(--acid);font-weight:700}
.master-stem{width:1px;height:20px;background:var(--moss);margin:0 auto}
.master-branch{height:1px;background:var(--moss);max-width:72%;min-width:90px;margin:0 auto 14px}
</style>

{% assign geckos = site.geckos | sort: "name" %}
{% assign seen_pairings = "|" %}
<div class="master-tree">
{% for seed in geckos %}
  {% if seed.parents %}
    {% assign seed_raw = seed.parents | replace: ' X ', '×' | replace: ' x ', '×' | replace: ',', '×' %}
    {% assign seed_parts = seed_raw | split: '×' %}
    {% capture seed_key_raw %}{% for part in seed_parts %}{{ part | strip | replace: '  ', ' ' | replace: '  ', ' ' | downcase }}{% unless forloop.last %}|||{% endunless %}{% endfor %}{% endcapture %}
    {% assign seed_key_parts = seed_key_raw | split: '|||' | sort %}
    {% capture seed_key %}|{% for part in seed_key_parts %}{{ part }}{% unless forloop.last %}|||{% endunless %}{% endfor %}|{% endcapture %}

    {% unless seen_pairings contains seed_key %}
      {% capture seen_pairings %}{{ seen_pairings }}{{ seed_key }}{% endcapture %}
      <section class="master-family">
        <div class="master-parents">
        {% for parent_name in seed_parts %}
          {% assign clean_parent = parent_name | strip | replace: '  ', ' ' | replace: '  ', ' ' %}
          {% assign parent_norm = clean_parent | downcase %}
          {% assign matched_parent = nil %}
          {% for candidate in geckos %}
            {% assign candidate_norm = candidate.name | strip | replace: '  ', ' ' | replace: '  ', ' ' | downcase %}
            {% if candidate_norm == parent_norm %}{% assign matched_parent = candidate %}{% break %}{% endif %}
          {% endfor %}
          <div class="master-node{% unless matched_parent %} missing{% endunless %}">{% if matched_parent %}<a href="{{ matched_parent.url | relative_url }}">{{ matched_parent.name }}</a>{% else %}{{ clean_parent }}{% endif %}</div>
          {% unless forloop.last %}<div class="master-cross">×</div>{% endunless %}
        {% endfor %}
        </div>
        <div class="master-stem"></div>
        <div class="master-branch"></div>
        <div class="master-children">
        {% for child in geckos %}
          {% if child.parents %}
            {% assign child_raw = child.parents | replace: ' X ', '×' | replace: ' x ', '×' | replace: ',', '×' %}
            {% assign child_parts = child_raw | split: '×' %}
            {% capture child_key_raw %}{% for part in child_parts %}{{ part | strip | replace: '  ', ' ' | replace: '  ', ' ' | downcase }}{% unless forloop.last %}|||{% endunless %}{% endfor %}{% endcapture %}
            {% assign child_key_parts = child_key_raw | split: '|||' | sort %}
            {% capture child_key %}|{% for part in child_key_parts %}{{ part }}{% unless forloop.last %}|||{% endunless %}{% endfor %}|{% endcapture %}
            {% if child_key == seed_key %}<div class="master-node"><a href="{{ child.url | relative_url }}">{{ child.name }}</a>{% if child.hatch_date %}<small>{{ child.hatch_date }}</small>{% endif %}</div>{% endif %}
          {% endif %}
        {% endfor %}
        </div>
      </section>
    {% endunless %}
  {% endif %}
{% endfor %}
</div>
