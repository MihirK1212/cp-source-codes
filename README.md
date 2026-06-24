---
layout: default
permalink: /
---

# CP & DSA source codes

Competitive programming notes and solutions organized by topic. Each markdown file under [`src/questions/`](src/questions/README.html) holds a problem write-up and/or solution sketch.

**GitHub Pages:** This site is built with [Jekyll](https://jekyllrb.com/) on [GitHub Pages](https://docs.github.com/pages). Problem pages are published as **HTML** (`.html`), not raw `.md`. Use links from the topic indexes below, or replace `.md` with `.html` in the URL. If your Pages URL uses a different repo name, set `baseurl` in [`_config.yml`](_config.yml).

## Table of contents

- [Browse by topic](#browse-by-topic)
- [CSES](#cses)
- [USACO](#usaco)
  - [Bronze](#bronze)
  - [Silver](#silver)
  - [Gold](#gold)
- [Repository layout](#repository-layout)
- [Scripts](#scripts)

---

## Browse by topic

| Topic | Index |
| --- | --- |
| Arrays | [`src/questions/arrays/README.html`](src/questions/arrays/README.html) |
| Binary search | [`src/questions/binary-search/README.html`](src/questions/binary-search/README.html) |
| C++ STL | [`src/questions/cpp-stl/README.html`](src/questions/cpp-stl/README.html) |
| Data structure implementations | [`src/questions/data-structure-implementations/README.html`](src/questions/data-structure-implementations/README.html) |
| Dynamic programming | [`src/questions/dp/README.html`](src/questions/dp/README.html) |
| Disjoint set union (DSU) | [`src/questions/dsu/README.html`](src/questions/dsu/README.html) |
| Fenwick & segment trees | [`src/questions/fenwick-and-segment-trees/README.html`](src/questions/fenwick-and-segment-trees/README.html) |
| Graphs | [`src/questions/graphs/README.html`](src/questions/graphs/README.html) |
| Heaps | [`src/questions/heaps/README.html`](src/questions/heaps/README.html) |
| Linked list | [`src/questions/linked-list/README.html`](src/questions/linked-list/README.html) |
| Math | [`src/questions/math/README.html`](src/questions/math/README.html) |
| Misc | [`src/questions/misc/README.html`](src/questions/misc/README.html) |
| Queue | [`src/questions/queue/README.html`](src/questions/queue/README.html) |
| Recursion & backtracking | [`src/questions/recursion-and-backtracking/README.html`](src/questions/recursion-and-backtracking/README.html) |
| Sliding window | [`src/questions/sliding-window/README.html`](src/questions/sliding-window/README.html) |
| Stack | [`src/questions/stack/README.html`](src/questions/stack/README.html) |
| Subarray hashing | [`src/questions/subarray-hashing/README.html`](src/questions/subarray-hashing/README.html) |
| Trees | [`src/questions/trees/README.html`](src/questions/trees/README.html) |

---

## CSES

| Section | Index |
| --- | --- |
| DP | [`src/questions/cses/DP/README.html`](src/questions/cses/DP/README.html) |
| Range queries | [`src/questions/cses/range-queries/README.html`](src/questions/cses/range-queries/README.html) |
| Sorting & searching | [`src/questions/cses/sorting-and-searching/README.html`](src/questions/cses/sorting-and-searching/README.html) |
| Trees | [`src/questions/cses/Trees/README.html`](src/questions/cses/Trees/README.html) |

---

## USACO

### Bronze

| Track | Index |
| --- | --- |
| Additional practice | [`src/questions/usaco/bronze-additional-practice/README.html`](src/questions/usaco/bronze-additional-practice/README.html) |
| Ad hoc | [`src/questions/usaco/bronze-ad-hoc/README.html`](src/questions/usaco/bronze-ad-hoc/README.html) |
| Complete search | [`src/questions/usaco/bronze-complete-search/README.html`](src/questions/usaco/bronze-complete-search/README.html) |
| Complete search with recursion | [`src/questions/usaco/bronze-complete-search-with-recursion/README.html`](src/questions/usaco/bronze-complete-search-with-recursion/README.html) |
| Introduction to graph algorithms | [`src/questions/usaco/bronze-introduction-to-graph-algorithms/README.html`](src/questions/usaco/bronze-introduction-to-graph-algorithms/README.html) |
| Introduction to greedy algorithms | [`src/questions/usaco/bronze-introduction-to-greedy-algorithms/README.html`](src/questions/usaco/bronze-introduction-to-greedy-algorithms/README.html) |
| Introduction to sets and maps | [`src/questions/usaco/bronze-introduction-to-sets-and-maps/README.html`](src/questions/usaco/bronze-introduction-to-sets-and-maps/README.html) |
| Rectangle geometry | [`src/questions/usaco/bronze-rectangle-geometry/README.html`](src/questions/usaco/bronze-rectangle-geometry/README.html) |
| Simulation | [`src/questions/usaco/bronze-simulation/README.html`](src/questions/usaco/bronze-simulation/README.html) |

### Silver

| Track | Index |
| --- | --- |
| Custom comparators & coordinate compression | [`src/questions/usaco/silver-custom-comparators-and-coordinate-compression/README.html`](src/questions/usaco/silver-custom-comparators-and-coordinate-compression/README.html) |
| DFS | [`src/questions/usaco/silver-dfs/README.html`](src/questions/usaco/silver-dfs/README.html) |
| Trees | [`src/questions/usaco/silver-trees/README.html`](src/questions/usaco/silver-trees/README.html) |

### Gold

| Track | Index |
| --- | --- |
| Intro to DP | [`src/questions/usaco/gold-intro-to-dp/README.html`](src/questions/usaco/gold-intro-to-dp/README.html) |
| Knapsack DP | [`src/questions/usaco/gold-knapsack-dp/README.html`](src/questions/usaco/gold-knapsack-dp/README.html) |

---

## Repository layout

| Path | Contents |
| --- | --- |
| [`_config.yml`](_config.yml) | Jekyll / GitHub Pages config (`baseurl`, optional front matter). |
| [`_layouts/default.html`](_layouts/default.html) | HTML wrapper and markdown styling for rendered pages. |
| [`src/questions/README.html`](src/questions/README.html) | Hub of all topics (generated from `README.md` in that folder). |
| [`scripts/`](scripts/) | Helper scripts |

---

## Scripts

- [`scripts/format_md_questions.py`](scripts/format_md_questions.py) — normalize fences, headers, and links in question markdown under `src/questions/`.
- [`scripts/generate_question_indexes.py`](scripts/generate_question_indexes.py) — regenerate `README.md` indexes under `src/questions/` (run after adding or renaming problem files).

---

## Local Jekyll preview

```bash
bundle install
bundle exec jekyll serve
```

Open the site at `http://127.0.0.1:4000/cp-source-codes/` (adjust `baseurl` if you change it).
