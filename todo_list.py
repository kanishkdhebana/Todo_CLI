import argparse
import json

TASK_DATA_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASK_DATA_FILE, 'r') as file:
            return json.load(file)
        
    except FileNotFoundError:
        print("Tasks file not found. Creating a new one.")
        return []
    
    except json.JSONDecodeError:
        print("Error loading tasks. Using an empty list.")
        return []


def save_tasks(tasks):
    try:
        with open(TASK_DATA_FILE, 'w') as file:
            json.dump(tasks, file, indent = 2)
            
    except IOError:
        print("Error saving tasks.")


def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")
    

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
            

def mark_complete(task_index):
    tasks = load_tasks()
    try:
        task_index = int(task_index)
        tasks[task_index - 1] = f"~{tasks[task_index - 1]}"  # ~ means completed
        save_tasks(tasks)
        print(f"Task {task_index} marked as complete.")
        
    except (IndexError, ValueError):
        print("Invalid task index.")
        

def remove_task(task_index):
    tasks = load_tasks()
    try:
        task_index = int(task_index)
        del tasks[task_index - 1]
        save_tasks(tasks)
        print(f"Task {task_index} removed.")
        
    except (IndexError, ValueError):
        print("Invalid task index.")
        

# CLI interface
def parse_args():
    parser = argparse.ArgumentParser(description = "To-do list manager")
    parser.add_argument("command", choices = ["add", "list", "complete", "remove", "commands"], help="Command to perform")
    parser.add_argument("task", nargs = "?", help = "Task to add or its index")
    return parser.parse_args()


def list_commands():
    print("Available commands:")
    print(" todo_add: Add a new task")
    print(" todo_list: List all tasks or tasks in a category")
    print(" todo_complete: Mark a task as complete")
    print(" todo_remove: Remove a task")
    print(" todo_help: List available commands")


# driver function
def main():
    args = parse_args()
    
    if args.command == "add":
        add_task(args.task)
        
    elif args.command == "list":
        list_tasks()
        
    elif args.command == "complete":
        try:
            task_index = int(args.task)
            mark_complete(task_index)
            
        except ValueError:
            print("Invalid task index.")
            
    elif args.command == "remove":
        try:
            task_index = int(args.task)
            remove_task(task_index)
            
        except ValueError:
            print("Invalid task index.")
            
    elif args.command == "commands":
        list_commands()
        
    else:
        print("Invalid command")


if __name__ == "__main__":
    main()
