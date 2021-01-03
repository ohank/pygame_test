import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('./Space-Invaders-Pygame-master/ufo.png')
pygame.display.set_icon(icon)
run = True

player_image = pygame.image.load('./assert/ship.png')
player_pos = {"x": 370, "y": 480}
player_move_x = 0


def draw_player(x, y):
    screen.blit(player_image, (x, y))


while run:
    screen.fill((50, 50, 150))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player_move_x = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_move_x = -1
            if event.key == pygame.K_RIGHT:
                player_move_x = 1


    player_pos['x'] += player_move_x
    draw_player(player_pos['x'], player_pos['y'])
    pygame.display.update()
