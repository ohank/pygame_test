import random
import pygame

pygame.init()
clock = pygame.time.Clock()
clock.tick(30)
screen = pygame.display.set_mode((800, 600))


background = pygame.image.load('assets/background.png')

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('assets/ship.png')
pygame.display.set_icon(icon)
run = True

player_image = pygame.image.load('assets/ship.png')
player_pos = {"x": 370, "y": 480}
player_move_x = 0

enemy_image = pygame.image.load('assets/enemy.png')
enemy_pos = {"x": random.randint(0, 800), "y": random.randint(50, 300)}
enemy_move_x = 0.1
enemy_move_y = 0


def draw_player(player_position: dict):
    screen.blit(player_image, (player_position['x'], player_position['y']))


def draw_enemy(enemy_position: dict):
    screen.blit(enemy_image, (enemy_position['x'], enemy_position['y']))


while run:
    screen.fill((50, 50, 150))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_move_x = -0.3
            if event.key == pygame.K_RIGHT:
                player_move_x = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player_move_x = 0

    player_pos['x'] += player_move_x
    player_pos['x'] = 0 if player_pos['x'] <= 0 else player_pos['x']
    player_pos['x'] = 736 if player_pos['x'] >= 736 else player_pos['x']

    enemy_pos['x'] += enemy_move_x
    if enemy_pos['x'] <= 0:
        enemy_move_x = 0.1
        enemy_pos['y'] += 5
    if enemy_pos['x'] >= 736:
        enemy_move_x = -0.1
        enemy_pos['y'] += 5

    draw_player(player_pos)
    draw_enemy(enemy_pos)
    pygame.display.update()
