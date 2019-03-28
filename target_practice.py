import pygame
import pygame.sprite
import sys

screen = pygame.display.set_mode((1200, 800))
screen_rect = screen.get_rect()

image = pygame.image.load('ship.bmp')
image_rect = image.get_rect()
image_rect.midleft = screen_rect.midleft

while True:
    
    screen.fill((0, 255, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
        elif event.type == pygame.QUIT:
            sys.exit()
    
 
    
    
    screen.blit(image, image_rect)
    pygame.display.flip()
