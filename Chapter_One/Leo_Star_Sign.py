import pygame
pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

done = False
white = pygame.Color(255,255,255)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.rect(screen, white, (100, 500, 10, 10))
    pygame.draw.rect(screen, white, (300, 500, 10, 10))
    pygame.draw.rect(screen, white, (325, 400, 5, 5))

    pygame.draw.rect(screen, white, (600, 450, 20, 20))
    pygame.draw.rect(screen, white, (620, 400, 5, 5))
    pygame.draw.rect(screen, white, (635, 500, 5, 5))

    pygame.draw.rect(screen, white, (630, 750, 15, 15))
    pygame.draw.rect(screen, white, (800, 200, 5, 5))
    pygame.draw.rect(screen, white, (850, 240, 5, 5))

    pygame.display.update()
pygame.quit()
