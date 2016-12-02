def defineClasses():
	
	class Images:
		def __init__(self,x,y,image):
			self.x = x
			self.y = y
			self.image = image

	
	class Pane(object):
		def __init__(self):
			pygame.init()
			self.font = pygame.font.SysFont('Arial', 25)
			pygame.display.set_caption('Box Test')
			self.screen = DISPLAYSURF
			self.screen.fill((white))
			pygame.display.update()
		
		def addRect(self):
			self.rect = pygame.draw.rect(self.screen, (black), (175, 75, 200, 100), 2)
			pygame.display.update()
		
		def addText(self):
			self.screen.blit(self.font.render('Hello I AM THE TRASH MAN!!!!', True, (255, 0, 0)), (200, 100))
			pygame.display.update()


	
	class potion:
		def __init__(self, mainMod, mainAmplifier, name, types, image, x, y):
			self.mainMod = mainMod
			self.mainAmplifier = mainAmplifier
			self.name = name
			self.types = types
			self.image = image
			self.x = x
			self.y = y

	
	class swordItem:
		def __init__(self, speedMod, damage, extraMod, size, name, types):
			self.speedMod = speedMod
			self.damage = damage
			self.extraMod = extraMod
			self.size = size
			self.name = name
			self.types = types
	
			
	class Player:
		def __init__(self, health, maxhealth, attack, speed, defense, level, exp, expneeded, gold, x, y, image, ):
			self.health = health
			self.maxhealth = maxhealth
			self.attack = attack
			self.speed = speed
			self.defense = defense
			self.level = level
			self.exp = exp
			self.expneeded = expneeded
			self.gold = gold
			self.x = x
			self.y = y
			self.image = image
			self.height = 20
			self.width = 10
		
		def heal(self, amount):
			self.health += amount
			if self.health > self.maxhealth:
				self.health = self.maxhealth
			return self.health
		
		def attacked(self, damage):
			self.health -= damage
			return self.health
		
		def draw(self, surface):
			surface.blit(self.image, (self.x, self.y))

	
	class Enemy:
		def __init__(self, health, attack, defense, speed, name, exp, gold, x, y, facing, image, ):
			self.health = health
			self.attack = attack
			self.defense = defense
			self.speed 	= speed
			self.name = name
			self.exp = exp
			self.gold = gold
			self.x = x
			self.y = y
			self.facing = facing
			self.image = image
			self.width = 10
			self.height = 10
		
		def attacked(self, damage):
			self.health -= damage
			return self.health
		
		def draw(self, surface):
			surface.blit(self.image, (self.x, self.y))
	
		
	class Tile:
		def __init__(self, image, x, y, occupied):
			self.image = image
			self.x = x
			self.y = y
			self.occupied = occupied
	
	global Images, Pane, potion, swordItem, Player, Enemy, Tile