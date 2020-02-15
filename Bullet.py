import pygame
import Constants

class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, change_x, change_y)):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
 
        # Set height, width
        self.image = pygame.Surface([2, 2])
        self.image.fill((120,120,120))
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        # Set speed vector
        self.change_x = change_x
        self.change_y = change_y
 
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
 
        if self.rect.x < 0 or self.rect.x > Constants.SCREEN_HEIGHT:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = Constants.SCREEN_HEIGHT
            else:
                self.rect.top = 0
