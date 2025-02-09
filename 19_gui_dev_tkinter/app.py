import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox


text_contents =  dict()


def get_current_tab():
    return notebook.nametowidget(notebook.select())


def get_text_content(text_widget) -> str:
    return text_widget.get('1.0', 'end-1c')


def get_text_widget():
    current_tab = get_current_tab()
    text_widget = current_tab.winfo_children()[0]
    return text_widget


def create_file(content='', title='Untitled'):
    container = ttk.Frame(notebook)
    container.pack()

    text_area = tk.Text(container)
    text_area.insert('end', content)
    text_area.pack(side='left', fill='both', expand=True)

    notebook.add(container, text=title)
    notebook.select(container)

    text_contents[str(text_area)] = hash(content)

    text_scroll = ttk.Scrollbar(container, orient='vertical', command=text_area.yview)
    text_scroll.pack(side='right', fill='y')
    text_area['yscrollcommand'] = text_scroll.set


def save_file():
    file_path = filedialog.asksaveasfilename()
    try:
        filename = os.path.basename(file_path)
        text_widget = get_text_widget()
        content = get_text_content(text_widget)

        with open(file_path, 'w') as file:
            file.write(content)
    
    except (AttributeError, FileNotFoundError):
        print("Save operation cancelled.")
        return

    notebook.tab('current', text=filename)
    text_contents[str(text_widget)] = hash(content)


def open_file():
    file_path = filedialog.askopenfilename()
    try:
        filename = os.path.basename(file_path)
        with open(file_path, 'r') as file:
            content = file.read()
    except (AttributeError, FileNotFoundError):
        print("Open operation cancelled.")
        return
    create_file(content, filename)


def current_tab_unsaved() -> bool:
    current = get_text_widget()
    name = notebook.tab('current')['text']
    return name[-1] == '*'


def confirm_close():
    return messagebox.askyesno(
            message='There are unsaved changes. Are you sure you want to close?',
            icon='warning',
            title='Unsaved changes'
        )


def close_current_tab():
    current = get_text_widget()
    if current_tab_unsaved() and not confirm_close():
        return
    if len(notebook.tabs()) == 1:
        create_file()
    current_tab = get_current_tab()
    notebook.forget(current_tab)
    notebook.select(0)


def check_for_changes():
    current = get_text_widget()
    content = get_text_content(current)
    name = notebook.tab('current')['text']

    if hash(content) != text_contents[str(current)]:
        if name[-1] != '*':
            notebook.tab('current', text=name + '*')
    elif name[-1] == '*':
        notebook.tab('current', text=name[:-1])


def confirm_quit():
    unsaved = False

    for tab in notebook.tabs():
        tab_widget = root.nametowidget(tab)
        text_widget = tab_widget.winfo_children()[0]
        content = get_text_content(text_widget)

        if hash(content) != text_contents[str(text_widget)]:
            unsaved = True
            break

    if unsaved:
        confirm = confirm_close()
        if confirm:
            root.destroy()
    
    return confirm


def show_about_info():
    messagebox.showinfo(
        title='About',
        message='The Teclado Text Editor is a simple text editor to help you learn about Tkinter.'
    )


root = tk.Tk()
root.title("Teclado Text Editor")
root.option_add('*tearOff', False)

menubar = tk.Menu()
file_menu = tk.Menu(menubar)
help_menu = tk.Menu(menubar)
menubar.add_cascade(menu=file_menu, label='File')
menubar.add_cascade(menu=help_menu, label='Help')
file_menu.add_command(label='New', command=create_file, accelerator='Command+N')
file_menu.add_command(label='Save', command=save_file, accelerator='Command+S')
file_menu.add_command(label='Open', command=open_file, accelerator='Command+O')
file_menu.add_command(label='Close Tab', command=close_current_tab, accelerator='Command+W')
file_menu.add_command(label='Quit', command=confirm_quit)
help_menu.add_command(label='About', command=show_about_info)

root.bind('<Command-n>', lambda event: create_file())
root.bind('<Command-o>', lambda event: open_file())
root.bind('<Command-s>', lambda event: save_file())
root.bind('<Command-w>', lambda event: close_current_tab())
root.bind('<KeyPress>', lambda event: check_for_changes())
root.config(menu=menubar)

main = ttk.Frame(root)
main.pack(fill='both', expand=True, padx=1, pady=(4,0))

notebook = ttk.Notebook(main)
notebook.pack(fill='both', expand=True)

create_file()

root.mainloop()
