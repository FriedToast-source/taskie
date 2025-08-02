import argparse
import os
import json
from prettytable import PrettyTable
from datetime import datetime,timezone
from rich.console import Console

console = Console()


dt = datetime.now(timezone.utc)
time = dt.strftime('%a %d %b %Y, %I:%M%p')

def main():

    parser = argparse.ArgumentParser(prog='task',description="Task manager that Manages your tasks")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("task",type=str, help="Task description")

    parser_update = subparsers.add_parser("update",help="update a task description")
    parser_update.add_argument("id", type=int, help="ID of the task to update")
    parser_update.add_argument("task",type=str, help="update task")

    parser_list = subparsers.add_parser("list",help="list tasks")
    parser_list.add_argument("status", type=str, nargs='?', default=None, help="Status of the tasks")

    parser_mark = subparsers.add_parser("mark", help="Mark a task as completed or pending")
    parser_mark.add_argument("id", type=int, help="ID of the task to mark")
    parser_mark.add_argument("status", type=str, choices=["done", "in-progress"], help="New status")

    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("id", type=int, help="ID of the task to delete")

    args = parser.parse_args()

    if args.command == "add":
            write_json(args.task)
    elif args.command == "list":
            if args.status is None:
                 show_all()
            else:
                 show_some(args.status)
    elif args.command == "update":
            update_json(args.id, args.task)
    elif args.command == "mark":
            mark_json(args.id, args.status)
    elif args.command == "delete":
            delete_json(args.id)
    else:
            parser.print_help()


def write_json(task):

    new_data = {
    "id":0,
    "status":"todo",
    "task":task,
    "createdat": time,
    "updatedat":"n/a",
    }

    if not os.path.exists('tasks.json'):
        with open('task.json', 'r+') as file:
            data = json.load(file)
            data["to-do-list"].append(new_data)
            file.seek(0)
            json.dump(data, file, indent=4)
        reorder_json()
        console.print(f"[green]task added successfully.[/green]")

def mark_json(id,status):
        if not os.path.exists('tasks.json'):
            with open('task.json','r+') as file:
                data = json.load(file)
                new_dict = {"to-do-list":[]}
                for item in data["to-do-list"]:
                    if item["id"] == id:
                        new_dict["to-do-list"].append({"id":item["id"],"status":status,"task":item["task"],
                                                    "createdat": item["createdat"], "updatedat":"time"})
                    else:
                        new_dict["to-do-list"].append(item)

                if new_dict == data["to-do-list"]:
                    console.print(f"[red]Task ID {id} not found.[/red]")
                    return

            with open('task.json', 'w') as file:
                file.seek(0)
                json.dump(new_dict, file, indent=4)



def delete_json(id):
        if not os.path.exists('tasks.json'):
            with open('task.json','r+') as file:
                data = json.load(file)
                new_dict={"to-do-list":[]}
                new_dict["to-do-list"] = [info for info in data["to-do-list"] if info["id"] != id]
                file.seek(0)
                file.truncate()
                json.dump(new_dict, file, indent=4)
                if len(new_dict)==len(data["to-do-list"]):
                    console.print(f"[yellow]Task ID {task_id} deleted successfully.[/yellow]")
                else:
                    console.print(f"[red]Task ID {task_id} does not exist.[/red]")

            reorder_json()

def update_json(id,task):
    if not os.path.exists('tasks.json'):
        with open('task.json','r+') as file:
            data = json.load(file)
            new_dict = {"to-do-list":[]}
            for info in data["to-do-list"]:
                if info["id"] == id:
                    new_dict["to-do-list"].append({"id":id,"status":info["status"],"task":task,"createdat": info["createdat"], "updatedat":time})
                else:
                    new_dict["to-do-list"].append(info)
            if new_dict == data["to-do-list"]:
                console.print(f"[red]Task ID {id} not found.[/red]")
                return

            file.seek(0)
            file.truncate()
            json.dump(new_dict, file, indent=4)

def reorder_json():
    if not os.path.exists('tasks.json'):
        with open('task.json','r+') as file:
            data = json.load(file)
            new_dict = {"to-do-list":[]}
            for i, item in enumerate(data["to-do-list"]):
                new_dict["to-do-list"].append({"id":i+1,"status":item["status"],"task":item["task"],"createdat": item["createdat"], "updatedat":item["updatedat"]})
        with open('task.json', 'w') as file:
            file.seek(0)
            json.dump(new_dict, file, indent=4)

def table_json(list):

    x = PrettyTable()
    x.field_names = ["ID", "STATUS","TASK","CREATEDAT","UPDATEDAT"]
    for item in list:
        row = item.values()
        x.add_row(row)
    return x

def show_some(status):
     if not os.path.exists('tasks.json'):
        with open('task.json', 'r') as file:
            data = json.load(file)
            list = [info for info in data["to-do-list"] if info["status"] == status]
            table = table_json(list)
            print(table)

def show_all():
     if not os.path.exists('tasks.json'):
        with open('task.json', 'r') as file:
            data = json.load(file)
            table = table_json(data["to-do-list"])
            print(table)

if __name__ == "__main__":
    main()

