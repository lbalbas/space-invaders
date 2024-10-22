# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 570))
clock = pygame.time.Clock()
running = True
dt = 0

left_wall = pygame.Rect(0,0,2,570)
right_wall = pygame.Rect(720,0,2,570)
top_wall = pygame.Rect(0,0,720,2)
bottom_wall = pygame.Rect(0,570,720,2)


player_x = 300
player_y = 300
speed = 2
width = 15
height = 15

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")


    player = pygame.Rect(player_x, player_y, width, height)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and not player.colliderect(top_wall):
        player_y -= 300 * dt
    if keys[pygame.K_s] and not player.colliderect(bottom_wall):
        player_y += 300 * dt
    if keys[pygame.K_a] and not player.colliderect(left_wall):
        player_x -= 300 * dt
    if keys[pygame.K_d] and not player.colliderect(right_wall):
        player_x += 300 * dt


    pygame.draw.rect(screen, (255,255,255), player, 0)
    pygame.draw.rect(screen, (0,0,0), left_wall, 0)
    pygame.draw.rect(screen, (0,0,0), right_wall, 0)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()