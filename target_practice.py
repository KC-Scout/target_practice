import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
import sys

screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
screen_rect = screen.get_rect()

image = pygame.image.load('ship.bmp')
image_rect = image.get_rect()
image_rect.midleft = screen_rect.midleft
image_move_down = False
image_move_up = False

target_rect = pygame.Rect(400, 0, 100, 100)
target_color = (255, 0, 0)
target_rect.midright = screen_rect.midright
target_direction = 1

class Bullet (Sprite):
    """Bullet class to define bullets"""
    def __init__(self, image_rect):
        super(Bullet, self).__init__()
        self.rect = pygame.Rect(0, 0, 15, 3)
        self.color = (0, 0, 255)
        self.rect.midright = image_rect.midright
        
    def update(self):
        self.rect.x += 3
        
bullets = Group()        
        



    
while True:
    
    screen.fill((0, 255, 0))
    fire_bullet = False
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
                
            # Move flag ships movement up and down 
            elif event.key == pygame.K_UP:
                image_move_up = True
            elif event.key == pygame.K_DOWN:
                image_move_down = True
                
            # Active bullet fired 
            elif event.key == pygame.K_SPACE:
                fire_bullet = True  
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                image_move_up = False
            if event.key == pygame.K_DOWN:
                image_move_down = False
        
        elif event.type == pygame.QUIT:
                sys.exit()
                
    # Move the image up and down
    if image_move_up and image_rect.top > screen_rect.top:
        image_rect.y -= 2
    elif image_move_down and image_rect.bottom < screen_rect.bottom:
        image_rect.y += 2
            
    # If bullet fired, add to bullets group
    if fire_bullet:
        new_bullet = Bullet(image_rect)
        bullets.add(new_bullet)
    bullets.update()
    
    # Move the Target up and down
    target_rect.y += target_direction
    if target_rect.bottom >= screen_height:
        target_direction *= -1
    elif target_rect.top <= 0:
        target_direction *= -1
        
    for x in bullets:
        screen.fill(x.color, x.rect)
      
    screen.fill(target_color, target_rect)
    screen.blit(image, image_rect)
    pygame.display.flip()
