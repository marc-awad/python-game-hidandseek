from game import Game
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_HOME_PAGE, STARTING_BUTTON

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Page d'accueil")
    

    # Mettre à jour l'affichage
    pygame.display.update()
    home_page_button = pygame.image.load(STARTING_BUTTON)
    home_page_button = pygame.transform.scale(home_page_button,(SCREEN_WIDTH/10, SCREEN_HEIGHT/10))
    home_page_button_rect = home_page_button.get_rect()

    center_position_x = (SCREEN_WIDTH-home_page_button.get_width())/2
    center_position_y = (SCREEN_HEIGHT-home_page_button.get_height())/2

    home_page_button_rect.x = center_position_x
    home_page_button_rect.y = center_position_y

    background_home_page = pygame.image.load(BACKGROUND_HOME_PAGE)
    background_home_page = pygame.transform.scale(background_home_page, (SCREEN_WIDTH, SCREEN_HEIGHT))

    opened_page = True
    while opened_page:
        screen.blit(background_home_page, (0, 0))
        screen.blit(home_page_button,home_page_button_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                opened_page = False
        mouse_pos = pygame.mouse.get_pos()
        if home_page_button_rect.collidepoint(mouse_pos):
            home_page_button = pygame.transform.scale(home_page_button,(SCREEN_WIDTH/9, SCREEN_HEIGHT/9))
            if event.type == pygame.MOUSEBUTTONDOWN:
                game = Game()
                game.run()

        else: 
            home_page_button = pygame.transform.scale(home_page_button,(SCREEN_WIDTH/10, SCREEN_HEIGHT/10))

        pygame.display.flip()

    # Quitter Pygame
    pygame.quit()


if __name__ == "__main__":
    main()