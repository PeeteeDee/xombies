import pygame
import common, graphics
from pygame.locals import *
pygame.init()

def spawn_mob():
	#
	to_spawn=0
	if common.round<=5:
		to_spawn=common.round*2
	elif common.round<=10:
		to_spawn=common.round*3
	elif common.round<=20:
		to_spawn=common.round*2
	else:
		to_spawn=common.round
	#

class Zombie(object):
	def __init__(self, x,y, species):
		self.x=x
		self.y=y
		self.type=species

	def search(self):
		if common.last_frame>=10:
			common.last_frame=0
			for i in xrange(0,len(common.zomb_list)):
				self.x=common.zomb_list[i][0]
				self.y=common.zomb_list[i][1]
				#print 'zombie', i,'\'s pos is', self.x, self.y

				if common.arena[self.y][self.x-2]==0:
					#print common.arena[self.y][self.x-1-1]
					if self.x>common.player_pos[0]:
						print 'move left'
						self.x-=1
				#print common.arena[self.y][self.x]
				if common.arena[self.y-1][self.x]==0:
					if self.x<common.player_pos[0]:
						print 'move right'
						self.x+=1

				#if self.y>common.player_pos[1]:
				#	print 'move up'
				#	self.y-=1
				#if self.y<common.player_pos[1]:
				#	print 'move down'
				#	self.y+=1
				common.zomb_list[i][0]=self.x
				common.zomb_list[i][1]=self.y


	def move(self):
		#gives zombies motion at speed according to self.species
		pass
	def attack(self):
		#gives damage to player according to self.species
		pass
	def draw(self):
		for i in xrange(0,len(common.zomb_list)):
			x=common.zomb_list[i][0]*50-50
			y=common.zomb_list[i][1]*50-50

			if common.zomb_list[i][2]==0:
				common.zombie1=pygame.transform.rotate(graphics.zombie1, 0)

			elif common.zomb_list[i][2]==1:
				common.zombie1=pygame.transform.rotate(graphics.zombie1, 90)
	  
			elif common.zomb_list[i][2]==2:
				common.zombie1=pygame.transform.rotate(graphics.zombie1, 90)
	  
			elif common.zomb_list[i][2]==3:
				common.zombie1=pygame.transform.rotate(graphics.zombie1, 270)

			common.screen.blit(common.zombie1, [x,y])
			#pygame.draw.rect(common.screen, (0,255,0), (x,y,50,50))


class Player(object):
	def __init__(self,x,y, weapon, ammo, key):
		self.x=x
		self.y=y
		self.weapon=weapon
		self.ammo=ammo
		self.key=key
	def spawn(self):
		self.ammo=100000

	def move(self):
		self.x-=1
		self.y-=1
		if self.key==273:
			if common.arena[self.y-1][self.x]==0:
				common.player_pos[1]-=1
				common.directytion='up'
		elif self.key==276:
			if common.arena[self.y][self.x-1]==0:
				common.player_pos[0]-=1
				common.direction='left'
		elif self.key==274:
			if common.arena[self.y+1][self.x]==0:
				common.player_pos[1]+=1
				common.direction='down'
		elif self.key==275:
			if common.arena[self.y][self.x+1]==0:
				common.player_pos[0]+=1
				common.direction='right'

	def shoot(self):
		pass
	def death(self):
		pass
	def draw(self):
		if common.direction=='up':
			common.player=pygame.transform.rotate(graphics.player, 180)

		elif common.direction=='left':
			common.player=pygame.transform.rotate(graphics.player, 270)
	  
		elif common.direction=='down':
			common.player=pygame.transform.rotate(graphics.player, 0)
	  
		elif common.direction=='right':
			common.player=pygame.transform.rotate(graphics.player, 90)

		common.screen.blit(common.player, [self.x*50-50,self.y*50-50])




#ignore, this was old version of Zombie.search()
def search(self):
	#searches for player
	if common.last_frame>=10:
		for i in xrange(0,len(common.zomb_list)):
			self.x=common.zomb_list[i][0]
			self.y=common.zomb_list[i][1]
			print self.x,self.y
			#check for wall here
			#if common.arena[self.y][self.x-1]!=1:
			if self.x>common.player_pos[0]:
				self.x-=1
				common.zomb_list[i][2]=3
			#here
			#if common.arena[self.y][self.x+1]!=1:
			if self.x<common.player_pos[0]:
				self.x+=1
				common.zomb_list[i][2]=1
			#here
			#if common.arena[self.y-1][self.x]:
			if self.y>common.player_pos[1]:
				self.y-=1
				common.zomb_list[i][2]=0
			#and here
			#if common.arena[self.y+1][self.x]:
			if self.y<common.player_pos[1]:
				self.y+=1
				common.zomb_list[i][2]=2

			common.zomb_list[i][0]=self.x
			common.zomb_list[i][0]=self.y
		common.last_frame=0