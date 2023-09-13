import tkinter as tk
from tkinter import *
from tkinter import ttk
from task_functionality import add_task_button_click, remove_task_button_click


# Creation of the Window
app = tk.Tk()
app.title("To-Do List")
app.geometry("960x640")
app.resizable(height=True, width=True)
canvas = Canvas(app, width=960, height=640)
canvas.pack()


# Entry
task_entry = ttk.Entry(app, width=80, style="TEntry")
task_entry_style = ttk.Style()
task_entry_style.configure("TEntry", font="Roboto", relx=1.5, rely=1.5)

# Label
todo_label = ttk.Label(app, text="ToDo Application", style="TLabel")
todo_label_style = ttk.Style()
todo_label_style.configure("TLabel", font=("Arial Bold", 35))

# ListBox
task_box_list = Listbox(app, width=80, height=20)
task_box_list.pack()

# Buttons
add_button = ttk.Button(
    app,
    width=15,
    text="Add Task",
    style="TButton",
    command=lambda: add_task_button_click(task_entry, task_box_list),
)
add_button_style = ttk.Style()
add_button_style.configure("TButton", font="Roboto", padx=10, pady=10)
remove_button = ttk.Button(
    app,
    width=15,
    text="Remove Task",
    style="TButton",
    command=lambda: remove_task_button_click(task_box_list),
)
remove_button_style = ttk.Style()
remove_button_style.configure("TButton", font="Roboto", padx=10, pady=10)

# Canvas add
canvas.create_window(500, 50, window=todo_label)
canvas.create_window(500, 200, window=task_entry)
canvas.create_window(400, 150, window=add_button)
canvas.create_window(550, 150, window=remove_button)
canvas.create_window(500, 400, window=task_box_list)

# Run
app.mainloop()
