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

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/task-manager-cli.git
    cd task-manager-cli
    ```

2. **Install the required packages:**

    Install the dependencies using `pip`:

    ```bash
    pip install click
    ```

3. **Make the script executable (optional):**

    If you want to run the script directly:

    ```bash
    chmod +x task_manager.py
    ```

## Usage

### Adding a Task

To add a new task, use the `add` command followed by the task description and an optional priority flag.

```bash
python task_manager.py add "Buy groceries" --priority h
