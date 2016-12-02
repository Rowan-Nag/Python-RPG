import pygame, sys
from pygame.locals import *
from game import *

green = (29, 209, 62)
blue = (56, 129, 224)
grey = (186, 184, 169)
yellow = (242, 178, 60)


grass = 0
water = 1
cave = 2
sand = 3

tileColor = {
	grass: green,
	water: blue,
	cave: grey,
	sand: yellow
}

grassRow = [grass,grass,grass]




tileMap = []


for i in range(100):
	grassRow.append(grass)
	tileMap.append(grassRow)




TILESIZE = 40
MAPWIDTH =len(grassRow)
MAPHEIGHT = len(tileMap)
