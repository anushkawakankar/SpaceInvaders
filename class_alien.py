import pygame, sys
from random import randint
from pygame.locals import *



class alien:
	def __init__(self,type):
		if type==1:
			self.img = pygame.image.load('alien1.png')
		if type==2:
			self.img = pygame.image.load('export.png')	
		self.img = pygame.transform.scale(self.img, (90,50))
		
	def makealien(self,screen,x,y):
		screen.blit(self.img, (x,y))