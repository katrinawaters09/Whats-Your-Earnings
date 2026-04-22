import tkinter as tk

# -----------------------------
# Window
# -----------------------------
window = tk.Tk()
window.title("Payday Calculator")
window.geometry("420x650")

# -----------------------------
# Variables
# -----------------------------
display_text = tk.StringVar()
display_text.set("Hourly Rate: ")

selected_state = tk.StringVar()
selected_state.set("Michigan")

state_tax_rates = {
"Alabama": 5.0,
"Alaska": 0.0,
"Arizona": 2.5,
"Arkansas": 3.9,
"California": 8.0,
"Colorado": 4.4,
"Connecticut": 6.0,
"Delaware": 5.0,
"Florida": 0.0,
"Georgia": 5.2,
"Hawaii": 8.5,
"Idaho": 5.3,
"Illinois": 4.95,
"Indiana": 3.0,
"Iowa": 3.8,
"Kansas": 5.6,
"Kentucky": 4.0,
"Louisiana": 3.0,
"Maine": 7.0,
"Maryland": 5.5,
"Massachusetts": 5.0,
"Michigan": 4.25,
"Minnesota": 7.0,
"Mississippi": 4.0,
"Missouri": 4.7,
"Montana": 5.5,
"Nebraska": 4.5,
"Nevada": 0.0,
"New Hampshire": 0.0,
"New Jersey": 6.5,
"New Mexico": 5.0,
"New York": 7.5,
"North Carolina": 4.25,
"North Dakota": 2.5,
"Ohio": 2.75,
"Oklahoma": 4.5,
"Oregon": 8.0,
"Pennsylvania": 3.07,
"Rhode Island": 5.0,
"South Carolina": 6.0,
"South Dakota": 0.0,
"Tennessee": 0.0,
"Texas": 0.0,
"Utah": 4.5,
"Vermont": 6.5,
"Virginia": 5.75,
"Washington": 0.0,
"West Virginia": 4.8,
"Wisconsin": 5.5,
"Wyoming": 0.0
}


hourly_rate = ""
hours_worked = ""
tax_percent_manual = ""
current_field = "rate"
# -----------------------------
# Functions
# -----------------------------
def update_display():
    if current_field == "rate":
        if hourly_rate == "":
            display_text.set("Hourly Rate: ")
        else:
            display_text.set("Hourly Rate: " + hourly_rate)
    elif current_field == "hours":
        if hours_worked == "":
         display_text.set("Hours Worked:")
        else:
            display_text.set("Hours Worked:" + hours_worked)
    elif current_field == "tax":
        if tax_percent_manual == "":
            display_text.set("Tax %:" \
            "")
        else:
            display_text.set("Tax %: " + tax_percent_manual)


def press_number(num):
    global hourly_rate, hours_worked, tax_percent_manual

    if current_field == "rate":
        hourly_rate += str(num)
    elif current_field == "hours":
        hours_worked += str(num)
    elif current_field == "tax":
        tax_percent_manual += str(num)

    update_display()


def press_decimal():
    global hourly_rate, hours_worked, tax_percent_manual

    if current_field == "rate":
        if "." not in hourly_rate:
            if hourly_rate == "":
                hourly_rate = "0."
            else:
                hourly_rate += "."

    elif current_field == "hours":
        if "." not in hours_worked:
            if hours_worked == "":
                hours_worked = "0."
            else:
                hours_worked += "."

    elif current_field == "tax":
        if "." not in tax_percent_manual:
            if tax_percent_manual == "":
                tax_percent_manual = "0."
            else:
                tax_percent_manual += "."

    update_display()


def select_rate():
    global current_field
    current_field = "rate"
    update_display()


def select_hours():
    global current_field
    current_field = "hours"
    update_display()


def select_tax():
    global current_field
    current_field = "tax"
    update_display()
 

def clear_all():
    global hourly_rate, hours_worked, tax_percent_manual, current_field
    hourly_rate = ""
    hours_worked = ""
    tax_percent_manual = ""
    current_field = "rate"
    display_text.set("Hourly Rate: ")
    result_label.config(text="")


def backspace():
    global hourly_rate, hours_worked, tax_percent_manual

    if current_field == "rate":
        hourly_rate = hourly_rate[:-1]
    elif current_field == "hours":
        hours_worked = hours_worked[:-1]
    elif current_field == "tax":
        tax_percent_manual = tax_percent_manual[:-1]

    update_display()


