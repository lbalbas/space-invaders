import random
import pygame
from data.enemy import Enemy
class Horde(pygame.Rect):
    def __init__(self):
        self.x = 1
        self.y = 1
        self.width = 520
        self.height = 220
        self.enemies = []
        self.direction = "right"
        self.pos = pygame.math.Vector2(self.x, self.y)
        self.velocity = pygame.math.Vector2(0.50, 0.06)
        self.bullets = []

    def spawn(self):
        for i in range(5):
            for j in range(11):
                self.enemies.append(Enemy(j * 50, i * 50, 20, 20))
    
    def move(self):
        for enemy in self.enemies:
            enemy.move()
        self.pos += self.velocity
        self.x = self.pos.x
        self.y = self.pos.y

    def change_direction(self):
        if self.direction == "right":
            self.direction = "left"
        else:
            self.direction = "right"
        
        self.velocity.x *= -1
        for enemy in self.enemies:
            enemy.speed.x *= -1