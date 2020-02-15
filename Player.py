import pygame
from Constants import Constants
from Bullet import Bullet

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, clr):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(clr)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        
        self.bullets = []
 
    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y

    def draw(self,surface):
        surface.blit(self.image,self.rect)

    def shoot(self):
        self.bullets.append(Bullet(self.rect.x, self.rect.y, self.change_x, self.change_y))

    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        if self.rect.x < 0 or self.rect.x > Constants.SCREEN_WIDTH:
            if self.change_x > 0:
                self.rect.right = Constants.SCREEN_WIDTH
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = 0
        
        self.rect.y += self.change_y
 
        if self.rect.y < 0 or self.rect.y > Constants.SCREEN_HEIGHT:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = Constants.SCREEN_HEIGHT
            else:
                self.rect.top = 0
