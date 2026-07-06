# Steps to maintain this repository of questions

1. Examine all changes: new files, files moved between directories, deleted files (use `git status`).

2. Check `scripts/` first — use the available scripts wherever possible:
   - `scripts/format_md_questions.py` — fixes code fences, headings, title headers
   - `scripts/generate_question_indexes.py` — regenerates all `README.md` index files
   - `scripts/sync_topics_yml.py` — syncs `_data/topics.yml` with files on disk
   - Run in order: format → generate indexes → sync topics

3. For changed/new `.md` files, format markdown properly (no content changes — no extra comments, no extra text):
   - ` ```cpp ` fences for all C++ code
   - Proper headings, bullet points, problem description section

4. If a **new topic folder** was added under `src/questions/`:
   - Add it to `TOP_LEVEL_TITLES` in `scripts/generate_question_indexes.py`
   - Add it as a new top-level entry in `_data/topics.yml`

5. Run the three scripts (step 2) to regenerate all indexes and sync the topics mapping.

6. Verify: 
    - all section `README.md` files list the correct problems (nested as well till the deepest level), 
    - `_data/topics.yml` has no stale/missing entries, and navigation links are accurate.



i want to add a "flashcards" feature in this repo which i should be able to use on my github pages.

it should work natively in gitub pages

clicking on it will open open a new page which will show me the list of all available sections inside of questions (such as arrays, binary-search, ....)
clicking on a section will then start showing me a randomly picked series of questions. just directly show the enitre md file (eg:- @src/questions/dp/(DP on Trees) LCA using Binary Lifting.md ) as it is, but in responsive format (both pc and mobile friendly)

seciton choice is only at top level (eg:- cses) and not at nested levels below it (i.e. clicking on cses will start a random series taking the complete universe of questions inside cses/DP + cse/range-queries + ...)

implement this in minimum number of files required. make it compact, accurate, correct. i dont care about readability or maintainibility. i care only about it working accurately without bloating up a large number of files 