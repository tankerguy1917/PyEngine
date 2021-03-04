###### SCREEN FILE ######

#### Imports ####
import pygame, sys
from pygame.locals import *

#### Screen class ####
class Screen:
	def __init__(self, surf, loc, color):
		""" 
		res: (int, int) See docs.txt for more info
		surf: pygame.Surface((int, int)) See docs.txt for more info
		loc: (int, int) location to blit surface. See docs.txt for more info
		color: (int, int, int) color to fill background with. See docs.txt for more info
		"""
		self.surf = surf
		self.loc = loc
		self.color = color

	def show_img(self, img, loc):
		"""
		img: pygame.image.load("image_name") See docs.txt for more info
		loc: (int, int) location to blit img. See docs.txt for more info
		"""
		self.surf.blit(img, (loc))

	def draw_rect(self, rect, color):
		"""
		rect: pygame.Rect(int, int, int, int) See docs.txt for more info
		color: (int, int, int) color to fill the rect with. See docs.txt for more info
		"""
		pygame.draw.rect(self.surf, (color), rect)

	def set_bg(self, img, loc, color):
		"""
		img: pygame.image.load("image_name") See docs.txt for more info
		loc: (int, int) location to blit img. See docs.txt for more info
		color: (int, int, int) color to fill backround. See docs.txt for more info
		"""
		if color != None:
			self.surf.fill((color))
		if img != None:
			self.surf.blit(img, (loc))

	def set_res(self, surf, res):
		surf = pygame.transform.scale(surf, (res))
		return surf
