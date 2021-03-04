###### MAIN GAME FILE ######

#### Imports/Init ####
import pygame, sys
from pygame.locals import *
from a_screen import s
pygame.init()

test_rect = pygame.Rect(25, 10, 10, 10)

WIN = (500, 300)
screen = pygame.display.set_mode(WIN, 0, 32)

#Use this loop to test new features
while True:
	s.set_bg(None, None, (255, 255, 255))

	for e in pygame.event.get():
		if e.type == QUIT:
			pygame.quit()
			sys.exit()

	screen.blit(pygame.transform.scale(s.surf, WIN), s.loc)
	pygame