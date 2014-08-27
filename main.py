import pygame, sys, os, time
import common, events, graphics
from pygame.locals import *
from events import *
pygame.init()

common.width=1000
common.height=800
common.screen=pygame.display.set_mode([common.width,common.height])
pygame.display.set_caption("xombies")

def init():
	common.playing=True
	common.player=graphics.player
	common.zombie1=graphics.zombie1
	main()

def main():
	while common.playing==True:
		#process
		process_zombie=events.Zombie(None,None, None)
		process_zombie.search()
		common.last_frame+=1
		#display
		refresh()
		pygame.time.wait(50)

		for event in pygame.event.get():
			if event.type==QUIT:
				common.playing=False
				pygame.quit()
				sys.exit(0)
			elif event.type==KEYDOWN:
				key=event.key
				move_player=events.Player(common.player_pos[0],common.player_pos[1], None,None, key)
				move_player.move()

def refresh():
	common.screen.fill([0,0,0])
	for i in xrange(0,len(common.arena)):
		for n in xrange(0,len(common.arena[0])):
			if common.arena[i][n]==0:
				pygame.draw.rect(common.screen, (100,100,100),(n*50,i*50,50,50))
			elif common.arena[i][n]==1:
				pygame.draw.rect(common.screen, (0,0,0), (n*50,i*50,50,50))

	draw_player=events.Player(common.player_pos[0],common.player_pos[1], None, None, None)
	draw_player.draw()
	draw_zombs=events.Zombie(None,None,None)
	draw_zombs.draw()


	pygame.display.flip()


if __name__=='__main__':
	init()