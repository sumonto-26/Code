# Sliders
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

root = tk.Tk()
root.geometry("700x600")
root.title("Sliders")
root.minsize(600, 400)
# root.maxsize(900, 600)

# SLIDERS WIDGETS
# scale = ttk.Scale(root)
"""
ERROR
scale = ttk.Scale(root, command = lambda: print("test"))
ERROR
"""
# scale_int = tk.IntVar(value=400)
scale_float = tk.DoubleVar(value = 100)
scale_vertical = ttk.Scale(
    master = root,
    # command = lambda value: print(value),
    length = 50, # width of the Scale
    from_= 0,
    to = 200,
    orient = "vertical", # scale is "vertical" or "horizontal"
    variable = scale_float,
        command = lambda value: progress2.stop()

    )
scale_vertical.pack(pady=50)

scale_horizontal = ttk.Scale(
    master = root,
    # command = lambda value: print(value),
    length = 400, # width of the Scale
    from_= 0,
    to = 200,
    orient = "horizontal", # scale is "vertical" or "horizontal"
    variable = scale_float,
    command = lambda value: progress2.start()

    )

scale_horizontal.pack()


# Progress Bar
progress1 = ttk.Progressbar(
    master = root, 
    variable = scale_float,
    maximum = 200,
    orient = "vertical",
    mode = "indeterminate"
    )
progress1.pack()


progress2 = ttk.Progressbar(
    master = root, 
    variable = scale_float,
    maximum = 200,
    orient = "horizontal",
    mode = "determinate",
    length = 400
    )
progress2.pack()
progress2.start(300) # 30 miliseconds
# progress2.stop()

# scrolledtext
scroll = scrolledtext.ScrolledText(master = root, width = 70, height = 3)
scroll.pack()

# EXERSISE
exersise_int = tk.IntVar()
exersise_progress = ttk.Progressbar(master = root, orient = "vertical", variable = exersise_int)
exersise_progress.start(150)
exersise_progress.pack()

exersise_label = ttk.Label(master = root, textvariable = exersise_int, font = "none 15 bold")
exersise_label.pack()

exersise_scale = ttk.Scale(master = root, from_ = 0, to = 100, length = 100, variable = exersise_int)
exersise_scale.pack()


root.mainloop()