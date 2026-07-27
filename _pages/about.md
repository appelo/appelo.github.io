---
permalink: /
title: "Daniel Appelö"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% include base_path %}

I am a Professor in the [Department of Mathematics](https://math.vt.edu) and the
Computational Modeling and Data Analytics (CMDA) program at Virginia Tech. My
group develops fast, stable and accurate numerical algorithms for the
approximation of differential equations arising in engineering and the natural
sciences.

Much of our work is about waves --- acoustic, elastic and electromagnetic --- in
both the time and the frequency domain, and about what it takes to make high
order methods provably stable rather than merely accurate on smooth problems.
More recently we have also been working on quantum computing.

Our most ambitious current effort, running over the next five to seven years, is
**Quantum Digital Twins** (QDTs): rigorous, self-correcting, bi-directional
replicas of quantum computing hardware, together with the structure preserving
and scalable numerical methods they rest on. A QDT couples three layers --- the
quantum dynamics of the qubits (Schrödinger and Lindblad equations), the
electromagnetic design of the device (Maxwell and Helmholtz equations), and
quantum error correction --- into a single multi-fidelity framework. The
framework is learned from measurements through Bayesian experimental design and
optimal control, and in return it certifies and drives the physical device.
Making this work rests on two pillars of numerical analysis that are worth
pursuing in their own right: fast, scalable frequency domain wave solvers, and
structure preserving low rank and tensor network integrators for high
dimensional open quantum systems --- mathematical technology whose value extends
well beyond quantum computing.

## Research
{: .archive__subtitle}

* **Wave propagation.** High order accurate methods for acoustic, elastic and
  electromagnetic waves, built so that stability follows from a discrete energy
  estimate. This includes energy based discontinuous Galerkin methods, Hermite
  and Hermite-Taylor methods, and summation-by-parts finite differences.
* **Frequency domain solvers.** The WaveHoltz iteration solves the Helmholtz
  equation by time domain wave solves, turning an indefinite problem into a
  positive definite one that parallelizes and scales. Related work covers
  elastic and electromagnetic waves, overset grids, and eigenvalue computation.
* **Quantum computing.** Structure preserving methods for the Schrödinger and
  Lindblad equations --- completely positive and trace preserving integrators in
  particular --- together with quantum optimal control, quantum error
  correction, and the Bayesian characterization that ties a digital twin back to
  the device it models.
* **Low rank and tensor methods.** Adaptive low rank time stepping, low rank
  Anderson acceleration, and tensor network integrators for the high dimensional
  problems that open quantum systems and matrix differential equations give
  rise to.
* **Unbounded domains.** Artificial boundary conditions --- perfectly matched
  layers and local high order radiation conditions --- for problems posed on
  unbounded domains.

See the [publications]({{ base_path }}/publications/) page for the full list.

## Openings
{: .archive__subtitle}

<!-- REVIEW THIS BOX: remove or update once these positions are filled. -->

**We will have openings for both Postdocs and PhD students.** Please
[contact me](mailto:appelo@vt.edu) to learn more, and see the
[group]({{ base_path }}/group/) page for who you would be working with.
{: .notice--info}

## Group
{: .archive__subtitle}

The group currently includes two postdocs and four PhD students at Virginia Tech
and Michigan State. Former members have gone on to faculty positions at CSU Long
Beach, HKUST and UT Dallas, and to postdocs at Los Alamos, the Courant Institute
and Arizona State --- the [group]({{ base_path }}/group/) page has the full
roster.
