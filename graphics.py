import pygame, os, sys, common, main
from pygame.locals import *
pygame.init()
pygame.display.init()

zombie1 = pygame.image.load(os.path.join(os.path.dirname(os.path.realpath(__file__)), "src", "mob", "zombie1.png")).convert_alpha()
player = pygame.image.load(os.path.join(os.path.dirname(os.path.realpath(__file__)), "src", "mob", "player.png")).convert_alpha()

spawner = pygame.image.load(os.path.join(os.path.dirname(os.path.realpath(__file__)), "src", "item", "spawner.png")).convert_alpha()
bullet = pygame.image.load(os.path.join(os.path.dirname(os.path.realpath(__file__)), "src", "item", "bullet.png")).convert_alpha()