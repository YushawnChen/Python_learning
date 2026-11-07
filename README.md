# Python Foundations → Applied AI

Python practice by [Yushawn Chen](https://github.com/YushawnChen), building toward applied AI engineering internships.

This repository documents my Python foundations through small, runnable exercises and a record of what I improve. It is the learning layer of my portfolio; independent applications will be linked separately when they exist.

**Current stage · 7 November 2026:** following Bro Code's Python course, around four hours watched (self-reported). **10 exercise scripts uploaded.** Functions and later topics are next; watching progress is not a claim of mastery.

## Start here

| Example | What you can inspect | Run from the repository root |
| --- | --- | --- |
| [Concession stand](course/02_collections_games/concession_stand.py) | Dictionary lookup, menu selection, repeated items and PLN totals | `python3 course/02_collections_games/concession_stand.py` |
| [Rock, paper, scissors](course/02_collections_games/rock_paper_scissors.py) | Input validation, random choice and session win/loss tracking | `python3 course/02_collections_games/rock_paper_scissors.py` |
| [Shopping cart](course/02_collections_games/shopping_cart.py) | Collecting multiple items and accumulating a total | `python3 course/02_collections_games/shopping_cart.py` |

These are **course-based exercises**, not original product projects. My small local variations include PLN prices and session statistics; they are practice, not evidence of production or AI engineering experience.

## Run and check

Use **Python 3.10+**. The ten current scripts use only the Python standard library. Run them individually in a terminal; most ask for keyboard input.

```bash
git clone https://github.com/YushawnChen/Python_learning.git
cd Python_learning
python3 course/02_collections_games/concession_stand.py
```

Example: enter `pizza`, then `soda`, then `q`. The final bill is `PLN28.78`.

```bash
python3 -m compileall -q course tests
python3 -m unittest discover -s tests -v
```

Checks cover selected regression cases, not every input or every exercise. These beginner scripts still have limitations: several numeric prompts do not handle non-numeric input, cart exercises accept negative prices, and games use console interaction rather than reusable functions. See [the improvement backlog](docs/LEARNING_LOG.md#next-improvements).

## Repository map

```text
course/          Course exercises grouped by topic; includes future upload locations
projects/        Entry criteria and space for independently designed applications
tests/           Standard-library regression checks for selected exercises
docs/            Learning log, upload instructions and a Chinese HTML guide
```

- [All exercises and remaining course topics](course/README.md)
- [Learning log and next improvements](docs/LEARNING_LOG.md)
- [How to add the next exercise](docs/UPLOAD_GUIDE.md)
- [Independent project criteria](projects/README.md)
- [Chinese repository guide (download and open in a browser)](docs/repository-guide.html)

## From foundations to applied AI

My target is an applied AI engineering internship around **July 2027**. The next evidence I want to build is:

1. Finish the course and revisit selected scripts with functions, validation and meaningful tests.
2. Build an independent Python application with persistent data, a documented API integration and reproducible setup.
3. Publish a focused AI application with a demo, a small evaluation set, measured failure cases, and latency/cost observations.

These are plans. No AI application or independent portfolio project is published in this repository yet. Completed applications will get a short case study and a direct link here, so reviewers can reach the strongest evidence quickly.

## Source and assistance

Course reference: [Bro Code — Python Full Course for free](https://www.youtube.com/watch?v=ix9cRaBkVe0). Exercises follow or adapt course material; credit remains with its original creator. No ownership or licensing rights over the original course material are asserted here.

The November 2026 repository organization, documentation and selected bug fixes/checks were prepared with AI assistance. They do not imply that I independently designed all of this structure or have already mastered the upcoming topics. The original learning commits remain in Git history.

Profile: [github.com/YushawnChen](https://github.com/YushawnChen)
