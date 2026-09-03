---
layout: page
title: Observation Log
eyebrow: Dated records
description: Behaviour, development, breeding events, and the small details worth tracking over time.
permalink: /observations/
---
{% assign notes = site.observations | sort: "date" | reverse %}
{% if notes.size > 0 %}<div class="grid grid-3">{% for note in notes %}<a class="card" href="{{ note.url | relative_url }}"><div class="card-body"><p class="eyebrow">{{ note.date | date: "%Y.%m.%d" }}</p><h2 class="card-title">{{ note.title }}</h2>{% if note.summary %}<p class="card-summary">{{ note.summary }}</p>{% endif %}</div></a>{% endfor %}</div>{% else %}<div class="empty-state"><p>The notebooks are full. The website is catching up.</p></div>{% endif %}
