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

    def spawn(self):
        for i in range(5):
            for j in range(11):
                self.enemies.append(Enemy(j * 50, i * 50, 20, 20))
    
    def move(self):
        for enemy in self.enemies:
            enemy.move(self.direction)
        if self.direction == "right":
            self.x += 1
        else:
            self.x -= 1

        self.y += 1