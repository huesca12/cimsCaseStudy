import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple 2D Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player settings
player_size = 50
player_pos = [WIDTH // 2, HEIGHT // 2]
player_speed = 5

# Item settings
item_size = 30
item_pos = [random.randint(0, WIDTH - item_size), random.randint(0, HEIGHT - item_size)]

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - player_size:
        player_pos[1] += player_speed

    # Check for collision with item
    if (player_pos[0] < item_pos[0] < player_pos[0] + player_size or player_pos[0] < item_pos[0] + item_size < player_pos[0] + player_size) and \
       (player_pos[1] < item_pos[1] < player_pos[1] + player_size or player_pos[1] < item_pos[1] + item_size < player_pos[1] + player_size):
        item_pos = [random.randint(0, WIDTH - item_size), random.randint(0, HEIGHT - item_size)]

    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.rect(screen, RED, (item_pos[0], item_pos[1], item_size, item_size))
    pygame.display.flip()

    clock.tick(30)

pygame.quit()