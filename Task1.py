import tkinter as tk

def click(button_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + button_text)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
window = tk.Tk()
window.title("Calculator by ACHMAN")
window.geometry("300x400")

# Entry widget to display the input
entry = tk.Entry(window, width=16, font=('Arial', 24), bd=5, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('Clear', 5, 0)
]

# Create buttons
for (text, row, col) in buttons:
    if text == '=':
        action = calculate
    elif text == 'C':
        action = clear
    else:
        action = lambda x=text: click(x)
    tk.Button(window, text=text, width=5, height=2, font=('Arial', 18), command=action).grid(row=row, column=col, padx=5, pady=5)


