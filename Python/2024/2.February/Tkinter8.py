import tkinter as tk
from tkinter import ttk

# setup 
root = tk.Tk()
root.geometry("850x650")
root.maxsize(1000, 800)
root.minsize(700, 500)


root.title("Canvas")


# Canvas
# canvas = tk.Canvas(master = root, background = "lightyellow")
canvas = tk.Canvas(master = root, width = 700, height = 500, background = "#abcdef")
canvas.pack()

# DRAW RECTANGLE
# canvas.create_rectangle((top, left, bottom, right))
# canvas.create_rectangle((10, 100, 250, 250), fill = "lightgreen", width = 20)
# canvas.create_rectangle((100, 100, 200, 250), fill = "lightgreen", width = 10, dash = (1, 2, 3, 4...))
canvas.create_rectangle((100, 100, 200, 250), fill = "lightgreen", width = 10, dash = (1, 2, 1,2), outline = "darkgreen")


# DRAW OVAL
# canvas.create_oval(left, top, right, bottom)
# canvas.create_oval((100, 300, 200, 400))
# canvas.create_oval((100, 300, 200, 400), fill = "yellow")
# canvas.create_oval((100, 300, 200, 400), fill = "yellow", width = 10)
# canvas.create_oval((100, 300, 200, 400), fill = "yellow", width = 10, dash = (1, 2, 3, 4,...))
canvas.create_oval((100, 300, 200, 400), fill = "yellow", width = 5, dash = (1, 2, 3, 4), outline = "blue")

# DRAW ARC
# canvas. create_arc(left, top, right, bottom)
# canvas.create_arc((200, 400, 300, 500))
# canvas.create_arc((200, 400, 300, 500), fill = "red")
# canvas.create_arc((200, 400, 300, 500), fill = "red", width = 10)
# canvas.create_arc((200, 400, 300, 500), fill = "red", width = 10, dash = (1, 2, 3, 4,...)
# canvas.create_arc((200, 400, 300, 500), fill = "red", width = 10, dash = (1, 2, 3, 4), outline = "darkgreen")
# canvas.create_arc((200, 400, 300, 500), fill = "red", width = 10, dash = (1, 2, 3, 4), outline = "darkgreen", start = 45)
# canvas.create_arc((200, 400, 300, 500), fill = "red", width = 10, dash = (1, 2, 3, 4), outline = "darkgreen", start = 45, extent = 180)
canvas.create_arc((200, 400, 300, 500), fill = "red", width = 10, dash = (1, 2, 3, 4), outline = "darkgreen", start = 45, extent = 180, style = tk.ARC)



# DRAW POLYGON
# canvas.create_polygon((x1,y1, x2,y2, x3,y3,....))
# canvas.create_polygon((400,350, 430,200, 550,250, 450,450))
# canvas.create_polygon((400,350, 430,200, 550,250, 450,450), fill = "blue")
canvas.create_polygon((400,350, 430,200, 550,250, 450,450), fill = "blue")

# DRAW LINE
# canvas.create_line((start_x, start_y, end_x , end_y))
# canvas.create_line((100, 50, 500 , 50))
# canvas.create_line((100, 50, 500 , 50), fill = "green")
canvas.create_line((100, 50, 500 , 50), fill = "green", width = 10)

# DRAW TEXT
# canvas.create_text((x, y), text = "Any string")
# canvas.create_text((300, 200), text = "Any string")
canvas.create_text((300, 200), text = "Any string", fill = "red", width = 10)

canvas.create_window((600, 350), window = ttk.Label(master = root, text = "this is text in a canvas"))


# EXERSISE

def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval((x-brush_sise/2, y-brush_sise/2, x+brush_sise/2, y+brush_sise/2), fill = "black", width = 2)

def brush_size_adjust(event):
    global brush_sise
    if event.delta > 0:
        brush_sise += 4
    else:
        brush_sise -= 4
    
    brush_sise = max(0,min(brush_sise , 100))
    # print(event)
    

brush_sise = 10
canvas.bind("<Motion>", draw_on_canvas)
canvas.bind("<MouseWheel>", brush_size_adjust)


# Run
root.mainloop()