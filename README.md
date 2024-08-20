# Todo CLI

A simple and effective Command-Line Interface (CLI) application to manage tasks. This Task Manager allows you to add, list, complete, and remove tasks with varying priorities. Tasks are stored in a JSON file, making it easy to persist and manage your tasks over time.

## Features

- **Add Tasks:** Add new tasks with a priority level (Low, Medium, or High).
- **List Tasks:** View all tasks sorted by their priority.
- **Complete Tasks:** Mark tasks as completed.
- **Remove Tasks:** Remove tasks from the list.

## Requirements

- Python 3.6 or higher
- `click` library

## Installation and Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/kanishkdhebana/Todo_CLI
    cd Todo_CLI
    ```

2. **Install the required packages:**

    Install the dependencies using `pip`:

    ```bash
    pip install click
    ```

3. **Make the script executable:**

    If you want to run the script directly:

    ```bash
    chmod +x todo.py
    ```

4. **Add alias to .bashrc or .zshrc:**

    Add this line to `.bashrc` or `.zshrc` to create a convenient alias for the script:

    ```bash
    alias todo='python /path/to/todo.py'
    ```

    Replace `/path/to/todo.py` with the actual path to the `todo.py` file.

5. **Reload your shell configuration:**

    After adding the alias, reload your shell configuration to apply the changes:

    ```bash
    source ~/.bashrc   # For bash users
    source ~/.zshrc    # For zsh users
    ```

## Usage

### Adding a Task

To add a new task, use the `add` command followed by the task description and an optional priority flag.

```bash
todo add "Buy groceries" --priority h
