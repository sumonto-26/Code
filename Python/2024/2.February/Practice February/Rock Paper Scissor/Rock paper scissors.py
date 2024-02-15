import tkinter as tk
import ttkbootstrap as ttk
from PIL import ImageTk, Image
import random


IMAGE_PATH = 'Python/2024/1. January/2.February/Rock Paper Scissor/'
DEFAULT_IMAGE = 'nothing.png'

def update_image(file_path, label):
    """Update the image displayed in the given label."""
    try:
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        label.configure(image=photo)
        label.image = photo
    except FileNotFoundError:
        pass

def set_user_choice(choice):
    """Set the user's choice and update the UI."""
    user_string.set(choice)
    photo_variable.set(choice)
    update_image(IMAGE_PATH + f'{choice}.png', photo_label)
    set_enemy_choice()

def set_enemy_choice():
    """Set the enemy's choice randomly and update the UI."""
    enemy = random.choice(["rock", "paper", "scissor"])
    enemy_variable.set(enemy)
    update_image(IMAGE_PATH + f'{enemy}.png', enemy_photo_label)
    check()

def check():
    """Check the result of the game and update the UI."""
    enemy = enemy_variable.get()
    user = user_string.get()

    if enemy == user:
        check_variable.set("Draw")
    elif (enemy == "rock" and user == "scissor") or \
         (enemy == "paper" and user == "rock") or \
         (enemy == "scissor" and user == "paper"):
        check_variable.set("You lose")
    else:
        check_variable.set("You Win")

root = ttk.Window(themename="darkly")
root.geometry("900x600")
root.minsize(700, 400)
# root.maxsize(900, 600)


title = ttk.Label(master = root, text = "Rock Paper Scissors", background = "lightgreen", foreground = "black", font = "None 25 bold")
title.pack()

check_variable = tk.StringVar()
label = ttk.Label(text = "", font = "none 30 bold", textvariable = check_variable)
label.pack(pady=20)

items = ["rock", "paper", "scissor"]
user_string = tk.StringVar()
enemy_variable = tk.StringVar()
photo_variable = tk.StringVar()

# Make buttons
button1 = ttk.Button(master = root, text = "Rock", command = lambda: set_user_choice('rock'), style = "success-toolbutton")
button1.pack(side = "bottom", anchor = "n", fill = "x", padx = 150)

button2 = ttk.Button(master = root, text = "Paper", command = lambda: set_user_choice('paper'), style = "success-toolbutton")
button2.pack(side = "bottom", anchor = "n", fill = "x", padx = 150, pady = 2)

button3 = ttk.Button(master = root, text = "Scissor", command = lambda: set_user_choice('scissor'), style = "success-toolbutton")
button3.pack(side = "bottom", anchor = "n", fill = "x", padx = 150)


you_label = tk.Label(root, text = "You", font = "none 20 bold")
you_label.pack(side = "left", anchor = "e", padx = 50)

enemy_label = tk.Label(root, text = "Enemy", font = "none 20 bold")
enemy_label.pack(side = "right", anchor = "e", padx = 50)

photo_label = tk.Label(root)
photo_label.pack(side = "left", anchor = "e", padx = 10)

enemy_photo_label = tk.Label(root)
enemy_photo_label.pack(side = "right", anchor = "e", padx = 10)

update_image(IMAGE_PATH + DEFAULT_IMAGE, photo_label)
update_image(IMAGE_PATH + DEFAULT_IMAGE, enemy_photo_label)

root.mainloop()