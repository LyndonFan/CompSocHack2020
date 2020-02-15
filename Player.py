import pygame
from Constants import Constants
from Bullet import Bullet
from Game import Game
import math
class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, clr):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.clr = clr
        self.image.fill(clr)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        # Set speed vector
        self.change_x = 0
        self.change_y = 0

        self.shoot_countdown = 0
        self.power_counter = 0
        self.shoot_mode = 0
        self.clrs = [Constants.BLUE,Constants.RED,Constants.YELLOW,Constants.GREEN]

    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x * (2 if self.shoot_mode==1 else 1)
        self.change_y += y * (2 if self.shoot_mode==1 else 1)

    def draw(self,surface):
        surface.blit(self.image,self.rect)
        pygame.draw.circle(surface,self.clrs[self.shoot_mode],(self.rect.x,self.rect.y),int(Constants.SAFE_ZONE),2)

    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        if self.rect.x < 0 or self.rect.x > Constants.SCREEN_WIDTH - self.rect.width:
            if self.change_x > 0:
                self.rect.right = Constants.SCREEN_WIDTH
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = 0
        
        self.rect.y += self.change_y
 
        if self.rect.y < 0 or self.rect.y > Constants.SCREEN_HEIGHT - self.rect.height:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = Constants.SCREEN_HEIGHT
            else:
                self.rect.top = 0
        #logic for shooting modes
        if self.power_counter > 0:
            self.power_counter -= 1
            if self.power_counter == 0:
                print("Reset time")
                self.shoot_mode = 0

        if self.shoot_countdown==0:
            if self.shoot_mode == 0:
                mx,my = pygame.mouse.get_pos()
                dx = float(mx - self.rect.x)
                dy = float(my - self.rect.y)
                mag = math.sqrt(dx**2 + dy**2)
                if not(mag == 0):
                    dx *= 10.0 / mag
                    dy *= 10.0 / mag
                    Game.bullets.append(Bullet(self.rect.x, self.rect.y, dx, dy))
                self.shoot_countdown = 10
            if self.shoot_mode == 3:
                mx,my = pygame.mouse.get_pos()
                dx = float(mx - self.rect.x)
                dy = float(my - self.rect.y)
                mag = math.sqrt(dx**2 + dy**2)
                if not(mag == 0):
                    dx *= 10.0 / mag
                    dy *= 10.0 / mag
                    Game.bullets.append(Bullet(self.rect.x, self.rect.y, dx, dy))
                self.shoot_countdown = 1
            if self.shoot_mode == 2:
                for i in range(10):
                    th = float(math.pi*2*i/10.0)
                    Game.bullets.append(Bullet(self.rect.x,self.rect.y,10*math.cos(th),10*math.sin(th)))
                self.shoot_countdown = 10
        else:
            self.shoot_countdown -= 1
