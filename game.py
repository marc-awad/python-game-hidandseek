import pygame
from player import Player
from enemy import Enemy
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_IMAGE, SKY_IMAGE, SKY_SCALE_HEIGHT_RATIO, GAME_TITLE, PLAYER_SIZE, WHITE, VICTORY_SCREEN, WINNING_CONDITION, PLAYER_START_X, PLAYER_START_Y


class Game:
    def __init__(self):
        pygame.init()
        self.score = 0
        self.font = pygame.font.Font(None, 50)

        self.player = Player()
        self.enemy = Enemy()
        # Fenetre du jeu
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # Changer le titre
        pygame.display.set_caption(GAME_TITLE)

        # Charger l'image de fond (décor)
        self.background = pygame.image.load(BACKGROUND_IMAGE)
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Chargement et redimensionnement du ciel par rapport au background
        self.sky = pygame.image.load(SKY_IMAGE)
        self.sky = pygame.transform.scale(self.sky, (SCREEN_WIDTH, int(SCREEN_HEIGHT/SKY_SCALE_HEIGHT_RATIO)))

        self.started = True
        self.running = True

    def movements(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.player.move_up()
        if keys[pygame.K_DOWN]:
            self.player.move_down()
        if keys[pygame.K_LEFT]:
            self.player.move_left()
        if keys[pygame.K_RIGHT]:
            self.player.move_right()

    def show_victory_screen(self):
        self.victory_screen = pygame.image.load(VICTORY_SCREEN)
        self.victory_screen = pygame.transform.scale(
            self.victory_screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.blit(self.victory_screen, (0, 0))
        pygame.display.flip()
        
        # Réinitialiser le jeu si l'utilisateur appuie sur ESPACE
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.score = 0
            self.player.rect.x, self.player.rect.y = PLAYER_START_X, PLAYER_START_Y
            self.enemy.random_position()
            self.started = True

    def gravite(self):
        if self.player.rect.y < SCREEN_HEIGHT - PLAYER_SIZE:
            self.player.rect.y += 20

    def check_collision(self):
        if self.player.rect.colliderect(self.enemy.rect):
            self.enemy.random_position()
            self.score += 1
            # Vérifie la condition de victoire
            if self.score == WINNING_CONDITION:
                self.started = False
        # Met à jour le texte du score
        self.score_text = self.font.render(f"Score : {self.score}", True, WHITE)

    def run(self):
        # Garder la fenêtre allumée tant que le jeu est lancé
        while self.running:
            if self.started:
                self.check_collision()
                self.gravite()
                self.movements()

                # Injecter l'image dans l'écran à un certain endroit
                self.screen.blit(self.sky, (0, 0))
                self.screen.blit(self.background, (0, 0))
                self.screen.blit(self.player.image, self.player.rect)
                self.screen.blit(self.enemy.image, self.enemy.rect)
                # Position en haut à gauche
                self.screen.blit(self.score_text, (SCREEN_WIDTH/2, 5))
            else:
                self.show_victory_screen()

            # Mettre à jour l'écran (chaque frame du jeu)
            pygame.display.flip()

            # Parcourir la liste des evenements haut, bas, gauche, droite
            for event in pygame.event.get():
                # Si on appuie sur quqitter, la page se ferme --> started = false
                if event.type == pygame.QUIT:
                    self.running = False

        pygame.quit()