# Course index

Reference: [Bro Code's Python course](https://www.youtube.com/watch?v=ix9cRaBkVe0).
Topic groups below are repository organization, not exact video chapters. Current watch progress is self-reported at about four hours; uploaded code covers early topics through rock, paper, scissors. Watched does not mean implemented. There is no uploaded dice-roller or functions exercise yet.

## Existing work · 10 scripts

| Current file | Original root filename |
| --- | --- |
| [username_validator.py](01_basics/username_validator.py) | `check_user_input.py` |
| [compound_interest_calculator.py](01_basics/compound_interest_calculator.py) | `compound_interest_calculator.py` |
| [countdown_timer.py](01_basics/countdown_timer.py) | `countdown_time.py` |
| [single_item_cart.py](01_basics/single_item_cart.py) | `shop_cart.py` |
| [temperature_converter.py](01_basics/temperature_converter.py) | `temperture_convert.py` |
| [shopping_cart.py](02_collections_games/shopping_cart.py) | `shopping_cart.py` |
| [concession_stand.py](02_collections_games/concession_stand.py) | `concession_stand.py` |
| [quiz_game.py](02_collections_games/quiz_game.py) | `quiz_game.py` |
| [number_guessing_game.py](02_collections_games/number_guessing_game.py) | `number_guessing_game.py` |
| [rock_paper_scissors.py](02_collections_games/rock_paper_scissors.py) | `rock_paper_scissors.py` |

The two carts are different exercises: `single_item_cart.py` calculates one purchase; `shopping_cart.py` collects multiple purchases. Both are retained.

## Where the rest goes

| Folder | Coverage | Upload status |
| --- | --- | --- |
| [01_basics](01_basics/) | Input, numeric types, strings, conditions and loops. Existing exercises live here. | Existing work |
| [02_collections_games](02_collections_games/) | Lists, tuples, dictionaries and random choices. Existing exercises live here. | Existing work |
| [03_functions_modules](03_functions_modules/) | Next: functions, arguments, comprehensions, scope and modules. | Planned |
| [04_cli_projects](04_cli_projects/) | Planned: the course banking, slot machine, encryption and hangman exercises. | Planned |
| [05_oop](05_oop/) | Planned: classes, inheritance, polymorphism, properties and decorators. | Planned |
| [06_files_exceptions](06_files_exceptions/) | Planned: exceptions, file operations, dates and the alarm clock exercise. | Planned |
| [07_apis_concurrency](07_apis_concurrency/) | Planned: threads and requesting API data. | Planned |
| [08_gui](08_gui/) | Planned: PyQt5 basics, digital clock, stopwatch and weather application. | Planned |

A skipped early lesson can be uploaded later to its topic folder. For example, a dice roller belongs in `02_collections_games/`. The remaining roughly seven to eight hours have locations ready, but no completed work is claimed for them.

Only add external dependencies when a new exercise actually needs them. For an API or GUI app, document its own install/run steps in a subfolder README. Keep keys in environment variables, never in source files.
