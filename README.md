# Todo_CLI
A command-line tool to manage your tasks efficiently. Easily add, list, complete, and remove tasks. Uses JSON for data storage.

# To-Do List Manager

A simple command-line interface (CLI) based To-Do List Manager written in Python. This tool helps you manage your tasks, mark them as complete, and remove them once done. The tasks are stored in a JSON file (`tasks.json`) for persistent storage.

## Features

- **Add tasks**: Quickly add tasks to your to-do list.
- **List tasks**: View all your tasks in a numbered list.
- **Mark tasks as complete**: Mark tasks as complete using a special character (`~`).
- **Remove tasks**: Delete tasks from your list.
- **Command Aliases**: Use convenient aliases for the commands.

## Prerequisites

- **Python 3.x**: Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/todo-list-manager.git
    cd todo-list-manager
    ```

2. Create an alias for ease of use:

    Add the following aliases to your `.zshrc` (for zsh) or `.bashrc` (for bash) file:

    ```bash
    alias todo_add='python todo_list.py add'
    alias todo_list='python todo_list.py list'
    alias todo_complete='python todo_list.py complete'
    alias todo_remove='python todo_list.py remove'
    alias todo_help='python todo_list.py commands'
    ```

3. Reload your shell configuration:

    ```bash
    source ~/.zshrc  # or source ~/.bashrc if you're using bash
    ```

## Usage

1. **Add a new task:**

    ```bash
    todo_add "Buy groceries"
    ```

2. **List all tasks:**

    ```bash
    todo_list
    ```

3. **Mark a task as complete:**

    ```bash
    todo_complete 1
    ```

4. **Remove a task:**

    ```bash
    todo_remove 1
    ```

5. **List available commands:**

    ```bash
    todo_help
    ```

## Task Storage

Tasks are stored in a JSON file (`tasks.json`) located in the same directory as `todo_list.py`. This file is automatically created if it doesn't exist.
