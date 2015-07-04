import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
block_color = (53,115,255)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
#Resolução de tela
pygame.display.set_caption('A bit Racey')
#titulo da tela
clock = pygame.time.Clock()
#clock do jogo

carImg = pygame.image.load('img/racecar.png')

def things(thingx, thingy, thingw, thingh, color):
	pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def thing_dodged(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render("Dodged: "+str(count), True, black)
	gameDisplay.blit(text, [0,0])
def car(x,y):
	gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf, TextRect)
	pygame.display.update()

	time.sleep(2)

	game_loop()

def crash():
	message_display('You Crashed')


def game_loop():
	x = (display_width * 0.45)
	y = (display_height * 0.8)

	dodged = 0

	x_change = 0
	
	thing_startx = random.randrange(0,display_width)
	thing_starty = -600
	thing_speed = 4
	thing_width = 100
	thing_heigth = 100

	gameExit = False

	while not gameExit:
		#eventos por frame por segundo
		for event in pygame.event.get():
			#verificação de fechamento da tela
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0

		x += x_change

		gameDisplay.fill(white)

		#things(thingx, thingy, thingw, thingh, color):
		things(thing_startx, thing_starty, thing_width, thing_heigth, block_color)
		thing_starty += thing_speed

		car(x, y)
		thing_dodged(dodged)

		if x>display_width - car_width or x<0:
			crash()

		if thing_starty > display_height:
			thing_starty = 0 - thing_heigth
			thing_startx = random.randrange(0,display_width)
			dodged += 1
			thing_speed += 1
			thing_width += (dodged * 1.2)

		if y < thing_starty + thing_heigth:
			#print('y crossover')
			if x > thing_startx and x < thing_startx+thing_width or x+car_width > thing_startx and x+car_width < thing_startx+thing_width:
				#print('x crossover')
				crash()


		pygame.display.update()
		clock.tick(90)

game_loop()
pygame.quit()
quit()