import pygame
import random

# Define constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 500
GRID_SIZE = 40
GRID_ROWS = 10
GRID_COLS = 10
NUM_MINES = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)

# Initialize pygame
pygame.init()

# Set up the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Minesweeper")

# Set up the font
font = pygame.font.SysFont('Arial', 24)

# Set up the game board
board = [[0 for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]
revealed = [[False for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]
mines = set()
while len(mines) < NUM_MINES:
    row = random.randint(0, GRID_ROWS-1)
    col = random.randint(0, GRID_COLS-1)
    if (row, col) not in mines:
        mines.add((row, col))
        board[row][col] = -1
for row in range(GRID_ROWS):
    for col in range(GRID_COLS):
        if board[row][col] != -1:
            count = 0
            for i in range(max(0, row-1), min(GRID_ROWS, row+2)):
                for j in range(max(0, col-1), min(GRID_COLS, col+2)):
                    if board[i][j] == -1:
                        count += 1
            board[row][col] = count

# Define a function to draw the game board
def draw_board():
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            rect = pygame.Rect(col*GRID_SIZE, row*GRID_SIZE+100, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(window, GRAY, rect, 1)
            if revealed[row][col]:
                if board[row][col] == -1:
                    pygame.draw.circle(window, RED, rect.center, GRID_SIZE//2)
                else:
                    text = font.render(str(board[row][col]), True, BLACK)
                    text_rect = text.get_rect(center=rect.center)
                    window.blit(text, text_rect)

# Define a function to reveal squares
def reveal_squares(row, col):
    if revealed[row][col]:
        return
    revealed[row][col] = True
    if board[row][col] == -1:
        game_over()
        return
    elif board[row][col] == 0:
        for i in range(max(0, row-1), min(GRID_ROWS, row+2)):
            for j in range(max(0, col-1), min(GRID_COLS, col+2)):
                reveal_squares(i, j)

    # Check for win condition
    win = True
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            if board[row][col] != -1 and not revealed[row][col]:
                win = False
                break
        if not win:
            break
    if win:
        font = pygame.font.SysFont('Arial', 36)
        text = font.render("Game Over, You Win!", True, (0, 255, 0))
        text_rect = text.get_rect(center=(WINDOW_WIDTH//2, 50))
        window.blit(text, text_rect)
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        exit()


# Define a function to handle game over
def game_over():
    font = pygame.font.SysFont('Arial', 36)
    text = font.render("Game Over", True, RED)
    text_rect = text.get_rect(center=(WINDOW_WIDTH//2, 50))
    window.blit(text, text_rect)
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    exit()

# Define a function to handle events
# Define a function to handle events
def handle_events():
    global revealed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # left-click
                col = event.pos[0] // GRID_SIZE
                row = (event.pos[1] - 100) // GRID_SIZE
                if not revealed[row][col]:
                    reveal_squares(row, col)
            elif event.button == 3: # right-click
                col = event.pos[0] // GRID_SIZE
                row = (event.pos[1] - 100) // GRID_SIZE
                if not revealed[row][col]:
                    revealed[row][col] = True



# Start the game loop
while True:
    # Handle events
    handle_events()

    # Clear the screen
    window.fill(WHITE)

    # Draw the game board
    draw_board()

    # Update the display
    pygame.display.update()
