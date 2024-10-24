import pygame
import random
from data.player import Player
from data.enemy import Enemy
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
enemies = []
bullets = []
score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    screen.fill("black")

    keys = pygame.key.get_pressed()
    player.move(keys, top_wall, bottom_wall, left_wall, right_wall)

    if keys[pygame.K_SPACE] and len(bullets) == 0:
        bullets.append(Bullet(player.x, player.y, 5, 5))

    if len(enemies) < 5:
        enemies.append(Enemy(random.randint(0, 720), 0, 20, 15))

    for bullet in bullets:
        bullet.move()
        pygame.draw.rect(screen, (255, 0, 0), bullet, 0)

    for enemy in enemies:
        enemy.move()
        pygame.draw.rect(screen, (0, 255, 0), enemy, 0)
        for bullet in bullets:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemy.health -= 1
                if enemy.health == 0:
                    enemies.remove(enemy)
                    score += 1
        if player.colliderect(enemy):
            running = False
        if enemy.y > 570:
            enemies.remove(enemy)

    pygame.draw.rect(screen, (255, 255, 255), player, 0)
    pygame.draw.rect(screen, (0, 0, 0), left_wall, 0)
    pygame.draw.rect(screen, (0, 0, 0), right_wall, 0)

    pygame.display.set_caption(f"Score: {score}")
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()