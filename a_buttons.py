###### BUTTONS FILE ######

#### Imports ####
import pygame, sys
from pygame.locals import *

#### Button Class ####
class Button:
	def __init__(self, surf, img, x, y):
		"""
		surf: pygame.Surface(). See docs.txt for more details
		img: pygame.image.load(). See docs.txt for more details
		x: int. See docs.txt for more details
		y: int. See docs.txt for more details
		w: int. See docs.txt for more details
		h: int. See docs.txt for more details
		color: (int, int, int). See docs.txt for more details
		"""
		self.surf = surf
		self.img = img
		self.x = x
		self.y = y
		self.w = self.img.get_width()
		self.h = self.img.get_height()
		self.button_rect = pygame.Rect(self.x, self.y, self.w, self.h)

	def show_button(self, surf):
		surf.blit(self.img, (self.x, self.y))

	def set_img(self, img):
		self.img = img
