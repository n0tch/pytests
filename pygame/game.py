import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
#Resolução de tela
pygame.display.set_caption('A bit Racey')
#titulo da tela
clock = pygame.time.Clock()
#clock do jogo

crashed = False

while not crashed:
	#eventos por frame por segundo
	for event in pygame.event.get():
		#verificação de fechamento da tela
		if event.type == pygame.QUIT:
			crashed = True

		print(event)

	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()