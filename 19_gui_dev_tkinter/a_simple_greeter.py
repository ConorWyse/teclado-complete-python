import tkinter as tk
from tkinter import ttk


def greet():
    print(f"Hello, {user_name.get() or 'World'}!")


root = tk.Tk()
root.title("Greeter")

user_name = tk.StringVar()

# Top row: text input area
input = ttk.Frame(root)
name_label = ttk.Label(input, text="Name: ")
name_entry = ttk.Entry(input, width=15, textvariable=user_name)

input.pack(side='top', fill='both', expand=True)
name_label.pack(side='left', padx=(0, 10))
name_entry.pack(side='left', expand=True)

# Bottom row: controls
greet_button = ttk.Button(root, text="Greet", command=greet)
quit_button = ttk.Button(root, text="Quit", command=root.destroy)

greet_button.pack(side='left', expand=True)
quit_button.pack(side='left', fill='x', expand=True)

root.mainloop()
