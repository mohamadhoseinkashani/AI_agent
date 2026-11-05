# AI Agent

An AI coding agent built in Python that can autonomously inspect and modify a codebase using LLM function calling. Give it a prompt, and it plans which tools to use, calls them, reads the results, and iterates — similar to how tools like Cursor or Copilot Workspace work under the hood.

Built as part of the [Boot.dev](https://www.boot.dev) "Build an AI Agent" course.

> **Note:** This is a learning project / prototype built for a controlled local environment. Don't run it on code you don't trust — it can read, write, and execute Python files inside its working directory.

## What it can do

The agent has four tools, each implemented as a function the LLM can call:

| Tool | Description |
|------|-------------|
| `get_files_info` | List files and directories (with sizes) inside the working directory |
| `get_file_content` | Read a file's contents (with truncation for large files) |
| `write_file` | Create or overwrite a file |
| `run_python_file` | Execute a Python file with optional arguments and capture output |

It also ships with a sample `calculator/` app that the agent can debug and fix — that's the test codebase used in the demos/tests.

## How it works

1. You send a natural-language prompt (e.g. *"fix the bug in the calculator"*)
2. The prompt + tool schemas are sent to the LLM
3. The model replies with either text or one/more function calls
4. The app executes the calls inside a sandboxed working directory, returns the results to the model, and repeats until the task is done (or the iteration limit is hit)

## Project structure

```
.
├── main.py            # Agent loop & CLI entry point
├── config.py          # Config (iteration limit, etc.)
├── functions/         # Tool implementations + schemas
├── calculator/        # Sample app the agent operates on
├── test_*.py          # Tests for each tool function
└── pyproject.toml     # Dependencies (managed with uv)
```

## Running it locally

**Prerequisites:** Python 3.13+ (see `.python-version`), [uv](https://docs.astral.sh/uv/), and an API key for the LLM provider used in `main.py` (set it in a `.env` file — check `main.py` / course instructions for the exact variable name).

```bash
# Install dependencies
uv sync

# Run the agent (from the project root)
uv run main.py "your prompt here"

# Example: ask it to inspect and explain the calculator
uv run main.py "how does the calculator render results to the console?"
```

Add `--verbose` if your version supports it to see token usage and function calls step-by-step.

## Tests

```bash
uv run python -m unittest discover

# or run individual files, e.g.:
uv run python test_get_files_info.py
```

## What I learned

- LLM function / tool calling and building an agent loop
- Safely constraining file operations to a working directory
- Structuring a Python project with `uv` and `pyproject.toml`
- Writing tests for side-effectful functions (file I/O, subprocess execution)

## Next improvements

- [ ] Add a demo GIF / example transcript to this README
- [ ] Better error messages when a tool call fails
- [ ] Support more file types in `get_file_content`
