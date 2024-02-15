# Date ==> 15 February 2024
# import tkinter as tk
import ttkbootstrap as ttk
import random

root = ttk.Window(themename="darkly")
root.title("Number Gessing game.")
root.geometry("900x600")
root.minsize(800, 500)
root.maxsize(950, 600)

# Initialize num as a global variable
num = 0

def generate_random_number():
    global num
    num = random.randint(1, 1000)

def check():
    try:
        label["text"] = "..."
        root.after(500, check_result)  # Schedule check_result after 500 milliseconds
    except ValueError:
        label["text"] = "Type error Type a number."
        label["foreground"] = "red"

def check_result():
    try:
        user_number = int(entry.get())
        if user_number == num:
            label["text"] = "Correct answer!"
            label["foreground"] = "lightgreen"
        elif user_number < num:
            label["text"] = "Too low!"
            label["foreground"] = "red"
        elif user_number > num:
            label["text"] = "Too high!"
            label["foreground"] = "red"
    except ValueError:
        label["text"] = "Type error Type a number."
        label["foreground"] = "red"

# make label
label1 = ttk.Label(master=root, text="Guess the number:", font="none 15 bold")
label1.pack(pady=10)

# make entry
entry = ttk.Entry(master=root)
entry.pack()

# make button to submit
button = ttk.Button(master=root, text="Submit", command=check)
button.pack(pady=10)

# make label
label = ttk.Label(master=root, text="", font="none 35 bold")
label.pack(pady=50)

# make button to generate a new random number
restart_button = ttk.Button(master=root, text="Generate New Number", command=generate_random_number)
restart_button.pack(side="bottom", anchor="e", padx=30, pady=20)

# Initialize num when the program starts
generate_random_number()

root.mainloop()
