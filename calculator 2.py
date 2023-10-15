import tkinter as tk
import math

def calculate():
    try:
        expression = entry.get()
        expression = expression.replace('√', 'math.sqrt')
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    if number == '√':
        entry.insert(0, current + '√(')
    elif number == 'X':
        entry.insert(0, current[:-1])
    elif number == '(':
        entry.insert(0, current + '(')
    elif number == ')':
        entry.insert(0, current + ')')
    else:
        entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+',
    '√', 'X', '(', ')'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 20), command=calculate).grid(row=row_val, column=col_val)
    elif button == 'C':
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 20), command=clear).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 20), command=lambda num=button: button_click(num)).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
