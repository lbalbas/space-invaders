import pygame
import random
from data.player import Player
from data.horde import Horde
from data.bullet import Bullet
from data.specialEnemy import SpecialEnemy
# pygame setup
pygame.init()

screen = pygame.display.set_mode((720, 570))
clock = pygame.time.Clock()

START = 0
RUNNING = 1
GAME_OVER = 2

running = True
game_state = START

dt = 0

left_wall = pygame.Rect(0,0,2,570)
right_wall = pygame.Rect(720,0,2,570)
bottom_wall = pygame.Rect(0,570,720,2)

font = pygame.font.Font('freesansbold.ttf', 32)

pygame.display.set_caption("Space Invaders")

score = 0

def game_over():
    global game_state
    game_state = GAME_OVER

def add_score(int):
    global score
    score += int

while running:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not game_state == RUNNING:
            game_state = RUNNING
            player = Player(360, 520, 15, 15)
            horde = Horde()
            specialEnemy = SpecialEnemy(15, 15)
            score = 0

    if game_state == RUNNING:
        text = font.render("Score: " + str(score), True, (255,255,255), (0,0,0))
        textRect = text.get_rect()
        screen.blit(text, (10, 10))
        keys = pygame.key.get_pressed()

        if horde.enemies == []:
            player.lives = 2
            horde.spawn()

        horde.move(screen)
        horde.shoot()
        horde.check_collisions(left_wall, right_wall, bottom_wall, game_over)
        
        if not specialEnemy.hasSpawn and random.random() < 1 / 1500:
            specialEnemy.spawn()
        elif specialEnemy.hasSpawn:
            specialEnemy.update(screen)
            specialEnemy.check_collisions(left_wall, right_wall)
            specialEnemy.shoot()

        player.draw(screen)
        player.move(keys, left_wall, right_wall, screen)
        player.shoot(keys)
        player.check_collisions(horde, specialEnemy, game_over, add_score)
        
        pygame.draw.rect(screen, (0, 0, 0), left_wall, 0)
        pygame.draw.rect(screen, (0, 0, 0), right_wall, 0)
    elif game_state == GAME_OVER:
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over! Press space bar to restart", True, (255, 255, 255))
        screen.blit(text, (175, 200))
    elif game_state == START:
        text = font.render("PRESS SPACE TO START", True, (255,255,255), (0,0,0))
        textRect = text.get_rect()
        screen.blit(text, (175, 250))
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()