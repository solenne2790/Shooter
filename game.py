from player import Player
from monster import Monster
from comet_event import CometFallEvent


import pygame
import random
import player
import monster


#on crée une seconde classe qui va representer notre jeux
class Game:

	def __init__(self):
		#check if the game is started or not
		self.is_playing = False
		#generer notre joueur
		self.player = Player(self)
		self.all_players = pygame.sprite.Group()

		self.comet_event = CometFallEvent()
		# on gere notre groupe de monstres
		self.all_players.add(self.player)
		  #groupe de monstre
		self.all_monsters = pygame.sprite.Group
		self.all_monsters = pygame.sprite.Group()
		self.pressed = {}

		#2 pour que 2 monstres poppent au lieu d'un #

	def start(self):
		self.is_playing = True
		self.spawn_monster()
		self.spawn_monster()




	def game_over(self):
		#remettre a neuf le jeux ect
		self.all_monsters = pygame.sprite.Group()
		self.player.health = self.player.max_health
		self.is_playing = False

	def update(self, screen):
		# appliquer l'image du personnage
		screen.blit(self.player.image, self.player.rect)

		#actualiser la barre du jeux
		self.comet_event.update_bar(screen)
		# Actualiser la barre du joueur
		self.player.update_health_bar(screen)

		#actualiser la barre d'evenement du jeu
		self.comet_event.update_bar(screen)

		# recupere les projectiles du joueur
		for projectile in self.player.all_projectiles:
			projectile.move()

		# recuperer les monstres de notre jeux
		for monster in self.all_monsters:
			monster.forward()
			monster.update_health_bar(screen)

		# appliquer l'ensemble des images de projectile
		self.player.all_projectiles.draw(screen)

		# appliquer l'ensemble des images du groupe de monstres
		self.all_monsters.draw(screen)

		# detecter les touches en temps reel
		if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 920:
			self.player.move_right()
		if self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
			self.player.move_left()

	def check_collision(self,sprite,group):
		return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)

	def update_health_bar(self, surface):
		# dessiner la barre de vie#
		pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
		pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 7])

	def spawn_monster(self):
		monster = Monster(self)
		self.all_monsters.add(monster)
