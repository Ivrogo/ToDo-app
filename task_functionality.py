import tkinter as tk
from tkinter.messagebox import showerror


# Function to add a task
def add_task_button_click(task_entry, task_list):
    task = task_entry.get()
    if task == "":
        showerror(title="Error", message="You must enter a task before adding it")

    task_list.insert(tk.END, task)
    save_task_to_file(task_list)


# Function to remove a task
def remove_task_button_click(task_list):
    task_list.delete(0, tk.END)
    save_task_to_file(task_list)


# Function to save the task into a file to keep it persistent
def save_task_to_file(task_list):
    with open("tasks.txt", "w") as file:
        tasks = task_list.get(0, tk.END)
        file.write("\n".join(tasks))


# Function to load the tasks from the file
def load_task_from_file(task_list):
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.read().splitlines()
            for task in tasks:
                task_list.insert(tk.END, task)
    except FileNotFoundError:
        pass
