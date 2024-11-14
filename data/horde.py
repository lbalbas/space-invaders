import pygame
from data.enemy import Enemy
import random
from data.bullet import Bullet

class Horde():
    def __init__(self):
        self.enemies = []
        self.bullets = []

    def spawn(self):
        for i in range(5):
            for j in range(11):
                self.enemies.append(Enemy(j * 45 + 5, i * 50, 32, 32, i))
    
    def move(self, screen):
        for enemy in self.enemies:
            enemy.move()
            enemy.draw(screen)
        for bullet in self.bullets:
            bullet.move(screen)

    def shoot(self):
        for enemy in self.enemies:
            if random.random() < enemy.shootChance:
                self.bullets.append(Bullet(enemy.x, enemy.y, 10, 10, 2))
    def change_direction(self):       
        for enemy in self.enemies:
            enemy.speed.x *= -1
            enemy.rect.y += 20
            enemy.position.y += 20

    
    def check_collisions(self, left_wall, right_wall, bottom_wall, game_over):
        for enemy in self.enemies:
            if enemy.rect.colliderect(bottom_wall):
                game_over()
                break
            if enemy.rect.colliderect(left_wall) or enemy.rect.colliderect(right_wall):
                self.change_direction()
                break
