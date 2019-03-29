import pygame
import pygame.sprite
import sys

screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
screen_rect = screen.get_rect()

image = pygame.image.load('ship.bmp')
image_rect = image.get_rect()
image_rect.midleft = screen_rect.midleft

target_rect = pygame.Rect(400, 0, 100, 100)
target_color = (255, 0, 0)
target_rect.midright = screen_rect.midright
target_direction = 1

bullet_rect = pygame.Rect(0, 0, 15, 3)
bullet_color = (0, 0, 255)
fire_bullet = False

    
while True:
    
    screen.fill((0, 255, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
                
            # Move the ship up and down 
            elif event.key == pygame.K_UP:
                image_rect.y -= 45
            elif event.key == pygame.K_DOWN:
                image_rect.y += 45                
            # Active bullet fired 
            elif event.key == pygame.K_SPACE:
                bullet_rect.centery = image_rect.centery
                bullet_rect.centerx = image_rect.centerx
                fire_bullet = True
                
        elif event.type == pygame.QUIT:
                sys.exit()
                
    # Move the bullet across the screen if fired
    if fire_bullet:
        screen.fill(bullet_color, bullet_rect)
        bullet_rect.x += 1
    
    # Move the Target up and down
    target_rect.y += target_direction
    if target_rect.bottom >= screen_height:
        target_direction *= -1
    elif target_rect.top <= 0:
        target_direction *= -1
        
        
    screen.fill(target_color, target_rect)
    screen.blit(image, image_rect)
    pygame.display.flip()
