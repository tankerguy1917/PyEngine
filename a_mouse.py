###### MOUSE FILE ######

#### Imports ####
import pygame, sys
from pygame.locals import *

#### Mouse Class ####
class Mouse:
	def __init__(self, x, y, img, in_middle, mouse_vis):
		"""
		x: int, mouse x position. See docs.txt for more info
		y: int, mouse y position. See docs.txt for more info
		img: pygame.image.load("image_name") image to be displayed as the mouse. See docs.txt for more info
		in_middle: bool. See docs.txt for more info
		mouse_vis: bool. See docs.txt for more info
		"""
		self.x = x
		self.y = y
		self.img = img
		self.in_middle = in_middle
		self.mouse_vis = mouse_vis
		self.mouse_rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())
		pygame.mouse.set_visible(mouse_vis)

	def show_cursor(self, surf, res):
		"""
		surf: pygame.Surface or Screen.surf. See docs.txt for more info
		res: (int, int). See docs.txt for more info
		"""
		if self.in_middle:
			self.mouse_rect.center = (self.x - self.img.get_width() / res[0], self.y - self.img.get_height() / res[1])
			surf.blit(self.img, (self.mouse_rect[0] / res[0], self.mouse_rect[1] / res[1]))
