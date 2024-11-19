import pygame
import random
from constants import SCREEN_HEIGHT, ENEMY_SIZE, ENEMY_IMAGE, SCREEN_WIDTH


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(ENEMY_IMAGE)
        self.image = pygame.transform.scale(
            self.image, (ENEMY_SIZE, ENEMY_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.random_position()

    def random_position(self):
        self.rect.x = random.randint(0, SCREEN_WIDTH-ENEMY_SIZE)
        self.rect.y = random.randint(0, SCREEN_HEIGHT-ENEMY_SIZE)