import tkinter as tk
from tkinter import ttk


# Functions #
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(number))


def clear():
    entry.delete(0, tk.END)


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, 'Error')


# Our Calculator Window #
root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 2)
]

for text, row, column in buttons:
    if text.isdigit() or text in ['+', '-', '*', '/', '.']:
        btn = ttk.Button(root, text=text, command=lambda t=text: button_click(t), width=7)
    elif text == '=':
        btn = ttk.Button(root, text=text, command=calculate, width=15)
    else:
        btn = ttk.Button(root, text=text, command=lambda t=text: clear(), width=7)
    btn.grid(row=row, column=column, padx=5, pady=5, columnspan=3 if text == '=' else 1)


style = ttk.Style()
style.configure('Rounded.TButton', boarderwidth=0, relief='flat', padding=5, borderradius=10)

for i in range(10):
    style.map(f'Rounded.TButton', foreground=[('pressed', 'white'), ('active', 'white')],
              background=[('pressed', '!disabled', 'gray'), ('active', 'gray')])

for child in root.winfo_children():
    if isinstance(child, ttk.Button):
        child.configure(style='Rounded.TButton')

# Keeps our window open while running our app #
root.mainloop()
