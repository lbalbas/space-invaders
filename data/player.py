import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/player.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft = (x, y))
        self.x = x
        self.y = y
        self.speed = 1
        self.bullets = []

    def move(self, keys, top_wall, bottom_wall, left_wall, right_wall):
        if keys[pygame.K_w] and not self.rect.colliderect(top_wall):
            self.y -= 5
        if keys[pygame.K_s] and not self.rect.colliderect(bottom_wall):
            self.y += 5
        if keys[pygame.K_a] and not self.rect.colliderect(left_wall):
            self.x -= 5
        if keys[pygame.K_d] and not self.rect.colliderect(right_wall):
            self.x += 5

        self.rect = self.image.get_rect(topleft = (self.x, self.y))