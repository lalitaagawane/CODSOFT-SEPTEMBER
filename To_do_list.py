import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x400")
root.title("Todo List")

tasks = []

# function definition for create task
def create_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showinfo("Message", "Please Enter a task.")

# function definition for Track task
def track_task():
    tasks = listbox.get(0, tk.END)
    if tasks:
        tasks_str = "\n".join(tasks)
        messagebox.showinfo("To-Do List", "all tasks : \n" + tasks_str)
    else:
        messagebox.showinfo("To-do List", "no tasks in list")


# function definition for Update task
def update_tasks():
    try:
        selected_task_index = listbox.curselection()[0]
        current_task = listbox.get(selected_task_index)
        new_task = entry.get()
        if new_task:
            listbox.delete(selected_task_index)
            listbox.insert(selected_task_index, new_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Information", "Please enter a new task")
    except IndexError:
        messagebox.showinfo("Information", "Please select a task to update")


entry = tk.Entry(root)
entry.pack()

button_add = tk.Button(root, 
text="Add task", command=create_task)
button_add.pack()

button_update = tk.Button(root, 
text="Update task", command=update_tasks)
button_update.pack()

button_track = tk.Button(root, 
text="Track task", command=track_task)
button_track.pack()

listbox = tk.Listbox(root)
listbox.pack()


root.mainloop()
