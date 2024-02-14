import pygame
from pygame.locals import*

pygame.init()

screen_width = 900
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Breakout game")

# define font
# font = pygame.font.SysFont('calibri', 50)
# font = pygame.font.SysFont('bitstreamverasans', 50)
# font = pygame.font.SysFont('calibri', 50)
font = pygame.font.SysFont('Constantia', 50)


background_color = pygame.Color('grey12')
# Block_color's
block_red = [255, 50, 50]
block_green = [50, 255, 50] 
block_blue = [0, 100, 255]
# anything colors
anything_color = pygame.Color ('lightcyan')
anything_outline = pygame.Color ('cyan')

# text color
text_col = [78, 81, 139]



# Define game variable
cols = 12
rows = 6
clock = pygame.time.Clock() 
live_ball = False
game_over = 0

# function for outputing text only screen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# Brick wall class
class wall():
    def __init__(self):
        self.width = screen_width // cols
        self.height = 50
        
    def create_wall(self):
        self.block = []
        # Define an empty list for an individual block
        block_individual = []
        for row in range(rows):
            # reset the block row list
            block_row = []
            
            #iterate through each coloum in that row
            for col in range(cols):
                # generate x and y positions for each block and creat a rectangle from that
                block_x = col * self.width
                block_y = row * self.height
                rect = pygame.Rect(block_x, block_y, self.width, self.height)
                
                # assign block strength strength based on row 
                if row < 2 :
                    strength = 3
                elif row < 4 :
                    strength = 2
                elif row < 6 :
                    strength = 1

                # create a list at this point to store the rect and colour data
                block_individual = [rect, strength]
                
                block_row.append(block_individual)
                self.block.append (block_row) 
                                     
    def draw_walls(self):
        for row in self.block:
            for block in row:
                # assign a colour based on block strength
                if block[1] == 3:
                     Block_color = block_red
                elif block[1] == 2:
                    Block_color = block_blue
                elif block[1] == 1:
                    Block_color = block_green


                pygame.draw.rect(screen, Block_color, block[0])
                pygame.draw.rect(screen, background_color,( block[0]), 3 )
                
  
class anything():
    def __init__(self):
        self.reset()

        
        
    def moveing(self):
        
        # reset movement direction
        self.direction = 0
        key = pygame.key. get_pressed()
        if key [pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
            self.direction = 1
            
        if key [pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed
            self.direction = 1
        
        
    def draw (self):
        pygame.draw.rect( screen, anything_color, self.rect)
        pygame.draw.rect( screen, anything_outline, self.rect, 3)
        
    def reset(self):
        
        # define anything variables
        self.height = 20 
        self.width = int(screen_width / 6) 
        self.x = int((screen_width /2 ) - (self.width / 2))
        self.y = screen_height - (self.height / 2 + 40)
        self. speed = 10
        self.rect = Rect(self.x , self.y, self.width, self. height)
        self.direction = 0
        
# Make the ball for this game
class ball_make():
    def __init__(self, x, y):
        self.reset(x, y)

        
    def moveing(self):
        
        colliding_thresh = 5
        
        # Start of with the assumption that the wall has been destoryed completely
        wall_destroyed = 1
        row_counter = 0
        
        
        for row in wall.block:
            item_counter = 0
            for item in row:
                if self.rect.colliderect(item[0]):
                    
                    # check if collision was from above
                    if abs (self.rect.bottom - item [0].top) < colliding_thresh and self.speed_y > 0:
                        self.speed_y *= -1
                        
                    # check if collision was from below  
                    if abs (self.rect.top - item [0].bottom) < colliding_thresh and self.speed_y > 0:
                        self.speed_y *= -1
        
                    # check if collision was from left
                    if abs (self.rect.right - item [0].left) < colliding_thresh and self.speed_x > 0:
                        self.speed_x *= -1
                        
                    # check if collision was from right 
                    if abs (self.rect.left - item [0].right) < colliding_thresh and self.speed_x > 0:
                        self.speed_x *= -1
                        
                    # reduce the block's strength by doing damage to it
                    if wall.block[row_counter][item_counter][1] > 1:
                        wall.block[row_counter][item_counter][1] -= 1
                        
                    else:
                        wall.block[row_counter][item_counter][0] = (0, 0, 0, 0)
                        
                # Check if block still exists , in which case the wall is not destroyed
                if wall.block[row_counter][item_counter][0] != (0, 0, 0, 0) :
                    wall_destroyed = 0
                    
                # increase item_counter
                item_counter += 1
                
            # increase row_counter
            row_counter += 1
            
        # after iterating through all the  blocks, check if the wall is destroyed
        if wall_destroyed == 1 :
            self.game_over = 1
            
                        
        # Check for collsion with walls
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed_x *= -1
            
        if self.rect.top < 0 :
            self.speed_y *= -1
            
        if self.rect.bottom > screen_height:
            self.game_over = -1
            
        # look for collission with anything named box
        if self.rect.colliderect(player_anything):
            # check if colliding from the top
            if abs (self .rect.bottom - player_anything.rect.top)  < colliding_thresh and self.speed_y > 0:
                
                self.speed_y *= -1
                self.speed_x +=  player_anything.direction
                
                if self.speed_x > self.speed_max:
                    self.speed_x = self.speed_max
                    
                elif self.speed_x < 0 and self.speed_x < -self.speed_max:
                    self.speed_x = self.speed_max
                    
                else:
                    self.speed_x *= -1
                    
            
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        return self.game_over
        
    def draw(self):
        
        pygame.draw.circle( screen,anything_outline , (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad + 3)
        pygame.draw.circle( screen, anything_color, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad)
    
    def reset(self, x, y):
        self.ball_rad = 10
        self.x = x - self.ball_rad
        self.y = y
        self. rect = Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
        self . speed_x = 4
        self . speed_y = -4
        self . speed_max = 5
        self. game_over = 0
    
    
    
wall = wall()
wall.create_wall()

player_anything = anything()

# to make ball
ball = ball_make(player_anything.x + (player_anything.width // 2) , player_anything.y - player_anything.height)


run = True
while run == True:
    
    clock.tick(60)
    screen.fill(background_color)
    
    wall.draw_walls()
    player_anything.draw()
    ball.draw()
    
    if live_ball:
        
        player_anything.moveing()
        game_over = ball.moveing()
        
        if game_over !=  0:
            live_ball = False
    
    
    # print player instructions
    if not live_ball:
        if game_over == 0:
            draw_text('CLICK LEFT CLICK TO START', font, text_col, 150, screen_height // 2 + 100)
    
        elif game_over == 1 :
            draw_text('YOU WIN !', font, text_col, 350, screen_height // 2 + 50)
            draw_text('CLICK LEFT CLICK TO START', font, text_col, 150, screen_height // 2 + 100)

        elif game_over == -1 :
            draw_text('YOU LOSE', font, text_col, 350, screen_height // 2 + 50)
            draw_text('CLICK LEFT CLICK TO START', font, text_col, 150, screen_height // 2 + 100)
            
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.MOUSEBUTTONDOWN and live_ball == False:
            live_ball = True
            ball.reset (player_anything.x + (player_anything.width // 2) , player_anything.y - player_anything.height)
            player_anything.reset()
            wall.create_wall()




    pygame.display.update()
            
pygame.quit()
quit()