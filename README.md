Here I have added all types of data structure and algorithm questions.
With unit testing for them.
In this repo you can find all types of techniques and concepts regarding DSA.

## Career roadmap

Interview and career-growth plan lives in [Roadmap/](Roadmap/README.md) — 24-week plan covering DSA,
HTTP/internet fundamentals, LLD, HLD/distributed systems, AI/ML, and LLM/GenAI, with a progress tracker.

## uv command reference

[uv](https://docs.astral.sh/uv/) is the Python package/project manager used for this repo.
Command list below is from `uv 0.11.32`; run `uv help <command>` for full details on any of them.

### Project commands

| Command | Description |
| --- | --- |
| `uv init` | Create a new project |
| `uv add` | Add dependencies to the project |
| `uv remove` | Remove dependencies from the project |
| `uv sync` | Update the project's environment to match the lockfile |
| `uv lock` | Update the project's lockfile |
| `uv run` | Run a command or script in the project environment |
| `uv version` | Read or update the project's version |
| `uv export` | Export the lockfile to an alternate format (e.g. `requirements.txt`) |
| `uv tree` | Display the project's dependency tree |
| `uv format` | Format Python code in the project |
| `uv check` | Run checks on the project |
| `uv audit` | Audit the project's dependencies for known vulnerabilities |
| `uv build` | Build the project into source distributions and wheels |
| `uv publish` | Upload distributions to an index |

### Environments and Python versions

| Command | Description |
| --- | --- |
| `uv venv` | Create a virtual environment |
| `uv python list` | List the available Python installations |
| `uv python install` | Download and install Python versions |
| `uv python upgrade` | Upgrade installed Python versions |
| `uv python find` | Search for a Python installation |
| `uv python pin` | Pin the project to a specific Python version |
| `uv python dir` | Show the uv Python installation directory |
| `uv python uninstall` | Uninstall Python versions |
| `uv python update-shell` | Ensure the Python executable directory is on `PATH` |

### pip-compatible interface

| Command | Description |
| --- | --- |
| `uv pip install` | Install packages into an environment |
| `uv pip uninstall` | Uninstall packages from an environment |
| `uv pip compile` | Compile `requirements.in` to `requirements.txt` / `pylock.toml` |
| `uv pip sync` | Sync an environment with `requirements.txt` / `pylock.toml` |
| `uv pip freeze` | List installed packages in requirements format |
| `uv pip list` | List installed packages in tabular format |
| `uv pip show` | Show information about one or more installed packages |
| `uv pip tree` | Display the dependency tree for an environment |
| `uv pip check` | Verify installed packages have compatible dependencies |

### Tools (standalone CLI packages)

| Command | Description |
| --- | --- |
| `uv tool run` | Run a command provided by a Python package (alias: `uvx`) |
| `uv tool install` | Install commands provided by a Python package |
| `uv tool upgrade` | Upgrade installed tools |
| `uv tool list` | List installed tools |
| `uv tool uninstall` | Uninstall a tool |
| `uv tool update-shell` | Ensure the tool executable directory is on `PATH` |
| `uv tool dir` | Show the path to the uv tools directory |

### Workspaces

| Command | Description |
| --- | --- |
| `uv workspace metadata` | View metadata about the current workspace |
| `uv workspace list` | List the members of a workspace |
| `uv workspace dir` | Display the path of a workspace member |

### Authentication

| Command | Description |
| --- | --- |
| `uv auth login` | Login to a service (e.g. a private index) |
| `uv auth logout` | Logout of a service |
| `uv auth token` | Show the authentication token for a service |
| `uv auth dir` | Show the path to the uv credentials directory |

### Cache and self-management

| Command | Description |
| --- | --- |
| `uv cache clean` | Clear the cache, all entries or those for specific packages |
| `uv cache prune` | Prune dangling cache entries and cached environments |
| `uv cache dir` | Show the cache directory |
| `uv cache size` | Show the cache size |
| `uv self update` | Update uv itself |
| `uv self version` | Display uv's version |
| `uv help` | Display documentation for a command |

### Common global options

These work on most commands:

| Option | Description |
| --- | --- |
| `-n`, `--no-cache` | Avoid reading from or writing to the cache |
| `--cache-dir <DIR>` | Path to the cache directory |
| `--managed-python` / `--no-managed-python` | Require / disable uv-managed Python versions |
| `--no-python-downloads` | Disable automatic downloads of Python |
| `-q`, `--quiet` / `-v`, `--verbose` | Quieter or more verbose output |
| `--color <auto\|always\|never>` | Control use of color in output |
| `--offline` | Disable network access |
| `--directory <DIR>` | Change to the given directory before running |
| `--project <DIR>` | Discover a project in the given directory |
| `--config-file <FILE>` | Path to a `uv.toml` file to use for configuration |
| `--no-config` | Avoid discovering `pyproject.toml` / `uv.toml` |
| `-V`, `--version` | Display the uv version |

### Typical workflow

This repo has no `pyproject.toml` / `uv.lock` yet, so start with `uv init`:

```bash
uv init                     # create pyproject.toml
uv add --dev pytest         # add a dev dependency (creates .venv + uv.lock)
uv run pytest               # run the unit tests
uv sync                     # after a fresh clone, install locked dependencies
uvx ruff check .            # run a tool without installing it
```
