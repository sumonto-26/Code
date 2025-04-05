import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
CAPTION = "Pygame Basics"
FPS = 60  # Frame rate

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize screen and clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()

# Font for displaying text
font = pygame.font.Font(None, 36)  # Default font, size 36

def handle_events():
    """Handle all events, including quitting the game."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        # Handle keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Quit on ESC key
                return False
            print(f"Key pressed: {pygame.key.name(event.key)}")  # Print key name
        # Handle mouse input
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(f"Mouse clicked at: {event.pos}")  # Print mouse position
    return True

def draw_shapes():
    """Draw basic shapes on the screen."""
    # Draw a rectangle
    pygame.draw.rect(screen, RED, (50, 50, 100, 100))  # (x, y, width, height)
    # Draw a circle
    pygame.draw.circle(screen, GREEN, (200, 150), 50)  # (center_x, center_y, radius)
    # Draw a line
    pygame.draw.line(screen, BLUE, (300, 50), (400, 150), 5)  # (start, end, thickness)

def display_text(text):
    """Display text on the screen."""
    text = font.render(text, True, WHITE)  # (text, antialias, color)
    screen.blit(text, (250, 400))  # (text_surface, (x, y))

def main():
    """Main game loop."""
    running = True
    while running:
        # Handle events
        running = handle_events()

        # Clear the screen
        screen.fill(BLACK)

        # Draw shapes
        draw_shapes()

        # Display text
        display_text("hello world")

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(FPS)

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()