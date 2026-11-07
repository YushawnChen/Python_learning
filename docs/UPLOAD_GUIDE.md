# Upload the next exercise

## GitHub website

1. Open [the course folder](https://github.com/YushawnChen/Python_learning/tree/main/course) and choose the topic folder using its README. Start with `03_functions_modules` for your current next topics.
2. Choose **Add file → Upload files**. Drop only the exercise files into that folder. Choose **Add file → Create new file** if writing a short lesson note directly online.
3. Use descriptive names such as `default_arguments.py` or `keyword_arguments.py`. Multi-file apps get their own subfolder; avoid `final2.py`, spaces, and duplicate uploads at the root.
4. Run the program locally with typical input and one edge case. Run `python3 -m unittest discover -s tests -v` if changing a checked exercise.
5. Commit with a concrete message, e.g. `Add default argument practice` or `Fix empty cart total`.
6. Add a real session entry to `docs/LEARNING_LOG.md`. Update the course index and the root README's script count only when the uploaded evidence changes. Keep planned items labelled planned.

## VS Code / local Git

If you already have a local clone, sync it before editing. The repository was reorganized: old root script paths moved; see the [mapping](../course/README.md).

```bash
git pull --ff-only
# Edit a file in its topic folder, then run it:
python3 course/03_functions_modules/default_arguments.py
# The example above is a future filename; create it yourself first.
git status
git add course/03_functions_modules/default_arguments.py docs/LEARNING_LOG.md
git commit -m "Add default argument practice"
git push
```

If `git pull` reports local changes or a conflict, keep your work and inspect it before proceeding. Stage specific files so unrelated local files do not enter the repository.

## What belongs where

- Tutorial exercises and adaptations: `course/` with source attribution.
- Independent problem choice, design, implementation and evidence: `projects/` (or a dedicated repository linked from there).
- Notes about your actual reasoning and fixes: `docs/LEARNING_LOG.md`.
- Short targeted regression checks: `tests/`.

Do not upload `.env`, API keys, virtual environments, editor caches, private data or a copy of the tutorial video. Do not add an AI project to the featured list until it runs and you can explain it.
