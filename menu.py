import pygame
# import tictactoe
# import snake
# import mines2

# Initialize Pygame
pygame.init()

# Define constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
BUTTON_SPACING = 20
BUTTON_FONT_SIZE = 24
BUTTON_TEXT_COLOR = (255, 255, 255)
BUTTON_COLOR = (0, 0, 255)
BUTTON_HIGHLIGHT_COLOR = (0, 100, 255)

# Set up the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pygame Game Selector")

# Set up the font
font = pygame.font.SysFont('Arial', BUTTON_FONT_SIZE)

# Define a function to draw the buttons
def draw_button(text, x, y, width, height, highlight=False):
    button_color = BUTTON_HIGHLIGHT_COLOR if highlight else BUTTON_COLOR
    pygame.draw.rect(window, button_color, (x, y, width, height))
    button_text = font.render(text, True, BUTTON_TEXT_COLOR)
    text_rect = button_text.get_rect()
    text_rect.center = (x + width / 2, y + height / 2)
    window.blit(button_text, text_rect)

# Define a function to handle events
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if tic_tac_toe_button_rect.collidepoint(x, y):
                # Launch Tic Tac Toe game
                import tictactoe
            elif snake_button_rect.collidepoint(x, y):
                # Launch Snake game
                import snake
            elif mines2_button_rect.collidepoint(x, y):
                # Launch mines2 game
                import mines2

# Main game loop
while True:


    # Draw the buttons
    tic_tac_toe_button_rect = pygame.draw.rect(window, BUTTON_COLOR, (WINDOW_WIDTH / 2 - BUTTON_WIDTH / 2, 100, BUTTON_WIDTH, BUTTON_HEIGHT))
    draw_button("Tic Tac Toe", WINDOW_WIDTH / 2 - BUTTON_WIDTH / 2, 100, BUTTON_WIDTH, BUTTON_HEIGHT, tic_tac_toe_button_rect.collidepoint(pygame.mouse.get_pos()))

    snake_button_rect = pygame.draw.rect(window, BUTTON_COLOR, (WINDOW_WIDTH / 2 - BUTTON_WIDTH / 2, 170, BUTTON_WIDTH, BUTTON_HEIGHT))
    draw_button("Snake", WINDOW_WIDTH / 2 - BUTTON_WIDTH / 2, 170, BUTTON_WIDTH, BUTTON_HEIGHT, snake_button_rect.collidepoint(pygame.mouse.get_pos()))

    mines2_button_rect = pygame.draw.rect(window, BUTTON_COLOR, (WINDOW_WIDTH / 2 - BUTTON_WIDTH / 2, 240, BUTTON_WIDTH, BUTTON_HEIGHT))
    draw_button("Minesweeper", WINDOW_WIDTH / 2 - BUTTON_WIDTH / 2, 240, BUTTON_WIDTH, BUTTON_HEIGHT, mines2_button_rect.collidepoint(pygame.mouse.get_pos()))

    # Handle events
    handle_events()

    # Update the display
    pygame.display.update()


