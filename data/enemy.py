import pygame
import random

sprites = [
    "assets/enemy-4-0.png",
    "assets/enemy-3-0.png",
    "assets/enemy-2-0.png",
    "assets/enemy-1-0.png",
    "assets/enemy-0-0.png",
]

sprites2 = [
    "assets/enemy-4-1.png",
    "assets/enemy-3-1.png",
    "assets/enemy-2-1.png",
    "assets/enemy-1-1.png",
    "assets/enemy-0-1.png",
]

score = [30,20,20,10,10]


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, row):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = pygame.image.load(sprites[row])
        self.sprite = pygame.transform.scale(self.sprite, (width, height))
        self.sprite2 = pygame.image.load(sprites2[row])
        self.sprite2 = pygame.transform.scale(self.sprite2, (width, height))
        self.image = self.sprite
        self.rect = self.image.get_rect(topleft = (x, y))
        self.x = x
        self.y = y
        self.speed = pygame.math.Vector2(0.50, 0)
        self.position = pygame.math.Vector2(x, y)
        self.health = 1
        self.shootChance = 0.00010
        self.score = score[row]
        self.animation_timer = random.randint(0, 60)
    def move(self):
        self.position += self.speed
        self.x = self.position.x
        self.y = self.position.y
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
    
    def draw(self, screen):
        self.animation_timer += 1

        if self.animation_timer > 60:
            self.animation_timer = 0
            if self.image == self.sprite:
                self.image = self.sprite2
            else:
                self.image = self.sprite

        screen.blit(self.image, (self.x, self.y))