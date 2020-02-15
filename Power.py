import pygame

class Power(pygame.sprite.Sprite):
    def __init__(self,x,y):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.clr = clr
        self.image.fill(clr)

        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.centerx = x
