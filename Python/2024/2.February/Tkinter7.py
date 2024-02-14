import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("900x550")
root.minsize(800, 450)
root.maxsize(1000, 600)
root.title("Combo and Spin")

# combobox
items = (
    "cerculean",
    "cosmo",
    "cyborg",
    "darkly",
    "flatly",
    "journal",
    "litera",
    "lumen",
    "minty",
    "morph",
    "pulse",
    "sandstone",
    "simplex",
    "solar",
    "superhero",
    "united",
    "vapor",
    "yeti",
)

item_string = tk.StringVar(value = items[0])
combo = ttk.Combobox(master = root, textvariable = item_string)

# combo["values"] = items
combo.configure(values = items)

combo.pack()

# events
combo_label = ttk.Label(master = root, text = items[0], textvariable = item_string, font = "none 30 bold", background = "lightgreen")
combo_label.pack(pady = 0)




# SPINBOX
spin_int = tk.IntVar(value = 1)

spin = ttk.Spinbox(
    master = root,
    from_ = 1,
    to = 10,
    increment = 1,
    textvariable = spin_int
    )

spin_label_number = ttk.Label(
    master = root,
    textvariable = spin_int,
    font = "none 20 bold",
    background = "lightblue"
    )



arrow_string = tk.StringVar()

spin_label_arrow = ttk.Label(
    master = root,
    text = "nothing",
    font = "none 20 bold",
    background = "grey13",
    foreground = "white",
    textvariable = arrow_string
)
spin_label_arrow.pack(pady = 50 )


# spin['value'] = (1,2,3,4,5)
spin.bind("<<Increment>>", lambda event: arrow_string.set("UP"))
spin.bind("<<Decrement>>", lambda event: arrow_string.set("DOWN"))
spin.pack(pady = 50)
spin_label_number.pack(pady = 30)


'''# Exersise:
exersise_letters = ("A", "B", "C", "D", "E")
exersise_string = tk.StringVar(value = exersise_letters[0])
# exersise_spin = tk.Spinbox(master = root, textvariable = exersise_string)
# exersise_spin["values"] = exersise_letters
exersise_spin = ttk.Spinbox(master = root, textvariable = exersise_string, values = exersise_letters)
exersise_spin.pack()

exersise_spin.bind("<<Decrement>>", lambda event: print(exersise_string.get()))
'''

# run
root.mainloop()