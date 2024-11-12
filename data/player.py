import pygame
from data.bullet import Bullet

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
        self.lives = 2

    def move(self, keys, left_wall, right_wall, screen):
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and not self.rect.colliderect(left_wall):
            self.x -= 5
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and not self.rect.colliderect(right_wall):
            self.x += 5

        self.rect = self.image.get_rect(topleft = (self.x, self.y))
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullets:
            bullet.move(screen)
            if bullet.y < 0:
                self.bullets.remove(bullet)

    def shoot(self, keys):
        if keys[pygame.K_SPACE] and len(self.bullets) < 1:
            self.bullets.append(Bullet(self.x, self.y, 5, 5, -2))

    def check_collisions(self, horde, special_enemy, game_over, add_score): 
            
        if special_enemy.hasSpawn:
            for bullet in self.bullets:
                if bullet.rect.colliderect(special_enemy.rect):
                    special_enemy.health -= 1
                    if special_enemy.health == 0:
                        add_score(special_enemy.score)
                        special_enemy.hasSpawn = False
                        self.bullets.remove(bullet)
            for bullet in special_enemy.bullets:
                if bullet.rect.colliderect(self.rect):
                    special_enemy.bullets.remove(bullet)
                    self.lives -= 1
                    if self.lives < 0:
                        game_over()
        
        for enemy in horde.enemies:
            if self.rect.colliderect(enemy.rect):
                self.lives -= 1
                if self.lives < 0:
                    game_over()
            for bullet in self.bullets:
                if bullet.rect.colliderect(enemy.rect):
                    add_score(enemy.score)
                    horde.enemies.remove(enemy)
                    self.bullets.remove(bullet)
        
        for bullet in horde.bullets:
            if bullet.rect.colliderect(self.rect):
                horde.bullets.remove(bullet)
                self.lives -= 1
                if self.lives < 0:
                    game_over()
