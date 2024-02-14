import pygame

# To initialize or (to start pygame)
pygame.init()

# It is so fast to make it slow (we make a clock) 
clock = pygame.time.Clock()

# Colour making
black =  (0, 0, 0)
blue =   (0, 0, 255)
violet = (255, 0, 255)
green = (0,255,0)
light_green =  (0, 255, 150)
red =    (255,0,0)
white =  (255,255,255)

# x and y axies
x = 300
y = 200

# To update x and y and ("make smooth movement")
x_change = 0
y_change = 0

# Display or window making
gd = pygame.display.set_mode((700,700))
pygame.display.set_caption("My first program with pygame.")
# pygame.display.update() na dilao choley

# While loop use
game_over = False
while game_over == False:
    for event in pygame.event.get():
        
        # Cut botton make to Close this gameing window  
        if event.type == pygame.QUIT:
            game_over = True
            
        # Condition makeing for left right up down move
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT :
                x_change += 10
            elif event.key == pygame.K_RIGHT:
                x_change -= 10
            elif event.key == pygame.K_UP:
                y_change += 10
            elif event.key == pygame.K_DOWN:
                y_change -= 10
                
        # For stop this rect or box        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                y_change = 0
            pygame.display.update()
            
    # Background colour        
    gd.fill(light_green)
    
    # To make this movement smooth
    x = x - x_change
    y = y - y_change
    
    # To make boundary
    if  x <= 0:
        x = 0
    elif x >= 650: # To make boundary we make it >= 650 [if we type 700 it can't see cleanly.]
        x = 650
        
    # For y axies we type this 4 line code :    
    if  y <= 0:
        y = 0
    elif y >= 650:
        y = 650    
        
    # To countrol speed
    clock.tick(40)
    
    # DON'T REMOVE THIS LINES!!!
    #SOME SHAPES
    # Draw rect or a box
    # pygame.draw.rect(gd,blue,[x,y,50,50])
    
    # Draw circle 
    # pygame.draw.circle(gd,black,(x,y),35,50)
    
    # To make our circle cool we type this line 
    # pygame.draw.circle(gd, green, (x,y),30, 100, draw_top_left = True, draw_bottom_right = True)
    
    # Draw oval shape
    # pygame.draw.ellipse(gd, (blue), (x, y, 150, 75))
    
    # Draw line
    pos = pygame.mouse.get_pos()
    pygame.draw.line(gd, (black), (300,200), pos)
    
    # Draw polygon or nike logo
    # pygame.draw.polygon(gd, white ,((100,200),(200,300),(500,100), (200,250)) ) 
    
    # [Rule of draw Circle] pygame.draw.circle (display making ar variable , (colur),(position) size , center)
    
    # To update our display with shapes 
    pygame.display.update()

    # DON'T REMOVE THIS LINES !!!        
            
# To finish in program and make it cleanly work    
pygame.QUIT()            
QUIT()
