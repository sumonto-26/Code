import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window dimensions
window_width = 800
window_height = 600

# Set the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Create the game window
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Set the game clock
clock = pygame.time.Clock()

# Set the font
font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
    """Display the message on the screen"""
    message_text = font_style.render(msg, True, color)
    game_window.blit(message_text, [window_width/6, window_height/3])


def game_loop():
    """The main game loop"""
    # Set the initial position of the snake
    x = window_width / 2
    y = window_height / 2
    x_change = 0
    y_change = 0

    # Set the size of the snake
    snake_size = 10

    # Set the initial score
    score = 0

    # Set the initial position of the food
    food_x = round(random.randrange(0, window_width - snake_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, window_height - snake_size) / 10.0) * 10.0

    # Set the game over flag
    game_over = False

    # Start the game loop
    while not game_over:
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_size
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_size

        # Move the snake
        x += x_change
        y += y_change

        # Draw the snake and the food
        game_window.fill(white)
        pygame.draw.rect(game_window, red, [food_x, food_y, snake_size, snake_size])
        pygame.draw.rect(game_window, black, [x, y, snake_size, snake_size])

        # Check if the snake has hit the walls or itself
        if x >= window_width or x < 0 or y >= window_height or y < 0:
            game_over = True
        if x == food_x and y == food_y:
            score += 1
            food_x = round(random.randrange(0, window_width - snake_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, window_height - snake_size) / 10.0) * 10.0

        # Update the score
        message("Score: " + str(score), black)

        # Update the display
        pygame.display.update()

        # Set the game clock
        clock.tick(15)

    # Quit Pygame
    pygame.quit()
    quit()

# Start the game loop
game_loop()
