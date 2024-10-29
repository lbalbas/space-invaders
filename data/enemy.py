import pygame
import random

class Enemy(pygame.Rect):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.speed = pygame.math.Vector2(0.50, 0.06)
        self.position = pygame.math.Vector2(x, y)
        self.health = 1

    def move(self):
        self.position += self.speed
        self.x = self.position.x
        self.y = self.position.y