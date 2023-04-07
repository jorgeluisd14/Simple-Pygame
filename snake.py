import pygame
import random

# Define constants for the game window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
CELL_SIZE = 20

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize pygame
pygame.init()

# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Define the Snake class
class Snake:
    def __init__(self):
        self.body = [(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)]
        self.direction = 'right'

    def move(self):
        x, y = self.body[0]
        if self.direction == 'up':
            y -= CELL_SIZE
        elif self.direction == 'down':
            y += CELL_SIZE
        elif self.direction == 'left':
            x -= CELL_SIZE
        elif self.direction == 'right':
            x += CELL_SIZE
        self.body.insert(0, (x, y))
        self.body.pop()

    def grow(self):
        x, y = self.body[0]
        if self.direction == 'up':
            y -= CELL_SIZE
        elif self.direction == 'down':
            y += CELL_SIZE
        elif self.direction == 'left':
            x -= CELL_SIZE
        elif self.direction == 'right':
            x += CELL_SIZE
        self.body.insert(0, (x, y))

    def change_direction(self, direction):
        if direction == 'up' and self.direction != 'down':
            self.direction = 'up'
        elif direction == 'down' and self.direction != 'up':
            self.direction = 'down'
        elif direction == 'left' and self.direction != 'right':
            self.direction = 'left'
        elif direction == 'right' and self.direction != 'left':
            self.direction = 'right'

    def draw(self):
        for x, y in self.body:
            pygame.draw.rect(window, GREEN, (x, y, CELL_SIZE, CELL_SIZE))

# Define the Food class
class Food:
    def __init__(self):
        self.x = random.randint(0, WINDOW_WIDTH // CELL_SIZE - 1) * CELL_SIZE
        self.y = random.randint(0, WINDOW_HEIGHT // CELL_SIZE - 1) * CELL_SIZE

    def draw(self):
        pygame.draw.rect(window, RED, (self.x, self.y, CELL_SIZE, CELL_SIZE))

# Create the Snake and Food objects
snake = Snake()
food = Food()

# Run the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction('up')
            elif event.key == pygame.K_DOWN:
                snake.change_direction('down')
            elif event.key == pygame.K_LEFT:
                snake.change_direction('left')
            elif event.key == pygame.K_RIGHT:
                snake.change_direction('right')

    # Move the snake
    snake.move()

    # Check if the snake ate the food
    if snake.body[0] == (food.x, food.y):
        snake.grow()
        food = Food()

    # Check if the snake hit a wall or its own body
            # Check if the snake hit a wall or its own body

    if snake.body[0][0] < 0 or snake.body[0][0] >= WINDOW_WIDTH or \
        snake.body[0][1] < 0 or snake.body[0][1] >= WINDOW_HEIGHT:
        pygame.quit()
        exit()

    for i in range(1, len(snake.body)):
        if snake.body[0] == snake.body[i]:
            pygame.quit()
            exit()

    # Draw the game objects
    window.fill(WHITE)
    snake.draw()
    food.draw()
    pygame.display.update()

    # Set the frame rate
    clock.tick(10)  # 10 frames per second
