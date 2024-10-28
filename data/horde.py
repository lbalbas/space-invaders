import random
from data.enemy import Enemy
class Horde:
    def __init__(self):
        self.enemies = []

    def spawn(self):
        for i in range(5):
            for j in range(11):
                self.enemies.append(Enemy(j * 50, i * 50, 20, 20))