import pygame
from Constants import Constants
from Game import Game
class Enemy(pygame.sprite.Sprite):


    width = 20
    height = 40.0

    def __init__(self, px,py,dx,dy):


        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([Enemy.width,Enemy.height])
        self.image.fill((0,200,0))

        self.rect = pygame.Rect(px-Enemy.width/2, py-Enemy.height/2, Enemy.width,Enemy.height)
        self.dx = dx
        self.dy = dy
        #place the enemy at the centre of the screen

    def draw(self,surface):
        surface.blit(self.image,self.rect)

    def step(self):
        if (self.rect.left < 0 or self.rect.right > Constants.SCREEN_WIDTH):
            self.dx *= -1
        if (self.rect.top < 0 or self.rect.bottom > Constants.SCREEN_HEIGHT):
            self.dy *= -1
        self.rect = self.rect.move(self.dx,self.dy)
    def shot(self):
        if self.rect.collidelist(Game.bullets) >= 0:
            print("Enemy was shot")
            Game.score += 1
            return True
        return False

