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