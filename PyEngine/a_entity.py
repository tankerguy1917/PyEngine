###### ENTITY FILE ######

#### Imports ####
import pygame, sys
from pygame.locals import *

#### Entity Class ####
class Entity:
	def __init__(self, x, y, w, h, speed):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.speed = speed
		self.move = [0, 0]
		self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

	def show_entity(self, surf, color):
		pygame.draw.rect(surf, (color), self.rect)

	def set_pos(self):
		self.rect[0] += self.move[0]
		self.rect[1] += self.move[1]

	def set_dim(self, x, y, w, h):
		self.rect[0] = x
		self.rect[1] = y
		self.rect[2] = w
		self.rect[3] = h

	def collide1(self, rect_list):
		for rect in rect_list:
			if self.rect.colliderect(rect):
				if self.move[0] > 0:
					self.move[0] = 0
					self.rect.right = rect.left
				if self.move[0] < 0:
					self.move[0] = 0
					self.rect.left = rect.right
				if self.move[1] > 0:
					self.move[1] = 0
					self.rect.bottom = rect.top
				if self.move[1] < 0:
					self.move[1] = 0
					self.rect.top = rect.bottom

#### Platform Class ####
class Wall(Entity):
	def __init__(self, x, y, w, h, speed):
		super().__init__(x, y, w, h, speed)
		self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
