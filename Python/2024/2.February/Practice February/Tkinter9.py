import tkinter as tk
import random
from tkinter import ttk

# setup
root = tk.Tk()
root.geometry("800x600")
root.title("Treeview")
root.maxsize(1000, 800)
root.minsize(600, 400)

# TREEVIEW

# data
animal_name = ["Lion", "Elephant", "Tiger","Giraffe",
        "Penguin", "Dolphin","Kangaroo", "Cheetah",
        "Panda"]

animal_habitat = ["Grasslands", "Jungle", "Jungle", "Savannah"
        "Polar", "Ocean", "Desert", "Grasslands", "Mountain"]

animal_favorite_foods = [
    "Wildebeest",
    "Grass, fruits, and bark",
    "Deer, and various ungulates",
    "Acacia leaves and buds",
    "Fish and squid", 
    "Fish and squid",
    "Grass and vegetation",
    "deer, impalas, and smaller ungulates",
    "Bamboo leaves and shoots"]

tree = ttk.Treeview(master = root, columns = ("Animal", "Habitat", "Favorite food"), show = 'headings')
tree.heading("Animal", text = "Animal name")
tree.heading("Habitat", text = "Animal Habitat")
tree.heading("Favorite food", text = "Animal favorite foods")
# tree.pack()
tree.pack(fill = "both", expand = True)

for _ in range(100):
    name = random.choice(animal_name)
    habitat = random.choice(animal_habitat)
    favorite_foods = random.choice(animal_favorite_foods)
    data = (name, habitat, favorite_foods)
    tree.insert(parent = "", index = 0, values = data)

# tree.insert(parent = "", index = 0, values = ("pyhon", "Computer", "PYGAME"))
tree.insert(parent = "", index = tk.END, values = ("pyhon", "Computer", "PYGAME"))


# EVENTS
# tree.bind("<<TreeviewSelect>>", lambda event: print(event))
# tree.bind("<<TreeviewSelect>>", lambda event: print(tree.selection()))
def item_select(_):
    # print(tree.selection)
    for i in tree.selection():
        print(f"Data == {tree.item(i)["values"]}")
    # tree.item(tree.selection())
    
def delete_items(_):
    # tree.delete(item)
    for i in tree.selection():
        print(f"Delete {tree.item(i)["values"]}")
        tree.delete(i)
    
tree.bind("<<TreeviewSelect>>", item_select)
tree.bind("<Delete>", delete_items)


# run
root.mainloop()