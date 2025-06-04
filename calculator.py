import tkinter as tk
import math

def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def equal():
    try:
        expression = entry.get()
        expression = expression.replace('√', 'math.sqrt')
        expression = expression.replace('^', '**')
        expression = expression.replace('π', str(math.pi))
        expression = expression.replace('e', str(math.e))
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "error")

def key_event(event):
    char = event.char
    if char in '0123456789+-*/().':
        press(char)
    elif event.keysym == 'Return':
        equal()
    elif event.keysym == 'BackSpace':
        entry.delete(len(entry.get())-1, tk.END)
    elif event.keysym == 'Escape':
        clear()

root = tk.Tk()
root.title("My_calculator")
root.geometry("360x500")
root.configure(bg='#2b2b2b')

entry = tk.Entry(root, font=("Consolas", 22), bd=5, relief=tk.FLAT, justify="right", bg="#1e1e1e", fg="white", insertbackground="white")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=15, sticky="nsew")

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3), ('C',1,4),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3), ('(',2,4),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3), (')',3,4),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3), ('√',4,4),
    ('π',5,0), ('e',5,1), ('^',5,2), ('log',5,3), ('ln',5,4)
]

def log():
    try:
        val = float(entry.get())
        result = math.log10(val)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "error")

def ln():
    try:
        val = float(entry.get())
        result = math.log(val)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "error")

for (text, row, col) in buttons:
    if text == "=":
        action = equal
    elif text == "C":
        action = clear
    elif text == "log":
        action = log
    elif text == "ln":
        action = ln
    else:
        action = lambda x=text: press(x)

    btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 16), command=action,
                    bg="#3c3f41", fg="white", activebackground="#505355", activeforeground="white",
                    relief=tk.FLAT, bd=1)
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

for i in range(6):
    root.grid_rowconfigure(i, weight=1)

for i in range(5):
    root.grid_columnconfigure(i, weight=1)

root.bind("<Key>", key_event)

root.mainloop()
