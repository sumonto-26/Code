'''import tkinter
from PIL import Image, ImageTk

root = tkinter.Tk()

# "Width X Height"
root.geometry("800x534") # First Size

photo = tkinter.PhotoImage(file='Python/2024/1. January/2.February/teddy-bear.png')

photo_label = tkinter.Label(image=photo)
photo_label.pack()

# Width, Height
root.minsize(300,300)
# Width, Height
root.maxsize(933,600)

# gui logic
root.mainloop()'''

"""import tkinter

root = tkinter.Tk()
root.geometry("733x434")
root.title("My GUI")

# fill background
root.configure( bg = "grey")

'''# Important Label Options:

    # text - Adds the text to the label
    # bg - Background color
    # fg - Foreground color
    
    # font - Sets the font 
    # (Examples: ('comicsansms', 25, 'bold') or 'comicsansms 19 bold')
    
    # padx - Horizontal padding
    # pady - Vertical padding
    # relief - Border styling ('sunken', 'raised', 'groove', 'ridge', 'flat', 'solid')
    # width - Sets the width of the label
    # height - Sets the height of the label
    # anchor - Alignment within the label ('n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw', 'center')
    # underline - Index of the character to be underlined in the text
    # wraplength - Maximum line length for word wrapping
    # justify - Alignment of multiple lines ('left', 'center', 'right')
    # cursor - Cursor style when hovering over the label ('arrow', 'hand2', 'xterm')
'''

title_label4 = tkinter.Label(
    text="The quick brown fox jumps over the lazy dog",
    bg='lightblue',
    fg='black',
    padx=20,
    pady=10,
    font=('Helvetica', 20, 'italic'),
    borderwidth = 10,
    relief="ridge",
    width=20,
    height=3,
    anchor='w',
    underline = 0,
    wraplength = 1000,
    justify='right',
    cursor='arrow'
    )

'''# Important Pack Options:
    # anchor = n, ne, e, se, s, sw, w, nw, or center
    # side = top, bottom, left or right
    
    # fill = 'x' or 'y'
    # NOTE: If fill == 'x', then side should be 'bottom' or 'top'; otherwise, it won't work.
    # NOTE: If fill == 'y', then side should be 'left' or 'right'; otherwise, it won't work.
    
    # padx = Horizontal padding
    # pady = Vertical padding)'''

title_label4.pack(
    anchor='center',
    side='bottom',
    fill='x',
    padx=10,
    pady = 120
    )

root.mainloop()
"""

# video 9
"""import tkinter

root = tkinter.Tk()

root.configure(bg ="lightgray")
root.title("Basic Tkiner code")
root.geometry("793x498")
root.minsize(400,400)
root.maxsize(900,800)

f1 = tkinter.Frame(root , bg = "lightgreen", borderwidth = 5, relief='solid')
f1.pack(side="left",fill="y")

f2 = tkinter.Frame(root, borderwidth=8, bg="lightgreen", relief="solid")
f2.pack(side="top", fill="x", padx=5)

l = tkinter.Label(f1, text = "Any option", font="None 20 bold")
l.pack(side="top", pady=5)

l = tkinter.Label(f2, text = "Welcome to my code", font="None 15 bold",bg = "lightgreen", fg = "black", pady=2)
l.pack()

root.mainloop()"""


# video 10
import tkinter
import ttkbootstrap

# Constants
BUTTON_SIZE = 20
FRAME_BORDER_WIDTH = 15
FRAME_PADDING_Y = 10
BACKGROUND_COLOR = "grey14"

# Basic setup
root = ttkbootstrap.Window(themename = "vapor")
root.configure( bg = BACKGROUND_COLOR)
root.title("MY FIRST TKINTER PROJECT")
root.geometry("100x500")
root.minsize(600, 400)
root.maxsize(1000, 600)

# Create short cuts
def create_label(text):
    label = tkinter.Label(text = text, fg = "white", bg = BACKGROUND_COLOR, font = ("Optima", 25, "bold"))
    label.pack(side = "left", anchor = "ne")

def create_button(text, command, size):
    button = tkinter.Button(frame, fg = "white", bg = "#575757", text = text, font = ("none", size, "bold"), command = command)
    button.pack(side = "left", anchor = "nw", padx = 5)

def button_0():
    create_label("0")

def button_1():
    create_label("kljlkjh")

def button_2():
    create_label("2")

def button_3():
    create_label("3")

def button_4():
    create_label("4")

def button_5():
    create_label("5")

def button_6():
    create_label("6")

def button_7():
    create_label("7")

def button_8():
    create_label("8")

def button_9():
    create_label("9")

def space():
    create_label(" ")

# Create the frame
frame = tkinter.Frame(master = root, borderwidth = FRAME_BORDER_WIDTH, bg = "black", relief = "ridge")
frame.pack(side = "bottom", pady = FRAME_PADDING_Y)

# Button data
buttons_data = [
    ("1", button_1), ("2", button_2), ("3", button_3),
    ("4", button_4), ("5", button_5), ("6", button_6),
    ("7", button_7), ("8", button_8), ("9", button_9),
    ("0", button_0), ("_", space)
]

# Create buttons
for text, function_name in buttons_data:
    create_button(text, function_name, BUTTON_SIZE)


root.mainloop()



'''import tkinter


def get_values():
    print(f"Your Name ===> {user_value.get()}")
    print(f"Your Password ===> {pass_value.get()}")


background_color = "#abcdef"

root = tkinter.Tk()
root.geometry("800x500")
root.configure(bg = background_color)
root.title("code with harry's tkinter course video 11")
root.maxsize(1100, 700)
root.minsize(500, 300)

def create_label(text, row, column):
    variable = tkinter.Label(root, text = text, font= ("none", 15, "bold"), bg = background_color)
    variable.grid(row = row, column = column)

create_label("User Name", 1, 0)
create_label("User Password", 2, 0)


user_value = tkinter.StringVar()
pass_value = tkinter.StringVar()

user_entry = tkinter.Entry(root, textvariable= user_value)
pass_entry = tkinter.Entry(root, textvariable= pass_value)

user_entry.grid(row=1, column=1)
pass_entry.grid(row=2, column=1)

# There are 4 types of Variable Class
# 1. BooleanVar,
# 2. DoubleVar,
# 3. IntVar,
# 4. StringVar

tkinter.Button(text="Submit", bg="light green", command = get_values).grid(row=3,column=3)

root.mainloop()'''