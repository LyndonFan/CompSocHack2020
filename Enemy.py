import pygame
from Constants import Constants
class Enemy:


    width = 20
    height = 40.0

    def __init__(self, px,py,dx,dy):
        self.rect = pygame.Rect(px-Enemy.width/2, py-Enemy.height/2, Enemy.width,Enemy.height)
        self.dx = dx
        self.dy = dy
        #place the enemy at the centre of the screen

    def draw(self,surface):
        pygame.draw.rect(surface, (0,255,0),self.rect)

    def step(self):
        if (self.rect.left < 0 or self.rect.right > Constants.SCREEN_WIDTH):
            self.dx *= -1
        if (self.rect.top < 0 or self.rect.bottom > Constants.SCREEN_HEIGHT):
            self.dy *= -1
        self.rect = self.rect.move(self.dx,self.dy)

