import pygame, sys
from random import randint
from pygame.locals import *



class shipp:

	def __init__(self):
		self.shipimg = pygame.image.load('space.png')
		self.shipimg = pygame.transform.scale(self.shipimg, (150,150))
		self.x=325
		self.y=600

	def makeship(self,screen):
		screen.blit(self.shipimg, (self.x,self.y))


