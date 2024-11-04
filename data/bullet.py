import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/bullet.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft = (x, y))
        self.x = x
        self.y = y
        self.pos = pygame.math.Vector2(self.x, self.y)
        self.velocity = pygame.math.Vector2(0, direction)

    def move(self):
        self.pos += self.velocity
        self.y = self.pos.y
        self.rect = self.image.get_rect(topleft = (self.x, self.y))