import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
import sys
import pygame.font
pygame.font.init()

screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
screen_rect = screen.get_rect()

image = pygame.image.load('ship.bmp')
image_rect = image.get_rect()
image_rect.midleft = screen_rect.midleft
image_move_down = False
image_move_up = False


class Bullet (Sprite):
    """Bullet class to define bullets"""
    def __init__(self, image_rect):
        super(Bullet, self).__init__()
        self.rect = pygame.Rect(0, 0, 15, 3)
        self.color = (0, 0, 255)
        self.rect.midright = image_rect.midright
        
    def update(self):
        self.rect.x += 3
 
 
class Target(Sprite):
    """Target class to define target"""
    def __init__(self, screen_rect):
        super(Target, self).__init__()
        self.rect = pygame.Rect(400, 0, 100, 100)
        self.color = (255, 0, 0)
        self.rect.midright = screen_rect.midright
        self.speed = 1
        
class Button():
    """Make a play button to start the game"""
    def __init__(self, screen, msg):
        self.rect = pygame.Rect(0, 0, 200, 50)
        self.color = (0, 0, 255)
        self.rect.center = screen_rect.center
        self.font = pygame.font.SysFont(None, 42)
        self.prep_msg(msg)
        
        
    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, (255, 0, 0,), (0,0,255))
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        screen.fill(self.color, self.rect)
        screen.blit(self.msg_image, self.msg_image_rect)

msg = "PLAY"
game_active = False    
button = Button(screen, msg)    
bullets = Group()                
target = Target(screen_rect)
missed_targets = 0

while True:
    
    screen.fill((0, 255, 0))
    fire_bullet = False
    
    if game_active == False:
        button.draw_button()
    
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
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            if button.rect.collidepoint(mouse_position):
                game_active = True
        elif event.type == pygame.QUIT:
                sys.exit()
            
    if game_active:
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
        target.rect.y += target.speed
        if target.rect.bottom >= screen_height:
            target.speed *= -1
        elif target.rect.top <= 0:
            target.speed *= -1
        
        # Remove bullets and speed up game
        for bullet in bullets:
            screen.fill(bullet.color, bullet.rect)
            if pygame.sprite.collide_rect(bullet, target):
                bullets.remove(bullet)
                target.speed *= 2
            elif bullet.rect.x > screen_rect.right:
                missed_targets += 1
                bullets.remove(bullet)
                
        # Reset game active to return button to start screen, reset 
        # number of missed targets, and empty out bullet groups.
        if missed_targets > 3:
            game_active = False
            missed_targets = 0
            target.rect.midright = screen_rect.midright
            image_rect.midleft = screen_rect.midleft
            bullets.empty()
            target.speed = 1
        
    
    
    screen.fill(target.color, target.rect)
    screen.blit(image, image_rect)
    pygame.display.flip()
