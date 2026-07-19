from tkinter import *

root = Tk()
root.title("Advanced Calculator")
root.geometry("350x500")

# Entry box
entry = Entry(root, width=25, borderwidth=5, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Function to click buttons
def click(value):
    entry.insert(END, value)

# Clear function
def clear():
    entry.delete(0, END)

# Calculate result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+', '='
]

row = 1
col = 0

for button in buttons:
    if button == "=":
        Button(root, text=button, padx=25, pady=25,
               command=calculate).grid(row=row, column=col)
    else:
        Button(root, text=button, padx=25, pady=25,
               command=lambda b=button: click(b)).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
Button(root, text="Clear", padx=25, pady=25,
       command=clear).grid(row=row, column=0, columnspan=4, sticky="we")

root.mainloop()
