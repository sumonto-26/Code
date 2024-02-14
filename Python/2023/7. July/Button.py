import pygame

# using oop
class Button:
    def __init__(self,text,width,height,pos, elevation):
        
        # Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]
       
        # top rectangle
        self.top_rect = pygame.Rect(pos,(width, height))
        self.top_color = [30, 80, 155]
        
        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos,(width,elevation))
        self.bottom_color = [50, 50, 50]
        
        # Text
        self.text_surface = button_font.render(text , True , [255,255,255])
        self.text_rect = self.text_surface.get_rect(center = self.top_rect.center)
        
    def draw(self): # for draw button
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center
        
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation
        
        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius = 10)
        pygame.draw.rect(screen , self.top_color , self.top_rect, border_radius = 10 ) 
        screen.blit(self.text_surface, self.text_rect)
        # border_radius for how round our button it need integer
        self.click()

    def click(self): # for is user click or not
        # get mouse position 
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            
            # hexa decimal color
            self.top_color = [235, 0, 0] # [# D74B4B, ] hexe color
            # if player pressed the button 
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed == True :
                    print('THANK YOU')
                    self.pressed = False
                    
        else :
            self.dynamic_elevation = self.elevation
            self.top_color = [30, 80, 155]
                                   
pygame.init()

clock = pygame.time.Clock()
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode ((screen_width, screen_height))
pygame.display.set_caption ('Button making')
button_font = pygame.font.SysFont('PYTHON', 45 ) #

button_1 = Button('CLICK ME', 200, 40, (200,250) , 10) #

run = False
while run == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True
            
    screen.fill([225, 225, 225])
    button_1.draw() #
    pygame.display.update()
    clock.tick(60)

