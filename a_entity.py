###### ENTITY FILE ######

#### Imports ####
import pygame, sys
from pygame.locals import *

#### Entity Class ####
class Entity:
	def __init__(self, x, y, w, h, grav, air_time, speed):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.grav = grav
		self.air_time = air_time
		self.speed = speed
		self.falling = True
		self.jumping = False
		self.true_air_time = self.air_time
		self.true_grav = self.grav
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

	# Mainly for side scrollers
	def grav_effect(self):
		if self.falling:
			self.move[1] += self.grav

	# Mainly for side scrollers
	def jump(self):
		if self.jumping:
			self.move[1] = -self.grav
			self.air_time -= 1
			if self.air_time <= 0:
				self.jumping = False
				self.falling = True
	
	def collide1(self, rect_list):
		for rect in rect_list:
			if self.rect.colliderect(rect):
				if self.move[0] > 0:
					if self.rect.left == rect.right:
						self.move[0] = 0
						self.rect.right = rect.left
				if self.move[0] < 0:
					if self.rect.left == rect.right:
						self.move[0] = 0
						self.rect.left = rect.right
				if self.falling:
					self.move[1] = 0
					self.rect.bottom = rect.top
					self.air_time = self.true_air_time
				if self.move[1] < 0:
					if self.rect.top == rect.top:
						self.move[1] = 0
						self.rect.top = rect.bottom
						self.air_time = 0

#### Platform Class ####
# Mainly for side scrollers
class Platform(Entity):
	def __init__(self, x, y, w, h, grav, air_time, speed):
		super().__init__(x, y, w, h, grav, air_time, speed)
		self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
