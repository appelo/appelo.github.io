---
layout: archive
title: "Group"
permalink: /group/
author_profile: true
---

{% include base_path %}

The group works on high order accurate numerical methods for differential
equations. We will have openings for both postdocs and PhD students --- please
[get in touch](mailto:appelo@vt.edu) if you are interested.

## Current members
{: .archive__subtitle}

{% for m in site.data.group.current %}
### {% if m.linkedin %}[{{ m.name }}]({{ m.linkedin }}){% else %}{{ m.name }}{% endif %}
{: .archive__item-title}

{{ m.role }}{% if m.affiliation %}, {{ m.affiliation }}{% endif %}{% if m.expected %} (expected {{ m.expected }}){% endif %}
{: .archive__item-excerpt}
{% if m.projects %}
{{ m.projects | strip }}
{: .archive__item-excerpt}
{% endif %}{% endfor %}

## Alumni
{: .archive__subtitle}

{% assign alumni = site.data.group.alumni | sort: "end" | reverse %}
{% for m in alumni %}
### {% if m.linkedin %}[{{ m.name }}]({{ m.linkedin }}){% else %}{{ m.name }}{% endif %}
{: .archive__item-title}

{{ m.role }}{% if m.institution %}, {{ m.institution }}{% endif %}{% if m.years %} ({{ m.years }}){% endif %}
{: .archive__item-excerpt}
{% if m.note %}
{{ m.note | strip }}
{: .archive__item-excerpt}
{% endif %}{% if m.projects %}
{{ m.projects | strip }}
{: .archive__item-excerpt}
{% endif %}{% if m.thesis %}
*{{ m.thesis }}*
{: .archive__item-excerpt}
{% endif %}{% if m.now %}
First job: {{ m.now }}
{: .archive__item-excerpt}
{% endif %}{% endfor %}
