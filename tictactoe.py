import pygame

# Initialize pygame
pygame.init()

# Define constants
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300
GRID_SIZE = 100
LINE_WIDTH = 5
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Set up the font
font = pygame.font.SysFont('Arial', 24)

# Set up the game board
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
player = 1
winner = None

# Define a function to draw the game board
def draw_board():
    for i in range(1, 3):
        # Draw horizontal lines
        pygame.draw.line(window, BLACK, (0, i*GRID_SIZE), (WINDOW_WIDTH, i*GRID_SIZE), LINE_WIDTH)
        # Draw vertical lines
        pygame.draw.line(window, BLACK, (i*GRID_SIZE, 0), (i*GRID_SIZE, WINDOW_HEIGHT), LINE_WIDTH)

    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                # Draw an X
                pygame.draw.line(window, RED, (col*GRID_SIZE+20, row*GRID_SIZE+20), ((col+1)*GRID_SIZE-20, (row+1)*GRID_SIZE-20), LINE_WIDTH)
                pygame.draw.line(window, RED, ((col+1)*GRID_SIZE-20, row*GRID_SIZE+20), (col*GRID_SIZE+20, (row+1)*GRID_SIZE-20), LINE_WIDTH)
            elif board[row][col] == 2:
                # Draw an O
                pygame.draw.circle(window, BLUE, (col*GRID_SIZE+GRID_SIZE//2, row*GRID_SIZE+GRID_SIZE//2), GRID_SIZE//2-20, LINE_WIDTH)

# Define a function to check for a winner
def check_winner():
    global winner
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != 0:
            winner = board[row][0]
            return
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
            winner = board[0][col]
            return
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        winner = board[0][0]
        return
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        winner = board[0][2]
        return

# Define a function to handle events
# Define a function to handle events
def handle_events():
    global player, winner
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if winner is not None:
                return
            # Get the position of the mouse click
            x, y = pygame.mouse.get_pos()
            # Convert the position to board coordinates
            row = y // GRID_SIZE
            col = x // GRID_SIZE
            # If the cell is already occupied, do nothing
            if board[row][col] != 0:
                return
            # Update the board and the player
            board[row][col] = player
            player = 2 if player == 1 else 1
            # Check for a winner
            check_winner()


while True:
    # Handle events
    handle_events()
    # Draw the game board
    window.fill(WHITE)
    draw_board()
    # Check if there is a winner
    if winner is not None:
    # Display the winner
        text = font.render("Player {} wins!".format(winner), True, BLACK)
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        window.blit(text, text_rect)
    # Update the display
    pygame.display.update()


