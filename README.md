# Taskie

Taskie is a cli-task-tracker

## Installation

1. Clone the repository:

```bash
https://github.com/FriedToast-source/taskie.git
```

2. Navigate to the project directory

```bash
cd taskie
```

## Features

+ Add Tasks: Easily add new tasks with descriptions.
+ Update Tasks: Modify the description or status of existing tasks.
+ Delete Tasks: Remove tasks from your list.
+ Mark Tasks: Mark tasks as 'done', 'in progress', etc.
+ List Tasks: View all tasks or filter them by status.


## Usage

```bash

#add task
python taskie.py add "task description"

#update task
python taskie.py update id "new task description"

#mark task
python taskie.py mark id <done or inprogress>

#delete task
python taskie.py delete id

#list all tasks
python taskie.py list

#list tasks by status
python taskie.py list todo
python taskie.py list in-progress
python taskie.list done
```
roadmap.sh -> https://roadmap.sh/projects/task-tracker




