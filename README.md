# CP & DSA source codes

Competitive programming notes and solutions organized by topic. Each markdown file under [`src/questions/`](src/questions/) holds a problem write-up and/or solution sketch.

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

| Topic | Folder |
| --- | --- |
| Arrays | [`src/questions/arrays/`](src/questions/arrays/) |
| Binary search | [`src/questions/binary-search/`](src/questions/binary-search/) |
| Data structure implementations | [`src/questions/data-structure-implementations/`](src/questions/data-structure-implementations/) |
| Dynamic programming | [`src/questions/dp/`](src/questions/dp/) |
| Disjoint set union (DSU) | [`src/questions/dsu/`](src/questions/dsu/) |
| Fenwick & segment trees | [`src/questions/fenwick-and-segment-trees/`](src/questions/fenwick-and-segment-trees/) |
| Graphs | [`src/questions/graphs/`](src/questions/graphs/) |
| Heaps | [`src/questions/heaps/`](src/questions/heaps/) |
| Linked list | [`src/questions/linked-list/`](src/questions/linked-list/) |
| Math | [`src/questions/math/`](src/questions/math/) |
| Misc | [`src/questions/misc/`](src/questions/misc/) |
| Queue | [`src/questions/queue/`](src/questions/queue/) |
| Recursion & backtracking | [`src/questions/recursion-and-backtracking/`](src/questions/recursion-and-backtracking/) |
| Sliding window | [`src/questions/sliding-window/`](src/questions/sliding-window/) |
| Stack | [`src/questions/stack/`](src/questions/stack/) |
| Subarray hashing | [`src/questions/subarray-hashing/`](src/questions/subarray-hashing/) |
| Trees | [`src/questions/trees/`](src/questions/trees/) |

---

## CSES

| Section | Folder |
| --- | --- |
| DP | [`src/questions/cses/DP/`](src/questions/cses/DP/) |
| Range queries | [`src/questions/cses/range-queries/`](src/questions/cses/range-queries/) |
| Sorting & searching | [`src/questions/cses/sorting-and-searching/`](src/questions/cses/sorting-and-searching/) |
| Trees | [`src/questions/cses/Trees/`](src/questions/cses/Trees/) |

---

## USACO

### Bronze

| Track | Folder |
| --- | --- |
| Additional practice | [`src/questions/usaco/bronze-additional-practice/`](src/questions/usaco/bronze-additional-practice/) |
| Ad hoc | [`src/questions/usaco/bronze-ad-hoc/`](src/questions/usaco/bronze-ad-hoc/) |
| Complete search | [`src/questions/usaco/bronze-complete-search/`](src/questions/usaco/bronze-complete-search/) |
| Complete search with recursion | [`src/questions/usaco/bronze-complete-search-with-recursion/`](src/questions/usaco/bronze-complete-search-with-recursion/) |
| Introduction to graph algorithms | [`src/questions/usaco/bronze-introduction-to-graph-algorithms/`](src/questions/usaco/bronze-introduction-to-graph-algorithms/) |
| Introduction to greedy algorithms | [`src/questions/usaco/bronze-introduction-to-greedy-algorithms/`](src/questions/usaco/bronze-introduction-to-greedy-algorithms/) |
| Introduction to sets and maps | [`src/questions/usaco/bronze-introduction-to-sets-and-maps/`](src/questions/usaco/bronze-introduction-to-sets-and-maps/) |
| Rectangle geometry | [`src/questions/usaco/bronze-rectangle-geometry/`](src/questions/usaco/bronze-rectangle-geometry/) |
| Simulation | [`src/questions/usaco/bronze-simulation/`](src/questions/usaco/bronze-simulation/) |

### Silver

| Track | Folder |
| --- | --- |
| Custom comparators & coordinate compression | [`src/questions/usaco/silver-custom-comparators-and-coordinate-compression/`](src/questions/usaco/silver-custom-comparators-and-coordinate-compression/) |
| DFS | [`src/questions/usaco/silver-dfs/`](src/questions/usaco/silver-dfs/) |
| Trees | [`src/questions/usaco/silver-trees/`](src/questions/usaco/silver-trees/) |

### Gold

| Track | Folder |
| --- | --- |
| Intro to DP | [`src/questions/usaco/gold-intro-to-dp/`](src/questions/usaco/gold-intro-to-dp/) |
| Knapsack DP | [`src/questions/usaco/gold-knapsack-dp/`](src/questions/usaco/gold-knapsack-dp/) |

---

## Repository layout

| Path | Contents |
| --- | --- |
| [`src/questions/`](src/questions/) | Problem markdown grouped by topic or contest. Start from [`src/questions/README.md`](src/questions/README.md) for a hub page with links into every topic; each folder has its own generated `README.md` listing every `.md` file (for GitHub and GitHub Pages). |
| [`scripts/`](scripts/) | Helper scripts |

---

## Scripts

- [`scripts/format_md_questions.py`](scripts/format_md_questions.py) — normalize fences, headers, and links in question markdown under `src/questions/`.
- [`scripts/generate_question_indexes.py`](scripts/generate_question_indexes.py) — regenerate `README.md` indexes under `src/questions/` (run after adding or renaming problem files).
