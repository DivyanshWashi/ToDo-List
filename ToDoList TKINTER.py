import tkinter as tk
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
def remove_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except:
        pass
def mark_complete():
    try:
        index = listbox.curselection()[0]
        listbox.itemconfig(index, {'bg':'lightgreen'})
    except:
        pass
root = tk.Tk()
root.title("To-Do List")
entry = tk.Entry(root, width=50)
entry.pack(pady=10)
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)
complete_button = tk.Button(root, text="Mark as Completed", command=mark_complete)
complete_button.pack(pady=5)
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

root.mainloop()
