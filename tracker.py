import json
import os
from datetime import datetime
import argparse

TASK_FILE = "tasks.json"

#utility functions
def load_tasks():
	#create json file for storing taks if it doesnt exist.
	if not os.path.exists(TASK_FILE):
		return [] #File doesnt exist, return an empty list

	try:
		with open(TASK_FILE, 'r') as file:
			return json.load(file) #Attempt to load JSON data
	except (json.JSONDecodeError, ValueError):
		# if json is invalid or file is empty, return an empty list
		return []
	except Exception as e:
		return e

def save_tasks(tasks):
	#open file and write tasks to it
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def get_task_by_id(tasks, task_id):
    #Find a task by its id.
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

# CLI Command Functions
def add_task(description):
	#add new tasks
    tasks = load_tasks()
    task_id = max([task['id'] for task in tasks], default=0) + 1
    now = datetime.now().isoformat()
    tasks.append({
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    })
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")

def update_task(task_id, description):
    #Update tasks .
    tasks = load_tasks()
    task = get_task_by_id(tasks, task_id)
    if task:
        task["description"] = description
        task["updatedAt"] = datetime.now().isoformat()
        save_tasks(tasks)
        print(f"Task ID {task_id} updated successfully.")
    else:
        print(f"Task ID {task_id} not found.")

def delete_task(task_id):
    #Delete a task.
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]
    if len(tasks) != len(new_tasks):
        save_tasks(new_tasks)
        print(f"Task ID {task_id} deleted successfully.")
    else:
        print(f"Task ID {task_id} not found.")


def mark_task(task_id, status):
    #Mark a task as in-progress or done.
    tasks = load_tasks()
    task = get_task_by_id(tasks, task_id)
    if task:
        task["status"] = status
        task["updatedAt"] = datetime.now().isoformat()
        save_tasks(tasks)
        print(f"Task ID {task_id} marked as {status}.")
    else:
        print(f"Task ID {task_id} not found.")

def list_tasks(status=None):
    #List tasks & filtered by status.
    tasks = load_tasks()
    filtered_tasks = [task for task in tasks if not status or task["status"] == status]
    if not filtered_tasks:
        print("No tasks found.")
        return
    for task in filtered_tasks:
        print(f"{task['id']}: {task['description']} ({task['status']})")
        print(f"    Created At: {task['createdAt']}")
        print(f"    Updated At: {task['updatedAt']}")
 
# Main CLI Handler
def main():
    parser = argparse.ArgumentParser(
        description= "Task Tracker CLI",
        usage= """task-cli <command> [<args>]

		Commands:
		  add                Add a new task
		  update             Update a task 
		  delete             Delete a task
		  mark-in-progress   Mark a task as in-progress
		  mark-done          Mark a task as done
		  list               List tasks ( filter by status) """,
    )
    subparsers = parser.add_subparsers(dest="command")
    #subparsers = parser.add_subparsers(dest="command", required=True)

    # Subcommands
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument("status", nargs="?", choices=["todo", "in-progress", "done"], help="Filter tasks by status")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Description of the task")

    update_parser = subparsers.add_parser("update", help="Update an existing task")
    update_parser.add_argument("id", type=int, help="ID of the task to update")
    update_parser.add_argument("description", help="New description for the task")

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="ID of the task to delete")

    mark_in_progress_parser = subparsers.add_parser("mark-in-progress", help="Mark a task as in-progress")
    mark_in_progress_parser.add_argument("id", type=int, help="ID of the task to mark as in-progress")

    mark_done_parser = subparsers.add_parser("mark-done", help="Mark a task as done")
    mark_done_parser.add_argument("id", type=int, help="ID of the task to mark as done")

    mark_todo_parser = subparsers.add_parser("mark-todo", help="Mark a task as todo")
    mark_todo_parser.add_argument("id", type=int, help="ID of the task to mark as todo")

    args = parser.parse_args()

    # Command Execution
    if args.command == "add":
        add_task(args.description)
    elif args.command == "update":
        update_task(args.id, args.description)
    elif args.command == "delete":
        delete_task(args.id)
    elif args.command == "mark-in-progress":
        mark_task(args.id, "in-progress")
    elif args.command == "mark-done":
        mark_task(args.id, "done")
    elif args.command == "mark-todo":
        mark_task(args.id, "todo")
    elif args.command == "list":
        list_tasks(args.status)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()