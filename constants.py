from Classes import *
from game import *
def defineConstants():
	oldSword = swordItem(0,5,0,"Large","Old Sword","sword")
	club = swordItem(-10,15,0,"Large","Club","sword")
	dagger = swordItem(5,5,0,"Dual","Dagger","sword")
	
	speedPotion = potion("speed",5,"Speed Potion","Potion",'rabbit_up.png',10,10)
	healthPotion = potion("instaHp",20,"Health Potion","Potion",'healthPotion.png',10,20)
	
	
	turns = 0
	
	shopItems= [healthPotion,speedPotion,oldSword,club,dagger]
	shopPrices= [20, 150, 15, 150, 30]
	inventory = [ [healthPotion] , [] , [] , [] ]
	equipped = []