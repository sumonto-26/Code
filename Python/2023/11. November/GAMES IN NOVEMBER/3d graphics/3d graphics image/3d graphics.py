
# DATE 4 NOVEMBER 2023 
#  I made a 3d box and a flatformar game


# from ursina import *

# Cube Quad Sphere
# app = Ursina()
# player = Entity(model = "cube", color = color.green , scale_y = 2)

# def update():
#     player.x += held_keys["right arrow"] * 0.1
#     player.x -= held_keys["left arrow"] * 0.1
#     player.y += held_keys["up arrow"] * 0.1
#     player.y -= held_keys["down arrow"] * 0.1
#     player.rotation_x += held_keys["space"] * 5
#     player.rotation_y += held_keys["r"] * 5
    
# app.run()

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

for i in range (10):
    for j in range(10):
        Entity(
            model = "cube", color = color.dark_gray, collider = "box", ignore= True,
            position = (j, 0, i),
            parent = scene,
            origin_y = 0.5,
            texture = "white_cube"
        )
        
class TextureBox(Button):
    def __init__(self, position = (5,2,5)):
        super().__init__(
            parent = scene,
            position = position,
            model = "cube",
            origin_y = 0.5,
            texture = "grass texture copy.jpg",
            color = color.color(0,0,1)
        )
        
        self.texture_choice = 0
        self.textures = ["grass texture copy.jpg", 
                         "paper texture.jpg",
                         "Python texture.png",
                         "IMG_7994.JPG"
                         ]
        
    def input(self, key):
        if self.hovered :
            if key == 'left mouse down':
                self.texture_choice += 1
                self.texture_choice %= len (self.textures)
                self.texture = self.textures[self.texture_choice]
        
                
                

                
                
                
TextureBox()

player = FirstPersonController()
app.run()