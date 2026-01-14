---
layout: default
title: Recipes
---

# Recipes

{% for page in site.pages %}
{% if page.url contains '/recipes/' and page.url != '/recipes/' %}
- [{{ page.title }}]({{ page.url }})
{% endif %}
{% endfor %}
