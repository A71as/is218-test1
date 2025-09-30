# TinyTools Calculator – In-Class Test (30 min)

## Scenario
You’ve joined **TinyTools, Inc.** Deliver a production-ready **Python Calculator** library with four operations:

- **add**, **subtract**, **multiply**, **divide**  
- **Divide by zero must raise `ZeroDivisionError`.**

Your team enforces professional workflow:  
- **Brand-new repo**  
- **Atomic commits** with required prefixes  
- Pass **linting**  
- All **tests** must pass  
- **100% test coverage** required  

---

## Required Repo Layout
```

README.md
requirements.txt
src/
tests/

````

---

## Commit Rules
- Every commit message **must** start with one of:  
  - `chore:` — setup/config/docs  
  - `feature:` — new functionality **and its tests**  
  - `fix:` — bug fix or correcting a test  

- **Atomic history**:
  - Each calculator function (**add, subtract, multiply, divide**) must be delivered in **its own commit**, with the tests **and** the implementation together.  
  - Do **not** put multiple functions in one commit.  
  - Do **not** split one function across multiple commits.

- **Minimum 8 commits** required (more is fine; do not squash).

### Example Commit Timeline
1. `chore: initialize repo with README and requirements`
2. `chore: add project skeleton (src, tests) and setup notes`
3. `chore: document how to run lint/tests in README`
4. `feature: implement add() with unit tests`
5. `feature: implement subtract() with unit tests`
6. `feature: implement multiply() with unit tests`
7. `feature: implement divide() with unit tests including divide-by-zero`
8. `chore: add coverage command and enforce 100% in README`
9. *(if needed)* `fix: correct edge case in subtract() test`
10. *(if needed)* `fix: address pylint error in calculator module`

---

## Local Commands (before pushing)
```bash
# Install dependencies
pip install -r requirements.txt

# Lint (must be clean)
pylint --errors-only src

# Run tests
PYTHONPATH=src pytest tests -v
PYTHONPATH=src pytest --pylint src -v

# Coverage (must be 100%)
PYTHONPATH=src coverage run -m pytest tests
coverage report --fail-under=100
````

---

## How Grading Works

Your repository is graded entirely by the **GitHub Actions workflow** in `.github/workflows/ci.yml`.
If any step fails, you lose points for that category.

### Rubric (100 pts total)

| # | CI Job / Step         | Requirement                                                   | Points | Pass                                    | Fail                 |
| - | --------------------- | ------------------------------------------------------------- | -----: | --------------------------------------- | -------------------- |
| 1 | **Commit Policy**     | ≥ 8 commits                                                   |     20 | CI shows “Commit count requirement met” | Fewer than 8 commits |
| 2 | **Commit Policy**     | All commit messages start with `chore:` / `feature:` / `fix:` |     20 | All messages valid                      | Any message invalid  |
| 3 | **Project Structure** | `README.md`, `requirements.txt`, `src/`, `tests/` present     |     10 | All present                             | Any missing          |
| 4 | **Lint Check**        | `pylint --errors-only src` clean                              |     15 | No errors                               | Any error            |
| 5 | **Pytest-Pylint**     | `pytest --pylint src -v` passes                               |      5 | Pass                                    | Fail                 |
| 6 | **Unit Tests**        | `pytest tests -v` passes                                      |     15 | All tests pass                          | Any fail             |
| 7 | **Coverage**          | `coverage report --fail-under=100` shows 100%                 |     15 | Exactly 100%                            | < 100%               |

**Total = 100 points**

---

## Submission

* Push to GitHub/GitLab and share the repo URL **OR** upload a zip including `.git` history.
* Your **last commit** must be before the 30-minute deadline.

Fixed commit prefixes error