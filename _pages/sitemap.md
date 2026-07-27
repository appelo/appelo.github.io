---
layout: archive
title: "Sitemap"
permalink: /sitemap/
author_profile: true
---

{% include base_path %}

A list of all the pages found on the site. For you robots out there, there is an
[XML version]({{ base_path }}/sitemap.xml) available for digesting as well.

## Pages
{: .archive__subtitle}

{% for post in site.pages %}
{% include archive-single.html %}
{% endfor %}

{% for collection in site.collections %}
{% unless collection.output == false or collection.label == "posts" %}
## {{ collection.label }}
{: .archive__subtitle}

{% for post in collection.docs %}
{% include archive-single.html %}
{% endfor %}
{% endunless %}
{% endfor %}
