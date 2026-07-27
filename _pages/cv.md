---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* Ph.D. in Numerical Analysis, NADA, KTH Royal Institute of Technology, 2005
  * Thesis: *Absorbing Layers and Non-Reflecting Boundary Conditions for Wave
    Propagation Problems*
  * Advisor: Gunilla Kreiss
* Licentiate, KTH Royal Institute of Technology, 2003
* M.S. in Numerical Analysis, KTH Royal Institute of Technology, 2000

Positions
======
* Professor, Department of Mathematics and CMDA, Virginia Tech
* Michigan State University, CMSE and Department of Mathematics
* University of Colorado Boulder
* University of New Mexico, Albuquerque
  * Hans Werthen Prize postdoctoral researcher, working with Tom Hagstrom on
    perfectly matched layer models for hyperbolic-parabolic systems and on
    Hermite methods
* Postdoc, Mechanical Engineering, Caltech, with Tim Colonius
* Lawrence Livermore National Laboratory, Applied Mathematics group, Center for
  Applied Scientific Computing
  * Part of the Serpentine project, developing massively parallel numerical
    methods for seismology with Anders Petersson and Bjorn Sjögreen, and high
    order accurate embedded boundary methods for the wave equation

<!-- TODO: add dates and ranks to the positions above; add Awards, Service,
     Grants and Students sections. -->

Publications
======

{%- for post in site.publications reversed %}
* [{{ post.title }}]({{ base_path }}{{ post.url }}){% if post.venue %}. {{ post.citation }}{% endif %}
{%- endfor %}

Talks
======

{%- for post in site.talks reversed %}
* [{{ post.title }}]({{ base_path }}{{ post.url }}){% if post.venue %}. {{ post.type }} at {{ post.venue }}, {{ post.location }}{% endif %}
{%- endfor %}

Teaching
======

{%- for post in site.teaching reversed %}
* [{{ post.title }}]({{ base_path }}{{ post.url }}){% if post.venue %}. {{ post.type }}, {{ post.venue }}{% endif %}
{%- endfor %}
