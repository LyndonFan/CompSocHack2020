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

    def draw(self,surface):
        surface.blit(self.image,self.rect)

    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        # Did this update cause us to hit a wall?
        if self.rect.x < 0 or self.rect.x > Constants.SCREEN_WIDTH or self.rect.y < 0 or self.rect.y > Constants.SCREEN_HEIGHT:
            del self
