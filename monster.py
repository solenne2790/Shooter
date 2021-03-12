import pygame
import random


class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1, 4)

    def damage(self, amount):
        # on definit le nombre de domages causes par le projectile#
        self.health -= amount

        # check if life is lower or equals to 0#
        if self.health <= 0:
            # on peux supprimer l'entite #
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health
            self.velocity = random.randint(1, 3)

    def update_health_bar(self, surface):
    # dessiner la barre de vie#
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])


    def forward(self):
        # le déplacement ne sera possible qu'en l'absence de collisions avec un groupe de joueurs#
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        #Si le monstre est en collision avec le joueur
        else:
            #Infliger des degats a notre joueur
            self.game.player.damage(self.attack)


