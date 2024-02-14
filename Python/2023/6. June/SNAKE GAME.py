import pygame , sys , random
from pygame.math import Vector2

# Creating a snake
class SNAKE:
    def __init__(self):
        self.body = [Vector2 ( 5,10), Vector2 (4,10), Vector2 (3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False
        
        
        # snake head
        
        self.head_up = pygame.image.load('2023/6. June/Snake game icon/head up.png').convert_alpha()
        self.head_down = pygame.image.load('2023/6. June/Snake game icon/head down.png').convert_alpha()
        self.head_left = pygame.image.load('2023/6. June/Snake game icon/head left.png').convert_alpha()
        self.head_right = pygame.image.load('2023/6. June/Snake game icon/head right.png').convert_alpha()
        
        # snake tall
        
        self.tail_up = pygame.image.load('2023/6. June/Snake game icon/last 3.png').convert_alpha()
        self.tail_down = pygame.image.load('2023/6. June/Snake game icon/last 1.png').convert_alpha()
        self.tail_left = pygame.image.load('2023/6. June/Snake game icon/last 2.png').convert_alpha()
        self.tail_right = pygame.image.load('2023/6. June/Snake game icon/last 4.png').convert_alpha()
        
        # for body body
        
        self.body_vertical = pygame.image.load ('2023/6. June/Snake game icon/body 1.png').convert_alpha()
        self.body_horizontal = pygame.image.load('2023/6. June/Snake game icon/body 2.png').convert_alpha()
        
        #for curve body parts
        
        self.body_tr = pygame.image.load('2023/6. June/Snake game icon/bodymove 1.png').convert_alpha()
        self.body_tl = pygame.image.load('2023/6. June/Snake game icon/bodymove 2.png').convert_alpha()
        self.body_br = pygame.image.load('2023/6. June/Snake game icon/bodymove 4.png').convert_alpha()
        self.body_bl = pygame.image.load('2023/6. June/Snake game icon/bodymove 3.png').convert_alpha()
        
        
    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        
        for index, block in enumerate(self.body) :
            # 1. We still need a rect for the positioning
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            
            # 2. What direction is the face heading  
            if index == 0:
                screen.blit(self.head, block_rect)
                # 3.snake head direction is not updateing 
            elif index == len(self.body) -1:
                screen.blit(self.tail,block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                    
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl,block_rect)
                        
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl,block_rect)
                        
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr,block_rect)
                        
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br,block_rect)
            #else:
             #   pygame.draw.rect(screen,(150, 100, 100), block_rect)
        
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0): self.head = self.head_left
        elif head_relation == Vector2(-1, 0): self.head = self.head_right
        elif head_relation == Vector2(0, 1): self.head = self.head_up
        elif head_relation == Vector2(0, -1): self.head = self.head_down
        
        
        
        
        
        
        
        
        # for block in self.body :
        #     # Create a rect 
        #     x_pos = int(block.x * cell_size)
        #     y_pos = int(block.y * cell_size)
            
        #     block_rect = pygame.Rect( x_pos , y_pos , cell_size , cell_size)
            
        #     # Draw the rectangle
        #     pygame.draw.rect (screen,(183, 111, 122) , block_rect)
            
    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0): self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1): self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1): self.tail = self.tail_down
        
    
    # make movement_snake function
    def movement_snake(self):
        if self.new_block == True:
                body_copy = self.body[ : ]
                body_copy.insert(0, body_copy[0] + self.direction)
                self.body = body_copy [ : ]
                self.new_block = False
        
        else:
            body_copy = self.body[ : -1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy [ : ]
           
           
    # make add_block function
    def add_block(self):
        self.new_block = True
                
class FRUIT:
    def __init__(self):
        self.randomize()

        
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size) ,int(self.pos.y * cell_size), cell_size , cell_size )
        screen.blit(apple,fruit_rect)
        # pygame.draw.rect ( screen , (126, 166, 114) , fruit_rect)
        # draw the rect.
    
    def randomize(self):
        self.x = random.randint (0 , cell_number - 1)
        self.y = random.randint(0 , cell_number - 1)
        self.pos = Vector2(self.x , self.y)
        # create an x & y position
        # draw a square
   
class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        
    def update(self):
        self.snake.movement_snake()
        self.check_collision()
        self.check_fail()
        
    def draw_elements(self):
        # call 2 function
        self.fruit.draw_fruit()
        self.snake.draw_snake ()
        
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            # reposition the fruit
            self.fruit.randomize()
            
            # add another block to the snake
            self.snake.add_block()

    def check_fail(self):
        #check if  snake is outside of the screen 
        if not 0 <= self.snake.body[0].x < cell_number:
            self.game_over()
        if not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        
        
        for block in self.snake.body[1 : ]:
            if block == self.snake.body[0]:
                self.game_over()
                
        # check if snake hits it self
    
    def game_over (self):
        pygame.quit()
        sys.exit()
        # for if gameover it remove this display
            
pygame.init()

# Make 2 variables
cell_size = 40
cell_number = 19

# Make display
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))

# To control speed
clock = pygame.time.Clock()

# To import apple image
apple = pygame.image.load('2023/6. June/Snake game icon/apple.png').convert_alpha() #for image load better

# green = [175, 215, 70]

# Make x and y axies
# x_position = 200
# y_position = 250
# test_surface = pygame.Surface((100, 200))

# For box color 
# test_surface.fill(pygame.Color('blue'))

# # To draw Rectangle 
# test_rect = test_surface.get_rect(topright = (x_position, y_position))

# To draw Rectangle
# test_rect = pygame.Rect(100, 200, 100, 100)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE , 150)

main_game = MAIN()

# Make game loop
while True:
    # Draw all our elements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        def draw_grass(self):
            grass_color = pygame.Color(green)
            for row in range(cell_number):
                if row % 2 == 0:
                    for col in range(cell_number):
                        if col % 2 == 0 :
                            grass_rect = pygame.Rect(col * cell_size ,row * cell_size ,cell_size,cell_size)
                            pygame.draw.rect (screen , grass_color, grass_rect )
                
                    
                            
            self.draw_grass()
        #For movement
        if event.type == SCREEN_UPDATE:
            main_game.update()
            
        # if key prese
        if event.type == pygame.KEYDOWN:
            # for up movement
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1 :  # to type this line the snake can't move the opposite side
                    main_game.snake.direction = Vector2 ( 0 , -1)
                
            # for down movement
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1 :  # to type this line the snake can't move the opposite side
                    main_game.snake.direction = Vector2 ( 0 , 1)
                
            # for right movement
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1 :  # to type this line the snake can't move the opposite side
                    main_game.snake.direction = Vector2 ( 1 , 0)
                
            # for left movement
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1 :  # to type this line the snake can't move the opposite side
                    main_game.snake.direction = Vector2 ( -1 , 0)
            
            
    # screen.fill(pygame.Color ('light blue')) For making build-in color 
    # screen.fill(green)
    screen.fill ((175, 255, 70))

    # call draw_elements function
    main_game.draw_elements()
    
    # Update this program
    pygame.display.update()
    
    # To control speed
    clock.tick(60)
    
pygame.QUIT()
quit()