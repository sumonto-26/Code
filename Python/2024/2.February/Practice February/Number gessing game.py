import tkinter as tk
from tkinter import ttk
import random
import pyttsx3

root = tk.Tk()
root.geometry("900x500")
root.minsize(800, 400)
root.maxsize(1000, 600)





def check():
    num = random.randint(1, 1000)
    print(num)

    try:
        user_number = int(entry.get())
        if user_number == num:
            print("corect answer")
            num = random.randint(1, 1000)
            print(num)
            label["text"] = ""
        elif user_number < num:
            print("low")
        elif user_number > num:
            print("high")
    except ValueError:
        print("type a number not string")


# make label
label = ttk.Label(master = root, text = "", font = "none 35 bold")
label.pack()

# make entry
entry = ttk.Entry(master = root)
entry.pack()

# make button
button = ttk.Button(master = root, text = "submit", command = check)
button.pack()

# restart_button = ttk.Button(master = root, text = "restart", command = restart)
# restart_button.pack(side = "bottom", anchor = "e", padx = 30, pady = 20)

root.mainloop()