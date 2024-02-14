import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_Int.get()
    ans = round(mile_input * 1.61, 3)
    output_string.set(ans)

# root
root = ttk.Window(themename = "simplex")
root.title("demo")
root.geometry("400x250")
root.configure(bg = "grey13")
root.maxsize(600, 300)

# Title
title_label = ttk.Label(
    master = root,
    text = "Miles to kilometers",
    background = "#abcdef",
    foreground = "black",
    borderwidth = 0,
    font = "Calibri 24 bold",
    relief = "solid"
    )
title_label.pack(pady = 20)

# input field
input_frame = ttk.Frame(master = root, borderwidth = 10)
entry_Int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_Int)
button = ttk.Button(master = input_frame, text = "Convert", command = convert)
entry.pack(side = "left" , padx = 10, pady = 10)
button.pack(side = "left")
input_frame.pack(pady = 10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(
    master = root,
    text = "Output",
    font = "None 20",
    textvariable = output_string
)
output_label.pack(pady = 5)

# run
root.mainloop()

# Clear Code 21:30 finish