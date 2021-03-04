###### SCREEN FILE ######

#### Imports ####
import pygame, sys
from pygame.locals import *

#### Screen class ####
class Screen:
	def __init__(self, surf, loc, color):
		"""
		surf: pygame.Surface((int, int)) thats just how it is
		loc: (int, int) location to blit surface
		color: (int, int, int) color to fill background with
		"""
		self.surf = surf
		self.loc = loc
		self.color = color

	def show_img(self, img, loc):
		"""
		img: pygame.image.load("image_name")
		loc: (int, int) location to blit img
		"""
		self.surf.blit(img, (loc))

	def draw_rect(self, rect, color):
		"""
		rect: pygame.Rect(int, int, int, int)
		color: (int, int, int) color to fill the rect with
		"""
		pygame.draw.rect(self.surf, (color), rect)

	def set_bg(self, img, loc, color):
		"""
		img: pygame.image.load("image_name")
		loc: (int, int) location to blit img
		color: (int, int, int) color to fill backround
		"""
		if color != None:
			self.surf.fill((color))
		if img != None:
			self.surf.blit(img, (loc))

s = Screen(pygame.Surface((250, 150)), (0, 0), (0, 0, 255))