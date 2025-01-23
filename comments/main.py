import pygame
import random

# Initialize Pygame∏
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player settings
player_size = 50
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - 2 * player_size]

# Enemy settings
enemy_size = 50
enemy_pos = [random.randint(0, SCREEN_WIDTH - enemy_size), 0]
enemy_list = [enemy_pos]

# Speed settings
SPEED = 10

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple 2D Game")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Function to drop enemies
def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, SCREEN_WIDTH - enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])

# Function to draw enemies
def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

# Function to update enemy positions
def update_enemy_positions(enemy_list, score):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < SCREEN_HEIGHT:
            enemy_pos[1] += SPEED
        else:
            enemy_list.pop(idx)
            score += 1
    return score

# Function to detect collisions
def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos, player_pos):
            return True
    return False

# Function to detect collision between player and enemy
def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
    return False

# Main game loop
game_over = False
score = 0

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= SPEED
    if keys[pygame.K_RIGHT] and player_pos[0] < SCREEN_WIDTH - player_size:
        player_pos[0] += SPEED

    screen.fill(BLACK)

    drop_enemies(enemy_list)
    score = update_enemy_positions(enemy_list, score)

    if collision_check(enemy_list, player_pos):
        game_over = True

    draw_enemies(enemy_list)

    pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], player_size, player_size))

    pygame.display.update()

    clock.tick(30)

print("Game Over! Your score was:", score)
pygame.quit()