import pygame
import random
from data.player import Player
from data.horde import Horde
from data.bullet import Bullet
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

player = Player(300, 300, 15, 15)
horde = Horde()
score = 0


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    screen.fill("black")

    keys = pygame.key.get_pressed()
    player.move(keys, top_wall, bottom_wall, left_wall, right_wall)

    if keys[pygame.K_SPACE] and len(player.bullets) == 0:
        player.bullets.append(Bullet(player.x, player.y, 5, 5, -1))

    if len(horde.enemies) == 0:
        horde.spawn()

    for bullet in player.bullets:
        bullet.move()
        pygame.draw.rect(screen, (255, 0, 0), bullet, 0)
    
    for bullet in horde.bullets:
        bullet.move()
        pygame.draw.rect(screen, (0, 255, 0), bullet, 0)    

    for enemy in horde.enemies:
        if random.random() < 0.00010:
            horde.bullets.append(Bullet(enemy.x, enemy.y, 5, 5, 1))
        pygame.draw.rect(screen, (0, 255, 0), enemy, 0)
        for bullet in player.bullets:
            if bullet.colliderect(enemy):
                player.bullets.remove(bullet)
                enemy.health -= 1
                if enemy.health == 0:
                    horde.enemies.remove(enemy)
                    score += 1
            if bullet.y < 0:
                player.bullets.remove(bullet)
        if player.colliderect(enemy):
            running = False
        if enemy.y > 570:
            horde.enemies.remove(enemy)

    horde.move()
    if horde.colliderect(right_wall) or horde.colliderect(left_wall):
        horde.change_direction()
    
    if horde.colliderect(bottom_wall):
        running = False
    
    for bullet in horde.bullets:
        if bullet.colliderect(player):
            horde.bullets.remove(bullet)
            running = False

    pygame.draw.rect(screen, (255, 255, 255), player, 0)
    pygame.draw.rect(screen, (0, 0, 0), left_wall, 0)
    pygame.draw.rect(screen, (0, 0, 0), right_wall, 0)

    pygame.display.set_caption(f"Score: {score}")
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()