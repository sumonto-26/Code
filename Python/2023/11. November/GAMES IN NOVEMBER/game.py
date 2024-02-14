import pygame
import random

pygame.init()

# Colors
Black = (0, 0, 30)
red = (255, 100, 20)
White = (195, 255, 255)
snake_color = (20, 200, 255)

# Creating window
screen_width = 900
screen_height = 700
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Snake Game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont("Comic Sans MS", 25)
font1 = pygame.font.SysFont("Comic Sans MS", 100)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def text_screen2(text, color, x, y):
    screen_text = font1.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def plot_snake(gameWindow, color, snk_list, snake_size, food_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def homepage():
    gameWindow.fill(Black)
    text_screen2("Snake Game", White, 200, 100)
    text_screen("Press Space to Play", White, 350, 250)
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                gameloop()

def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 500
    snake_y = 250
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 4
    snake_size = screen_height // 20
    food_size = screen_height // 30
    fps = 60

    while not exit_game:
        if game_over:
            gameWindow.fill(Black)
            text_screen2("Game Over! ", White, 200, 100)
            text_screen("Press Space To Start", White, 350, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameloop()



        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    elif event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    elif event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    elif event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < food_size and abs(snake_y - food_y) < food_size:
                score += 1
                food_x = random.randint(0, screen_width / 1)
                food_y = random.randint(0, screen_height / 1)
                snk_length += 5

            gameWindow.fill(Black)

            head = [snake_x, snake_y]
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if (
                snake_x <= 0
                or snake_x > screen_width
                or snake_y <= 0
                or snake_y > screen_height
            ):
                game_over = True

            plot_snake(gameWindow, snake_color, snk_list, snake_size, food_size)

            text_screen("Score: " + str(score * 1), White, 5, 5)
            pygame.draw.rect(gameWindow, (red), [food_x, food_y, food_size, food_size])

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

homepage()
