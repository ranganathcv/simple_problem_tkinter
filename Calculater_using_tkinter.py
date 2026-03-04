import tkinter as tk


current_input = ""
first_number = 0
operation = None
should_reset = False


root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill="x", padx=10, pady=10)



def update_display(value):
    entry.delete(0, tk.END)
    entry.insert(0, value)

def number_click(num):
    global current_input, should_reset

    if should_reset:
        current_input = ""
        should_reset = False

    current_input += str(num)
    update_display(current_input)

def operation_click(op):
    global first_number, operation, current_input, should_reset

    if current_input != "":
        first_number = float(current_input)

    operation = op
    should_reset = True

def calculate():
    global first_number, operation, current_input, should_reset

    try:
        second_number = float(current_input)

        if operation == "+":
            result = first_number + second_number

        elif operation == "-":
            result = first_number - second_number

        elif operation == "*":
            result = first_number * second_number

        elif operation == "/":
            if second_number == 0:
                update_display("Cannot divide by zero")
                return
            result = first_number / second_number

        update_display(result)
        current_input = str(result)
        should_reset = True

    except:
        update_display("Error")

def clear():
    global current_input, first_number, operation

    current_input = ""
    first_number = 0
    operation = None
    update_display("")



frame = tk.Frame(root)
frame.pack()

buttons = [
    ('7', lambda: number_click(7)), ('8', lambda: number_click(8)), ('9', lambda: number_click(9)), ('/', lambda: operation_click('/')),
    ('4', lambda: number_click(4)), ('5', lambda: number_click(5)), ('6', lambda: number_click(6)), ('*', lambda: operation_click('*')),
    ('1', lambda: number_click(1)), ('2', lambda: number_click(2)), ('3', lambda: number_click(3)), ('-', lambda: operation_click('-')),
    ('0', lambda: number_click(0)), ('C', clear), ('=', calculate), ('+', lambda: operation_click('+'))
]

row = 0
col = 0

for (text, func) in buttons:
    tk.Button(frame, text=text, width=5, height=2, font=("Arial", 14),
              command=func).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()