import pygame

#on crée une nouvelle classe qui va gerer le projectile de notre joueur
#projectile est une classe enfant de sprite
class Projectile(pygame.sprite.Sprite):
    #en dessous on cree notre constructeur

    def __init__(self, player):
        super().__init__()
        self.player = player
        self.velocity = 3
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image,(50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 125
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        #methode permettant de faire tourner notre projectile
        self.angle += 10
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        #on verifie si notre projectile entre en collision avec le monstre#
        for monster in  self.player.game.check_collision(self, self.player.game.all_monsters):
            #il faut supprimer le projectile#
            self.remove()
            #on inflige des degats aux monstres impactes#
            monster.damage(self.player.attack)


        self.rect.x += self.velocity
        self.rotate()
        #si notre projectile n'est plus a l'ecran
        if self.rect.x > 1080:
            self.remove()


