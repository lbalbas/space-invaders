import pygame

class Bullet(pygame.Rect):
    def __init__(self, x, y, width, height, direction):
        super().__init__(x, y, width, height)
        self.pos = pygame.math.Vector2(self.x, self.y)
        self.velocity = pygame.math.Vector2(0, direction)

    def move(self):
        self.pos += self.velocity
        self.y = self.pos.y