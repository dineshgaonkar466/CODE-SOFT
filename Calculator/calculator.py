from tkinter import *

# Create main window
root = Tk()
root.title("Simple Calculator")
root.geometry("300x420")

# Entry field
entry = Entry(root, width=20, font=('Arial', 18), borderwidth=5, relief="ridge", justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Functions
def click(number):
    entry.insert(END, number)

def clear():
    entry.delete(0, END)

def backspace():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current[:-1])  # removes last character

def equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
]

# Create buttons
for (text, row, col) in buttons:
    if text == 'C':
        Button(root, text=text, width=5, height=2, bg="red", fg="white", font=('Arial', 12), command=clear).grid(row=row, column=col, padx=5, pady=5)
    else:
        Button(root, text=text, width=5, height=2, font=('Arial', 12), command=lambda t=text: click(t)).grid(row=row, column=col, padx=5, pady=5)

# Backspace and Equal buttons
Button(root, text='←', width=5, height=2, bg="gray", fg="white", font=('Arial', 12), command=backspace).grid(row=5, column=0, padx=5, pady=5)
Button(root, text='=', width=17, height=2, bg="orange", fg="white", font=('Arial', 12), command=equal).grid(row=5, column=1, columnspan=3, padx=5, pady=5)

root.mainloop()
