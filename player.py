# C'est un sprite du jeu (tout ce qui n'est pas statique)
import pygame
from constants import PLAYER_SPEED, PLAYER_SIZE, PLAYER_IMAGE, PLAYER_START_X, PLAYER_START_Y


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(PLAYER_IMAGE)
        self.image = pygame.transform.scale(
            self.image, (PLAYER_SIZE, PLAYER_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = PLAYER_START_X
        self.rect.y = PLAYER_START_Y

    # Jumping
    def move_up(self):
        if self.rect.y > 0:
            self.rect.y -= PLAYER_SPEED*2

    def move_down(self):
        if self.rect.y < 700 - (PLAYER_SIZE+5):
            self.rect.y += PLAYER_SPEED

    def move_right(self):
        if self.rect.x < 1500 - (PLAYER_SIZE+5):
            self.rect.x += PLAYER_SPEED

    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= PLAYER_SPEED