from game import *
def combat( attack, obj, enemy, facing):

	if facing == 'right':
		attack.x = obj.x + 10
		attack.y = obj.y
	if facing == 'left':
		attack.x = obj.x - 10
		attack.y = obj.y
	if facing == 'down':
		attack.y = obj.y - 10
		attack.x = obj.x
	if facing == 'up':
		attack.y = obj.y + 10
		attack.x = obj.x
	
	print (facing + ' before draw')
	attack.image = pygame.image.load(facing + '_swordSlash.png')
	print (str(attack.image))
	if collide(obj, enemy):
		enemy.health -= obj.attack
		print("enemy's health is at " + str(enemy.health))
		return enemy.health
	
	else:
		return False

def collide(obja, objb):
	if obja.x < objb.x + objb.width and obja.x + obja.width > objb.x and obja.y < objb.y + objb.height and obja.y + obja.height > objb.y:
		print ('collide')
		return True
	else:
		print("didn't collide")
		return False