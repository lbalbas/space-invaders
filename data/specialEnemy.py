import pygame
from data.enemy import Enemy
from data.bullet import Bullet

import random
class SpecialEnemy(Enemy):
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/specialEnemy.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.x = 15 if random.randint(1, 2) % 2 == 0 else 705
        self.y = 30
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.speed = pygame.math.Vector2(0.75, 0)
        self.health = 1
        self.score = 50
        self.shootChance = 0.01
        self.bullets = []
        self.hasSpawn = False
    
    def spawn(self):
        if not self.hasSpawn:
            self.position = pygame.math.Vector2(self.x, self.y)
            self.hasSpawn = True
    
    def update(self,screen):
        screen.blit(self.image, (self.x, self.y))
        self.move()
        for bullet in self.bullets:
            bullet.move(screen)
            if bullet.y < 0:
                self.bullets.remove(bullet)
    def check_collisions(self, left_wall, right_wall):
        if self.rect.colliderect(right_wall) or self.rect.colliderect(left_wall):
            self.speed.x *= -1
    
    def shoot(self):
        if random.random() < self.shootChance:
            self.bullets.append(Bullet(self.x, self.y, 5, 5, 2))