import pygame

#créer une classe pour gérer cet evenement
class CometFallEvent:

	#lors de notre chargement -> on va créer un event
	def __init__(self):	
		self.percent = 0
		self.percent_speed = 5

	def add_percent(self):
		self.percent += self.percent_speed / 100

	def update_bar(self, surface):
		
		#ajouter un pourcentage a la barre
		self.add_percent()		

		#barre noire en background
		pygame.draw.rect(surface,(0,0,0),[     
		0, #l'axe des x
		surface.get_height() - 20, #l'axe des ordonnees
		surface.get_width(), #longueur de la fenetre
		10 #epaisseur de la barre
		])
		#barre rouge d'event
		pygame.draw.rect(surface, (187 , 11, 11),[     
		0, #l'axe des x
		surface.get_height() - 20, #l'axe des ordonnees
		(1080 / 100) * 10 , #longueur de la fenetre
		10 #epaisseur de la barre
		])


