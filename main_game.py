import pygame, sys
from random import randint
from pygame.locals import *
from class_alien import alien
from class_shipp import shipp
from class_bullet import bullet1
from class_bullet import bullet2
from class_bullet import bullet


pygame.init()

pygame.font.init() 
myfont = pygame.font.SysFont('Comic Sans MS', 35)

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Space Invaders')
clock = pygame.time.Clock()
black = (0,0,0)
white=(255,255,255)


ship=shipp()
blist = []
alist = []
appearalien=pygame.USEREVENT+1
pygame.time.set_timer(appearalien, 10000)
x_cor=0
y_cor=0
dis=0
score=0


while True:

	if dis==0:
		x_cor=randint(100,700)
		y_cor=randint(0,200)
		a=alien(1)
		alist.append([a.img,x_cor,y_cor,0,1])
		dis=1


	clock.tick(50)
	
	
	screen.fill(black)
	ship.makeship(screen)
	pygame.display.update()

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		
		change=0

		if event.type == appearalien:
			x_cor=randint(100,700)
			y_cor=randint(0,200)
			a=alien(1)
			alist.append([a.img,x_cor,y_cor,0,1])

		if event.type == pygame.KEYDOWN :
			if event.key == pygame.K_a and ship.x>0:
				change=-5
			elif event.key == pygame.K_d and ship.x<650:
				change=5
			if event.key == pygame.K_SPACE:
				b=bullet1()
				blist.append([ship.x+50,580,1.25,b.bulimg])
			if event.key == pygame.K_s:
				c=bullet2()
				blist.append([ship.x+60,580,2.5,c.bulimg])
			if event.key == pygame.K_q:	
				pygame.quit()
				sys.exit()
	ship.x+=change

	#drawing on the screen

	for newb in blist:
		newb[1]-=newb[2]
		if newb[1]<0:
			blist.remove(newb)
		if newb[1]>0:
			screen.blit(newb[3],(newb[0],newb[1]))
	for newa in alist:
		newa[3]+=1
		
		if newa[3]<=400:
			for buls in blist:
				if buls[0]>=newa[1]-15 and buls[0]<=newa[1]+85 and buls[1]>=newa[2] and buls[1]<=newa[2]+50:
					
					if buls[2]==1.25 :
						score=score+1
						alist.remove(newa)
						blist.remove(buls)
					if buls[2]==2.5:
						newa[3]=100
						blist.remove(buls)
						e=alien(2)
						newa[0]=e.img		


			
			screen.blit(newa[0],(newa[1],newa[2]))
	string="SCORE:"+str(score)			

	textsurface = myfont.render(string, False, white)			
	screen.blit(textsurface,(2,2))

	pygame.display.flip()
