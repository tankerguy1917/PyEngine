###### MAIN GAME FILE ######

#### Imports/Init ####
import pygame, sys, a_screen, time
from pygame.locals import *
from a_screen import Screen
from a_mouse import Mouse
pygame.init()

test_img = pygame.image.load("img_test.png")

test_rect = pygame.Rect(25, 10, 10, 10)

WIN = (500, 300)
screen = pygame.display.set_mode(WIN, 0, 32)

s = Screen(pygame.Surface((250, 150)), (0, 0), (0, 0, 255))

while True:
	mx, my = pygame.mouse.get_pos()
	m = Mouse(mx, my, test_img, True, True)

	s.set_bg(None, None, (255, 255, 255))

	s.draw_rect(test_rect, (255, 0, 0))

	m.show_cursor(s.surf, (2, 2))

	for e in pygame.event.get():
		if e.type == QUIT:
			pygame.quit()
			sys.exit()

	screen.blit(s.set_res(s.surf, (WIN[0], WIN[1])), s.loc)
	pygame.display.update()
