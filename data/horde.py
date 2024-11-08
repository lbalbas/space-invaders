import pygame
from data.enemy import Enemy
import random
from data.bullet import Bullet

class Horde(pygame.Rect):
    def __init__(self):
        self.x = 2
        self.y = 2
        self.width = 520
        self.height = 220
        self.enemies = []
        self.direction = "right"
        self.pos = pygame.math.Vector2(self.x, self.y)
        self.velocity = pygame.math.Vector2(0.40, 0.05)
        self.bullets = []

    def spawn(self):
        for i in range(5):
            for j in range(11):
                self.enemies.append(Enemy(j * 50, i * 50, 20, 20, i))
    
    def move(self, screen):
        for enemy in self.enemies:
            screen.blit(enemy.image, (enemy.x, enemy.y))
            enemy.move()

        self.pos += self.velocity
        self.x = self.pos.x
        self.y = self.pos.y
        for bullet in self.bullets:
            bullet.move(screen)

    def shoot(self):
        for enemy in self.enemies:
            if random.random() < enemy.shootChance:
                self.bullets.append(Bullet(enemy.x, enemy.y, 5, 5, 1))
    def change_direction(self):
        if self.direction == "right":
            self.direction = "left"
        else:
            self.direction = "right"
        
        self.velocity.x *= -1
        for enemy in self.enemies:
            enemy.speed.x *= -1
    
    def check_collisions(self, left_wall, right_wall, bottom_wall, game_over):
        if self.colliderect(right_wall) or self.colliderect(left_wall):
            self.change_direction()
        if self.colliderect(bottom_wall):
            game_over()
