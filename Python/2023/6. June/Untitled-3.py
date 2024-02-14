import pygame
pygame.init()

slow = pygame.time. Clock()
white = (255,255,255)
blue=(0,0,255)
black= (0,0,0)

x = 350
y = 450
width = 50
height = 50

# Jump program
isjump = False
jump_height = 10

#for movement
x_change = 0
y_change = 0

# Display making program
screen = pygame.display.set_mode((700,700))
pygame.display.update()

# While loop useing program
run = False
while run == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True
       
    # Drawing Program        
    pygame.draw.rect(screen, white,[x,y,width,height,],  )
    
    # Movement program
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT :
                x -= 5
        elif event.key == pygame.K_RIGHT:
                x += 5
    if event.type == pygame.KEYUP:
        if event.key == pygame. K_LEFT or  event.key == pygame. K_RIGHT:
           x_change =0
           
    # jump program    
    userInput = pygame.key.get_pressed()
    if isjump is False and userInput [ pygame.K_UP]:
        isjump = True
    if isjump is True:
        y -= jump_height
        # jumps speed
        jump_height -= 1
        
        if jump_height < -10:
            isjump = False
            jump_height = 10
        # Finish jump program
             
    # Boundary makeing program 
    if x<= 0: 
        x=0
    elif x >= 650:
        x=650
        
    # speed control program
    slow.tick(80)  
      
    pygame.display.update()
    
    # Backgrund program
    screen.fill (black)
pygame.QUIT()
QUIT()