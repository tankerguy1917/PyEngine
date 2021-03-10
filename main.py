###### MAIN GAME FILE ######

#### Imports/Init ####
import pygame, sys, a_screen
from pygame.locals import *
from a_screen import Screen
from a_mouse import Mouse
from a_buttons import Button
from a_entity import Entity, Platform
pygame.init()

clock = pygame.time.Clock()

test_img = pygame.image.load("img_test.png")
c = pygame.image.load("cursor.png")

collide_list = []

p = Entity(100, 30, 10, 10, 1, 20, 3)
pl = Platform(90, 10, 100, 10, None, None, None)
collide_list.append(pl.rect)
pl2 = Platform(100, 55, 100, 10, None, None, None)
collide_list.append(pl2.rect)

WIN = (500, 300)
screen = pygame.display.set_mode(WIN, 0, 32)

s = Screen(pygame.Surface((250, 150)), (0, 0), (0, 0, 255))

b = Button(s, test_img, 30, 20)

while True:
	s.set_bg(None, None, (255, 255, 255))
	p.grav += 0.2
	if p.grav > 3:
		p.grav = 3

	p.collide1(collide_list)
	p.grav_effect()

	pl.set_dim(50, 90, 100, 10)
	s.draw_rect(pl.rect, (0, 255, 0))
	s.draw_rect(pl2.rect, (0, 255,0 ))

	mx, my = pygame.mouse.get_pos()
	m = Mouse(mx, my, c, True, False)

	p.show_entity(s.surf, (255, 0, 0))
	p.jump()
	p.set_pos()

	m.show_cursor(s.surf, (2, 2))

	for e in pygame.event.get():
		if e.type == QUIT:
			pygame.quit()
			sys.exit()
		if e.type == KEYDOWN:
			if e.key == K_RIGHT:
				p.move[0] = p.speed
			if e.key == K_LEFT:
				p.move[0] = -p.speed
			if e.key == K_UP:
				p.jumping = True
		if e.type == KEYUP:
			if e.key == K_RIGHT:
				p.move[0] = 0
			if e.key == K_LEFT:
				p.move[0] = 0

	screen.blit(s.set_res(s.surf, (WIN[0], WIN[1])), s.loc)
	pygame.display.update()
	clock.tick(60)
