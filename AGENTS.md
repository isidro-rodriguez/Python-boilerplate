# AGENTS.md

## AGENT BEHAVIOR & TOKEN SAVING

- **Prevent loops:** Do not retry failed commands >2 times. Stop, summarize root cause, ask user.
- **Save context/tokens:** Concise responses. Avoid fluff, lengthy intros, or repetitive explanations.
- **Self-contained execution:** Batch tasks/code changes efficiently.

## TECH STACK & WORKFLOW

- **Lang:** Python 3.13+.
- **Package Manager:** `uv` ONLY (`uv add`, `uv run`, `uv venv`). NEVER raw `pip` unless inside an isolated venv.
- **Formatting/Linting:** `ruff` (`uv run ruff format`, `uv run ruff check`).

## CODE & LANGUAGE RULES

- **Pythonic Style:** Idiomatic Python, type hints, PEP 8, dataclasses/pydantic where fit, `pathlib` over `os.path`.
