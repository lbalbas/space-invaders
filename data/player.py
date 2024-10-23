import pygame

class Player(pygame.Rect):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.speed = 2

    def move(self, keys, top_wall, bottom_wall, left_wall, right_wall):
        if keys[pygame.K_w] and not self.colliderect(top_wall):
            self.y -= 5
        if keys[pygame.K_s] and not self.colliderect(bottom_wall):
            self.y += 5
        if keys[pygame.K_a] and not self.colliderect(left_wall):
            self.x -= 5
        if keys[pygame.K_d] and not self.colliderect(right_wall):
            self.x += 5