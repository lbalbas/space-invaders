import pygame
import random

class Enemy(pygame.Rect):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.speed = 0
        self.health = 1

    def move(self):
        self.y += self.speed