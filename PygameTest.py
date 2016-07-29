#Rectangles allow us to update a specific area rahter then the whole area

import pygame
import random as rd
import time as t

class Enemy:
	
	#Declares some local variables
	rectangle = None
	image = None

	#The __init__ function is special as it will always run the moment the class is called
	#Remember self allows the in-class function to use variables from the class's current instance
	def __init__(self):
		#Sets the current instance of image to the meteor image as an object
		self.image = pygame.image.load("Picture_cropped.png")
		#Scales the size of the image
		self.image = pygame.transform.scale(self.image, (50, 50))
		#Wraps the rectangle around the image so that it adjusts it's size if it is changed
		self.rectangle = self.image.get_rect()
		#These will randomly place the enemy: the second argument is so that the picture never sits off the screen
		self.rectangle.x = rd.randint(0, size[0] - self.rectangle.width)
		self.rectangle.y = rd.randint(0, size[1] - self.rectangle.height)
		#Randomly sets the speed and ensures that it is never 0
		self.speedX = rd.randint(-2, 2)
		while self.speedX == 0:
			self.speedX = rd.randint(-2, 2)
		self.speedY = rd.randint(-2, 2)
		while self.speedY == 0:
			self.speedY = rd.randint(-2, 2)
		
	def Move(self):
		self.rectangle.move_ip(self.speedX, self.speedY)

		#This block will ensure that no enemy will ever go outwith the window
		if self.rectangle.left < 0:
			self.speedX *= -1    
		if self.rectangle.top < 0:
			self.speedY *= -1
		if self.rectangle.right > size[0]:
			self.speedX *= -1
		if self.rectangle.bottom > size[1]:
			self.speedY *= -1


class Player:
	rectangle = None
	speed = 4
	image = None
	
	def __init__(self):
		self.image = pygame.image.load("GoodGuy.png")
		self.image = pygame.transform.scale(self.image, (30, 30))
		self.rectangle = self.image.get_rect()
		
		#This positions the player at the center of the screen at the beginning
		self.rectangle.x = size[0] // 2
		self.rectangle.y = size[1] // 2
		
	def Move(self):
		#This will take in key presses
		keys = pygame.key.get_pressed()
		#Calls the WallCollide function which returns 4 booleans testing if it is in contact with a wall
		canMoveUp, canMoveRight, canMoveDown, canMoveLeft = self.WallCollide(self.rectangle, self.speed)
		
		#Depending on the current key pressed, this will move the player
		if keys[pygame.K_UP] and canMoveUp:
			self.rectangle.move_ip(0, - self.speed)
		if keys[pygame.K_RIGHT] and canMoveRight:
			self.rectangle.move_ip(self.speed, 0)        
		if keys[pygame.K_DOWN] and canMoveDown:
			self.rectangle.move_ip(0, self.speed)
		if keys[pygame.K_LEFT] and canMoveLeft:
			self.rectangle.move_ip(- self.speed, 0)
			
	def WallCollide(self, rect, speed):
		#If '(rect.left - speed) > 0' is met, canMoveLeft will be True
		canMoveLeft = (rect.left - speed) > 0
		canMoveRight = (rect.right + speed) < size[0]
		canMoveUp = (rect.top - speed) > 0
		canMoveDown = (rect.bottom + speed) < size[1]
		
		return canMoveUp, canMoveRight, canMoveDown, canMoveLeft
		
		
def Collision(thingList):
	#Enumerate combines count with each item in the list as pairs eg 0,item1 1,item2...
	#Is the index counter and thing is the current item in the list
	#We do this so that we dont test for the player being in contact with itself
	for i, thing in enumerate(thingList):
		if i == 0:
			pass
		else:
			if thing.rectangle.colliderect(thingList[0].rectangle):
				print('Game Over')
				pygame.quit()

enemy_last_added_time = 0				
def add_thing(thingList , thing):
	global enemy_last_added_time
	if t.time() - enemy_last_added_time > 2:
		thingList.append(thing)
		enemy_last_added_time = t.time()
	return thingList


			
#Starts using pygame
pygame.init()
#Sets screen size as a tuple - static list
size = (1408, 700)
#Creates a new screen called 'screen' at size of the contents of variable 'size'
screen = pygame.display.set_mode(size)



thingList = []
thingList.append(Player())

for counter in range(5):
	thingList.append(Enemy())

isPaused = True

myfont = pygame.font.SysFont("HACKED", 20)

hsvacolor = pygame.Color(0, 0, 0, 0)
start = t.time()

while True:
	#Allows the program to quit
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	fps = 150    
	
	#Sets the hexadecimal value for the background colour
	color = [[102, 205, 170], [155, 23, 56], [45, 83, 43], [34, 76, 98]]


	hsvacolor.hsva = ( int((t.time()*100)%360) , 100 , 50 , 100)
	print(int((t.time()*100)%360) )
	

	'''
	counter += 1
	if counter < fps:
		screen.fill(color[0])
	elif counter < fps*2:
		screen.fill(color[1])
	elif counter < fps*3:
		screen.fill(color[2])
	elif counter < fps*4 :
		screen.fill(color[3])
	else:
		counter = 0
	'''
	screen.fill(hsvacolor)	
   
	timeElapsed = (t.time() - start) // 1
	
	label = myfont.render("Score = {0}".format(timeElapsed), 1, (255,255,0))

	if timeElapsed == 20:
		thingList = add_thing(thingList, Enemy())

	if timeElapsed == 30:
		thingList = add_thing(thingList, Enemy())
		thingList = add_thing(thingList, Enemy())

	if timeElapsed == 40:
		thingList = add_thing(thingList, Enemy())
		thingList = add_thing(thingList, Enemy())
		thingList = add_thing(thingList, Enemy())

	if timeElapsed == 50:
		thingList = add_thing(thingList, Enemy())
		thingList = add_thing(thingList, Enemy())
		thingList = add_thing(thingList, Enemy())
		thingList = add_thing(thingList, Enemy())

	if timeElapsed == 60:
		thingList = add_thing(thingList, Enemy())
		thingList = add_thing(thingList, Enemy())
		thingList = add_thing(thingList, Enemy())
		thingList = add_thing(thingList, Enemy())
		thingList = add_thing(thingList, Enemy())

	if timeElapsed == 70:
		thingList = add_thing(thingList, Enemy())
		thingList = add_thing(thingList, Enemy())
		thingList = add_thing(thingList, Enemy())
		thingList = add_thing(thingList, Enemy())
		thingList = add_thing(thingList, Enemy())
		thingList = add_thing(thingList, Enemy())

	#This block calls the move function for each thing in thingList
	for thing in thingList:
		thing.Move()
		#blit draws the items images and rectangles to the screen
		screen.blit(thing.image, thing.rectangle)
	
	screen.blit(label, (10, 10))
	
	#Updates the current display or if there are multiple displays, it will switch to the other one
	pygame.display.flip()

	Collision(thingList)
	
	#Limits the FPS to 150FPS
	pygame.time.wait(1000 // fps)
	
	
	while isPaused:
		pygame.event.pump()
		
		pygame.display.flip()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			isPaused = False
pygame.time.wait(200)