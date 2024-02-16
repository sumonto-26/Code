import tkinter as tk
from tkinter import ttk

def calculate_bmi():
    try:
        width_value = float(width_entry.get())
        height_value = float(height_entry.get())

        if width_string.get() == "pound" and height_string.get() == "inches":
            ans = 703 * (width_value / (height_value ** 2))
        elif width_string.get() == "pound" and height_string.get() == "meter":
            ans = 703 * (width_value / ((height_value * 39.3701) ** 2))
        elif width_string.get() == "pound" and height_string.get() == "centimeter":
            ans = 703 * (width_value / ((height_value * 0.393701) ** 2))

        elif width_string.get() == "kilogram" and height_string.get() == "inches":
            ans = width_value / ((height_value * 0.0254) ** 2)
        elif width_string.get() == "kilogram" and height_string.get() == "meter":
            ans = width_value / (height_value ** 2)
        elif width_string.get() == "kilogram" and height_string.get() == "centimeter":
            ans = width_value / ((height_value * 0.01) ** 2)

        bmi_result.set(f"Your BMI is: {ans:.2f}")

    except ValueError:
        bmi_result.set("Please enter valid numeric values")

root = tk.Tk()
root.geometry("600x550")
root.title("BMI Calculator")
root.resizable(False, False)
root.configure(bg = "grey15")

label1 = tk.Label(
    master = root,
    background = "lightblue",
    height = 2,
    font = "None 20 bold"
)
label1.pack(fill = 'x', padx = 5, pady = 5)

label2 = tk.Label(
    master = root,
    text = "BMI Calculator",
    background = "lightblue",
    foreground = "grey13",
    font = "None 20 bold"
)
label2.place(x = 10, y = 20)

label3 = tk.Label(
    master = root,
    text = "Width",
    background = "lightblue",
    foreground = "grey13",
    font = "None 15 bold"
)
label3.place(x = 50, y = 170)

label4 = tk.Label(
    master = root,
    text = "Height",
    background = "lightblue",
    foreground = "grey13",
    font = "None 15 bold"
)
label4.place(x = 50, y = 225)

height_types = [
    "inches",
    "meter",
    "centimeter"
]
width_types = [
    "kilogram",
    "pound"
]

width_string = tk.StringVar()
width_com = ttk.Combobox(master = root, width = 10, textvariable = width_string, font = "none 15 bold")
width_com["values"] = width_types
width_com.place(x = 400, y = 170)

height_string = tk.StringVar()
height_com = ttk.Combobox(master = root, width = 10, textvariable = height_string, font = "none 15 bold")
height_com.configure(values = height_types)
height_com.place(x = 400, y = 225)

width_entry = ttk.Entry(master = root, font = "none 12 bold")
width_entry.place(x = 175, y = 172)

height_entry = ttk.Entry(master = root, font= "none 12 bold")
height_entry.place(x = 175, y = 227)

bmi_result = tk.StringVar()
result_label = tk.Label(
    master = root,
    textvariable = bmi_result,
    background = "lightblue",
    foreground = "grey13",
    font = "None 20 bold"
)
result_label.place(x = 150, y = 355)

submit_button = tk.Button(
    master = root,
    text = "Submit",
    font = "none 15 bold",
    background = "lightgreen",
    command = calculate_bmi  
)
submit_button.pack(side = "bottom", anchor = "e", padx = 10, pady = 10)

root.mainloop()
