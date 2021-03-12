import pygame
import projectile
pygame.init()
from game import Game
from comet_event import CometFallEvent





background = pygame.image.load('assets/bg.jpg')
pygame.display.set_caption("comet fall game")
screen = pygame.display.set_mode((1080, 720))

#import and load game banner
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = screen.get_width() / 4

play_button = pygame.image.load('assets/button.png')
play_button =pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()



# on charge notre jeu
game = Game()

running = True

# boucle tant que notre condition est vraie
while running:

    # appliquer la fenetre du jeu
    screen.blit(background, (0, -200))

    #check if the game is start or not
    if game.is_playing:
        #start party instructions#
        game.update(screen)
		#if our game is not started
    else:
        screen.blit(banner, (300, 20))
        screen.blit(play_button, (350, 400))

    # on raffraichit l'ecran
    pygame.display.flip()

    for event in pygame.event.get():


        keys = pygame.key.get_pressed()

        if event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()


        if event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verification pour savoir si la souris est en collision avec le bouton joue
             if pygame.mouse.get_pressed()[0]:
                #voir si le jeux est en mode "lance"
                game.start()

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()












