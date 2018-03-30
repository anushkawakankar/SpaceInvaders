import pygame, sys
from random import randint
from pygame.locals import *

#main class bullet

class bullet:
	def __init__(self,x,y):			
		self.bulimg = pygame.transform.scale(self.bulimg, (x,y))
		

	def makebullet(self,screen,x):
		screen.blit(self.bulimg, (x,520))

#subclasses of bullet that inherit from main_bullet

class bullet1(bullet):
	def __init__(self):
		self.bulimg = pygame.image.load('bull.png')
		super(bullet1, self).__init__(50,30)
		

class bullet2(bullet):
	def __init__(self):
		self.bulimg = pygame.image.load('bull2.png')
		super(bullet2, self).__init__(30,40)
		

