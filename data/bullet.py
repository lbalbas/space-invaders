import pygame

class Bullet(pygame.Rect):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.speed = 1.2

    def move(self):
        self.y -= self.speed