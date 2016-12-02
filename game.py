import pygamefrom pygame.locals import *import randomimport sysfrom random import randintimport timefrom map import *from combat import *FPS = 60WINWIDTH = 640WINHEIGHT = 480HALF_WINWIDTH= int(WINWIDTH/2)HALF_WINHEIGHT= int(WINHEIGHT/2)class Images:	def __init__(self, x, y, image):		self.x = x		self.y = y		self.image = image			def draw(self, surface):		surface.blit(self.image, (self.x, self.y))class Pane(object):	def __init__(self):		pygame.init()		self.font = pygame.font.SysFont('Arial', 25)		pygame.display.set_caption('Box Test')		self.screen = DISPLAYSURF		self.screen.fill((white))		pygame.display.update()		def addRect(self):		self.rect = pygame.draw.rect(self.screen, (black), (175, 75, 200, 100), 2)		pygame.display.update()		def addText(self):		self.screen.blit(self.font.render('Hello I AM THE TRASH MAN!!!!', True, (255, 0, 0)), (200, 100))		pygame.display.update()class potion:	def __init__(self, mainMod, mainAmplifier, name, types, image, x, y):		self.mainMod = mainMod		self.mainAmplifier = mainAmplifier		self.name = name		self.types = types		self.image = image		self.x = x		self.y = yclass swordItem:	def __init__(self, speedMod, damage, extraMod, size, name, types):		self.speedMod = speedMod		self.damage = damage		self.extraMod = extraMod		self.size = size		self.name = name		self.types = typesclass Player:	def __init__(self, health, maxhealth, attack, speed, defense, level, exp, expneeded, gold, x, y, image, ):		self.health = health		self.maxhealth = maxhealth		self.attack = attack		self.speed = speed		self.defense = defense		self.level = level		self.exp = exp		self.expneeded = expneeded		self.gold = gold		self.x = x		self.y = y		self.image = image		self.height = 20		self.width = 10		def heal(self, amount):		self.health += amount		if self.health > self.maxhealth:			self.health = self.maxhealth		return self.health		def attacked(self, damage):		self.health -= damage		return self.health		def draw(self, surface):		surface.blit(self.image, (self.x, self.y))class Enemy:	def __init__(self, health, attack, defense, speed, name, exp, gold, x, y, facing, image, ):		self.health = health		self.attack = attack		self.defense = defense		self.speed = speed		self.name = name		self.exp = exp		self.gold = gold		self.x = x		self.y = y		self.facing = facing		self.image = image		self.width = 10		self.height = 10		def attacked(self, damage):		self.health -= damage		return self.health		def draw(self, surface):		surface.blit(self.image, (self.x, self.y))class Tile:	def __init__(self, image, x, y, occupied):		self.image = image		self.x = x		self.y = y		self.occupied = occupied		def defineConstants():	global sprites, enemies, inventory, equipped, hero, turns, swordSlash, wolf,facing	oldSword = swordItem(0, 5, 0, "Large", "Old Sword", "sword")	club = swordItem(-10, 15, 0, "Large", "Club", "sword")	dagger = swordItem(5, 5, 0, "Dual", "Dagger", "sword")		speedPotion = potion("speed", 5, "Speed Potion", "Potion", 'rabbit_up.png', 10, 10)	healthPotion = potion("instaHp", 20, "Health Potion", "Potion", 'healthPotion.png', 10, 20)		wolf = Enemy(40, 30, 5, 30, "Wolf", 20, 20, 20, 20, "right", pygame.image.load('wolf_down.png'))	hero = Player(100, 100, 10, 10, 0, 1, 0, 100, 15000, 0, 0, pygame.image.load('up.png'))	swordSlash = Images(pygame.image.load('right_swordSlash.png'), hero.x, hero.y - 5)		facing = 'down'	turns = 0	enemies = [wolf]	sprites = [hero, wolf]	hero.x = HALF_WINWIDTH	hero.y = HALF_WINHEIGHT		shopItems = [healthPotion, speedPotion, oldSword, club, dagger]	shopPrices = [20, 150, 15, 150, 30]	inventory = [[healthPotion], [], [], []]	equipped = []		inventoryImg = Images('inventory.png', 80, 100)	slashAttack = pygame.image.load('right_swordSlash.png')	myImage = pygame.image.load('up.png')				def main():	global FPSCLOCK,DISPLAYSURF		pygame.init()	FPSCLOCK = pygame.time.Clock()	#  pygame.display.set_icon(pygame.image.load(''))	DISPLAYSURF = pygame.display.set_mode((WINWIDTH,WINHEIGHT))	pygame.display.set_caption("RPG Game thing")	#BASICFONT = pygame.font.Font('freesansbold.ttf',32)	runGame()def runGame():		defineConstants()			# Game Loop	while 1:				DISPLAYSURF.fill((0, 0, 0))		drawMap()		updateSprites(sprites)						for event in pygame.event.get():			if event.type== pygame.QUIT:				terminate()						elif event.type==pygame.KEYDOWN:				global facing				swordOut = False								load()								check()								if event.key == pygame.K_UP or event.key==pygame.K_w:					hero.y-=10					hero.image=pygame.image.load('up.png')					facing = 'up'				if event.key== pygame.K_DOWN or event.key==pygame.K_s:					hero.y+=10					facing = 'down'					hero.image=pygame.image.load('down.png')				if event.key==pygame.K_LEFT or event.key==pygame.K_a:					hero.x-=10					facing = 'left'					hero.image = pygame.image.load('left.png')				if event.key==pygame.K_RIGHT or event.key==pygame.K_d:					hero.x+=10					facing = 'right'					hero.image=pygame.image.load('right.png')				print (facing + ' after direction')				if event.key==pygame.K_i:					displayInv()								if event.key==pygame.K_q:					combat(swordSlash, hero, wolf, facing)					swordOut = True					swordSlash.draw(DISPLAYSURF)																										if hero.x > WINWIDTH:					hero.x = 0				elif hero.x < 0:					hero.x = WINWIDTH				if hero.y > WINHEIGHT:					hero.y = 0				elif hero.y < 0:					hero.y = WINHEIGHT				print('player at' + str(hero.x) +',' + str(hero.y))								pygame.display.update()		FPSCLOCK.tick(FPS)def load():	cancel = False	if randint(0, 20) == 1:		newX = hero.x + randint(10, 15) * 10		newY = hero.y + randint(10, 15) * 10		enemyLoad = randint(0, 3)		for i in range(len(enemies)):			if enemies[i].x == newX:				if enemies[i].y == newY:					cancel = True		cancel = True		if enemyLoad == 0 and cancel == False and len(enemies) < 5:			rabbit = Enemy(10, 1, 1, 20, "Rabbit", 10, 5, newX, newY, "down", pygame.image.load('rabbit_up.png'))			enemies.append(rabbit)			sprites.append(rabbit)			print ("added rabbit")				if enemyLoad == 1 and cancel == False and len(enemies) < 5:			wolf = Enemy(40, 30, 5, 30, "Wolf", 20, 20, newX, newY, "down", pygame.image.load('wolf_down.png'))			enemies.append(wolf)			sprites.append(wolf)			print ("added wolf")		# if enemyLoad == 2 and cancel == False:		# Ape = Enemy(100, 20, 20, 10, "Ape", 50, 50, newX, newY, "down")		# enemies.append(Ape)		# print ("added ape")def shop():	shopping = True		for i in range(len(shopItems)):		print (str(i) + ") " + str(shopItems[i].name) + " " + str(shopPrices[i]))	while shopping == True:				print ("Which item number would you like to buy? Swords auto-equip themselves.")		into = int(input("<BUY>"))		if into == -1:			shopping = False		if into in range(0, len(shopItems)):			if hero.gold < shopPrices[into]:				print ("You don't have enough gold to buy this.")				shopping = False			else:				inventory.append(shopItems[into])				print ("You successfully bought a: " + str(shopItems[into].name))				shopping = False  # =-=-=-=-=SHOP=-=-=-=-=-def check():	swords = 0	for i in range(len(inventory)):		for j in range(len(inventory[i])):						if inventory[i][j].types == "sword":				equipped.append(inventory[i])				inventory.remove(inventory[i])				print ("equipped " + equipped[i].name)	for i in range(len(equipped)):		if equipped[i].types == "potion":			if equipped[i].mainMod == "speed":				hero.speed += equipped[i].mainAmplifier		if equipped[i].types == "sword":			if equipped[i].size == "Large":				swords += 2			if equipped[i].size == "Dual":				swords += 1			hero.attack += equipped[i].damage		if swords > 2:			if equipped[i].damage <= equipped[(i - 1)].damage:				pass	for i in range(len(enemies)):						distanceX = abs(enemies[i].x - hero.x)		distanceY = abs(enemies[i].y - hero.y)		if turns % 2 == 1:			if distanceX < 150 and distanceY < 150:				if distanceY < distanceX:					if enemies[i].x < hero.x:						enemies[i].facing = 'right'  # right						enemies[i].x += 10					elif enemies[i].x > hero.x:						enemies[i].facing = 'left'  # left						enemies[i].x -= 10  #				if distanceX < distanceY:					if enemies[i].y < hero.y:						enemies[i].facing = 'down'  # up						enemies[i].y += 10					elif enemies[i].y > hero.y:						enemies[i].facing = 'up'  # down						enemies[i].y -= 10		if enemies[i].x > WINWIDTH:			enemies[i].x = 0		if enemies[i].x < 0:			enemies[i].x = WINWIDTH		if enemies[i].y > WINHEIGHT:			enemies[i].y = 0		if enemies[i].y < 0:			enemies[i].y = WINHEIGHT				print (		str(enemies[i].name) + " at " + str(enemies[i].x) + "," + str(enemies[i].y) + " facing " + (enemies[i].facing))		if enemies[i].name == "Wolf":			if enemies[i].facing == 'down':				enemies[i].image = pygame.image.load('wolf_down.png')			if enemies[i].facing == 'up':				enemies[i].image = pygame.image.load('wolf_up.png')			if enemies[i].facing == 'left':				enemies[i].image = pygame.image.load('wolf_left.png')			if enemies[i].facing == 'right':				enemies[i].image = pygame.image.load('wolf_right.png')		if enemies[i].name == "Rabbit":			if enemies[i].facing == 'down':				enemies[i].image = pygame.image.load('rabbit_down.png')			if enemies[i].facing == 'up':				enemies[i].image = pygame.image.load('rabbit_up.png')			if enemies[i].facing == 'left':				enemies[i].image = pygame.image.load('rabbit_left.png')			if enemies[i].facing == 'right':				enemies[i].image = pygame.image.load('rabbit_right.png')		if len(inventory[1]) > 4:		inventory[2].append(inventory[1][5])		inventory[1].remove(inventory[1][5])def useItem():	print ("your inventory: ")	for i in range(len(inventory)):		print (str(i) + ") " + str(inventory[i].name))	using = True	used = int(input("<USE>"))	while using == True:				if used == -1:			using = False			print ("using canceled")				if used in range(len(inventory)):			if inventory[used].types == "Potion":								if inventory[used].mainMod == "instaHp":					hero.heal(inventory[used].mainAmplifier)				print ("Potion used")								if inventory[used].mainMod == "speed":					hero.speed += inventory[used].mainAmplifier								print ("Potion used")			using = Falsedef displayInv():	pygame.image.load('inventory.png')	for i in range(len(inventory)):		for j in range(len(inventory[i])):			pygame.image.load(str(inventory[i[j]]) + '.png')			def updateSprites(sprites):	for i in range(len(sprites)):				sprites[i].draw(DISPLAYSURF)	def terminate():	pygame.quit()	sys.exit()def drawMap():	for row in range(MAPHEIGHT):		for column in range(MAPWIDTH):			pygame.draw.rect(DISPLAYSURF,tileColor[tileMap[row][column]],(column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))						if __name__=='__main__':	main()