def calculate_pay():
    if hourly_rate == "" or hours_worked == "":
        result_label.config(text="Enter hourly rate and hours worked")
        return
    try:
        rate = float(hourly_rate)
        hours = float(hours_worked)
    except ValueError:
        result_label.config(text="Invalid input for hourly rate or hours worked")
        return

    chosen_state = selected_state.get()

    if tax_percent_manual == "":
        tax_percent = state_tax_rates.get(chosen_state, 0)
    else:
        try:
            tax_percent = float(tax_percent_manual)
        except ValueError:
            result_label.config(text="Invalid input for tax percentage")
            return

    gross_pay = rate * hours
    tax_amount = gross_pay * (tax_percent / 100)
    net_pay = gross_pay - tax_amount

    result_label.config(
        text="State: " + chosen_state +
            "\nTax %: " + str(tax_percent) +
            "\nGross Pay: $" + str(round(gross_pay, 2)) +
            "\nTax Amount: $" + str(round(tax_amount, 2)) +
            "\nNet Pay: $" + str(round(net_pay, 2))
)

# -----------------------------
# Display
# -----------------------------
display = tk.Entry(
window,
textvariable=display_text,
font=("Arial", 22),
justify="right",
bd=10,
relief="sunken"
)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# -----------------------------
# State dropdown
# -----------------------------
state_menu = tk.OptionMenu(window, selected_state, * state_tax_rates.keys())
state_menu.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

# -----------------------------
# Input buttons row
# -----------------------------
hourly_button = tk.Button(window, text="Hourly Rate", font=("Arial", 12), command=select_rate)
hourly_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

hours_button = tk.Button(window, text="Hours Worked", font=("Arial", 12), command=select_hours)
hours_button.grid(row=2, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")

# -----------------------------
# Tax / Clear / Backspace row
# -----------------------------
tax_button = tk.Button(window, text="Tax %", font=("Arial", 12), command=select_tax)
tax_button.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

clear_button = tk.Button(window, text="Clear", font=("Arial", 12), command=clear_all)
clear_button.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

back_button = tk.Button(window, text="⌫", font=("Arial", 12), command=backspace)
back_button.grid(row=3, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")

# -----------------------------
# Number pad
# -----------------------------
tk.Button(window, text="7", font=("Arial", 16), command=lambda: press_number(7)).grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
tk.Button(window, text="8", font=("Arial", 16), command=lambda: press_number(8)).grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
tk.Button(window, text="9", font=("Arial", 16), command=lambda: press_number(9)).grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

tk.Button(window, text="4", font=("Arial", 16), command=lambda: press_number(4)).grid(row=5, column=0, padx=5, pady=5, sticky="nsew")
tk.Button(window, text="5", font=("Arial", 16), command=lambda: press_number(5)).grid(row=5, column=1, padx=5, pady=5, sticky="nsew")
tk.Button(window, text="6", font=("Arial", 16), command=lambda: press_number(6)).grid(row=5, column=2, padx=5, pady=5, sticky="nsew")

tk.Button(window, text="1", font=("Arial", 16), command=lambda: press_number(1)).grid(row=6, column=0, padx=5, pady=5, sticky="nsew")
tk.Button(window, text="2", font=("Arial", 16), command=lambda: press_number(2)).grid(row=6, column=1, padx=5, pady=5, sticky="nsew")
tk.Button(window, text="3", font=("Arial", 16), command=lambda: press_number(3)).grid(row=6, column=2, padx=5, pady=5, sticky="nsew")

tk.Button(window, text="0", font=("Arial", 16), command=lambda: press_number(0)).grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
tk.Button(window, text=".", font=("Arial", 16), command=press_decimal).grid(row=7, column=2, padx=5, pady=5, sticky="nsew")

# -----------------------------
# Calculate button
# -----------------------------
calculate_button = tk.Button(window, text="Calculate Pay", font=("Arial", 14), command=calculate_pay)
calculate_button.grid(row=4, column=3, rowspan=4, padx=5, pady=5, sticky="nsew")

# -----------------------------
# Result label
# -----------------------------
result_label = tk.Label(window, text="", font=("Arial", 13), justify="left")
result_label.grid(row=8, column=0, columnspan=4, padx=10, pady=15, sticky="nsew")

# -----------------------------
# Grid expand
# -----------------------------
for i in range(9):
    window.grid_rowconfigure(i, weight=1)

for j in range(4):
     window.grid_columnconfigure(j, weight=1)


def key_input(event):
    global current_field

    key = event.char

    if key.isdigit():
        press_number(int(key))

    elif key == ".":
        press_decimal()

    elif event.keysym == "BackSpace":
        backspace()

    elif event.keysym == "Return":
        if current_field == "rate":
            select_hours()
        elif current_field == "hours":
            calculate_pay()
        elif current_field == "tax":
            calculate_pay()

window.bind("<Key>", key_input)


window.mainloop()
