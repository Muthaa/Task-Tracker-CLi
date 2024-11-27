# Task Tracker CLI  

Task Tracker is a simple command-line interface (CLI) application to help you manage and track tasks. You can add tasks, update them, delete tasks, and mark their progress. Tasks are stored in a `tasks.json` file in the current directory for persistence.
---

## Features  

- **Add Tasks**: Add new tasks with a short description.
- **Update Tasks**: Update the description of an existing task.
- **Delete Tasks**: Remove tasks by their unique ID.
- **Mark Tasks**: Mark tasks as `in-progress` or `done`.
- **List Tasks**: View all tasks or filter tasks by their status (`todo`, `in-progress`, `done`).
- **Persist Data**: Task data is stored in a JSON file for easy reuse.
- **Error Handling**: Gracefully handles invalid inputs and edge cases.
---

## Installation  

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/task-tracker-cli.git
   cd task-tracker-cli
   ```

2. **Run the Script**:
   Ensure Python 3 is installed on your system.  
   ```bash
   python tracker.py
   ```
---

## Usage  

$ python tracker.py
Task Tracker CLI

Usage:
  python tracker.py <command> [arguments]

Available Commands:
  add <description>           Add a new task
  update <id> <description>   Update a task's description
  delete <id>                 Delete a task by ID
  mark-in-progress <id>       Mark a task as in-progress
  mark-done <id>              Mark a task as done
  list                        List all tasks
  list <status>               List tasks by status (todo, in-progress, done)

### General Commands  

Run the script with any of the following commands:  

#### **Add a New Task**  
```bash
python tracker.py add "Task description"
```  
Example:  
```bash
python tracker.py add "Buy color"
```  
Output:  
```
Task added successfully (ID: 1)
```

#### **Update a Task**  
```bash
python tracker.py update <task_id> "Updated description"
```  
Example:  
```bash
python tracker.py update 1 "Buy ram and cook dinner"
```  
Output:  
```
Task updated successfully.
```

#### **Delete a Task**  
```bash
python tracker.py delete <task_id>
```  
Example:  
```bash
python tracker.py delete 1
```  
Output:  
```
Task deleted successfully.
```

#### **Mark a Task**  
```bash
python tracker.py mark-in-progress <task_id>
```  
Example:  
```bash
python tracker.py mark-in-progress 1
```  
Output:  
```
Task marked as in-progress.
```

```bash
python tracker.py mark-done <task_id>
```  
Example:  
```bash
python tracker.py mark-done 1
```  
Output:  
```
Task marked as done.
```

#### **List Tasks**  
```bash
python tracker.py list
```  
Output:  
```
1. [todo] Buy groceries
2. [in-progress] Cook dinner
3. [done] Wash the car
```

#### **List Tasks by Status**  
```bash
python tracker.py list <status>
```  
- `done` - Lists completed tasks.  
- `todo` - Lists tasks that are not yet started.  
- `in-progress` - Lists tasks currently in progress.  

Example:  
```bash
python tracker.py list done
```  
Output:  
```
1. [done] Wash the car
```
---

## Task Properties  

Each task has the following properties stored in the JSON file:  

- **id**: A unique identifier.  
- **description**: The task's description.  
- **status**: Task status (`todo`, `in-progress`, `done`).  
- **createdAt**: Date and time the task was created.  
- **updatedAt**: Date and time the task was last updated.  
---

## Error Handling  

- **Empty or Invalid JSON File**: Automatically initializes a new JSON file.  
- **Invalid Task ID**: Prompts the user that the task ID does not exist.  
- **Invalid Command**: Displays usage instructions for invalid commands or arguments.
---

## Contribution  

Feel free to contribute to this project by submitting a pull request or raising an issue.  
---

## License  

This project is licensed under the MIT License.  
--- 
Enjoy managing your tasks with Task Tracker CLI! 🎉  

https://roadmap.sh/projects/task-tracker

