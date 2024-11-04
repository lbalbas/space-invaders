import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/enemy.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft = (x, y))
        self.x = x
        self.y = y
        self.speed = pygame.math.Vector2(0.50, 0.06)
        self.position = pygame.math.Vector2(x, y)
        self.health = 1

    def colliderect(self, rect):
        return self.rect.colliderect(rect)
    def move(self):
        self.position += self.speed
        self.x = self.position.x
        self.y = self.position.y
        self.rect = self.image.get_rect(topleft = (self.x, self.y))