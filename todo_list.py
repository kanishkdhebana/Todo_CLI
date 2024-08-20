#!/usr/bin/env python3

import json
import click

TASK_DATA_FILE = "tasks.json"

class Task:
    def __init__(self, description, completed = False, priority = "medium"):
        self.description = description
        self.completed = completed
        self.priority = priority
        
    def __str__(self) -> str:
        return f"{'[x]' if self.completed else '[ ]'} [{self.priority}] {self.description}"



class TaskManager:
    def __init__(self, task_data_file = TASK_DATA_FILE):
        self.task_data_file = task_data_file
        self.load_tasks()   

    def load_tasks(self):
        try:
            with open(self.task_data_file, 'r') as file:
                task_data = json.load(file)
                self.tasks = [Task(**task) for task in task_data]
            
        except FileNotFoundError:
            print("Tasks file not found. Creating a new one.")
            self.tasks = []
        
        except json.JSONDecodeError:
            print("Error loading tasks. Using an empty list.")
            self.tasks = []
        

    def save_tasks(self, tasks):
        try:
            task_data = [task.__dict__ for task in self.tasks]
            with open(self.task_data_file, 'w') as file:
                json.dump(task_data, file, indent = 2)
                
        except IOError:
            print("Error saving tasks.")
            

    def add_task(self, description, priority = "medium"):
        task = Task(description, priority = priority)
        self.tasks.append(task)
        self.save_tasks(self.tasks)
        

    def list_tasks(self):
        if not self.tasks:
            click.echo("No tasks found.")
            
        else:
            self.tasks.sort(key = lambda task: task.priority)
            for index, task in enumerate(self.tasks, start = 1):
                click.echo(f"{index}. {task}")
                

    def mark_complete(self, task_index):
        try:
            self.tasks[task_index - 1].completed = True  
            self.save_tasks(tasks)
            print(f"Task {task_index} marked as complete.")
            
        except (IndexError, ValueError):
            print("Invalid task index.")


    def remove_task(self, task_index):
        try:
            del self.tasks[task_index - 1]
            self.save_tasks(self.tasks)
            click.echo(f"Task {task_index} removed.")
            
        except (IndexError, ValueError):
            click.echo("Invalid task index.")
            

@click.group()
def cli():
    pass

PRIORITIES = {
    "l": "Low",
    "m": "Medium",
    "h": "High"
}
    

@cli.command()
@click.argument("description")
@click.option("-p", "--priority", default = "m", type = click.Choice(PRIORITIES.keys()), help = "Task priority (l: Low, m: Medium, h: High)")
def add(description, priority):
    task_manager = TaskManager() 
    task_manager.add_task(description, PRIORITIES[priority])
    click.echo(f"Task '{description}' added with priority '{PRIORITIES[priority]}'.")
    
@cli.command()
def list(): 
    task_manager = TaskManager()
    task_manager.list_tasks()
    
@click.command()
@click.argument("index", type = int)
def complete(index):
    task_manager = TaskManager() 
    task_manager.mark_complete(index)
    
@cli.command()
@click.argument("index", type = int)
def remove(index): 
    task_manager = TaskManager() 
    task_manager.remove_task(index)


if __name__ == "__main__":
    cli()
