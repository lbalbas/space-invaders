import pygame
import random

sprites = [
    "assets/enemy-4-0.png",
    "assets/enemy-3-0.png",
    "assets/enemy-2-0.png",
    "assets/enemy-1-0.png",
    "assets/enemy-0-0.png",
]

score = [30,20,20,10,10]

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, row):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprites[row])
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft = (x, y))
        self.x = x
        self.y = y
        self.speed = pygame.math.Vector2(0.40, 0.05)
        self.position = pygame.math.Vector2(x, y)
        self.health = 1
        self.shootChance = 0.00010
        self.score = score[row]
    def move(self):
        self.position += self.speed
        self.x = self.position.x
        self.y = self.position.y
        self.rect = self.image.get_rect(topleft = (self.x, self.y))