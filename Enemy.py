import pygame
from Constants import Constants
from Game import Game
import random
import math
class Enemy(pygame.sprite.Sprite):


    width = 20
    height = 40.0
    follow_speed = 2.0

    def __init__(self, px,py,dx,dy):

        self.type = random.randint(0,2)
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([Enemy.width,Enemy.height])
        self.image.fill((0,200,0))

        self.rect = pygame.Rect(px-Enemy.width/2, py-Enemy.height/2, Enemy.width,Enemy.height)

        self.dx = 0
        self.dy = 0
        if self.type == 0:
            self.dx = random.choice([-5,-3,3,5])
            self.dy = random.choice([-5,-3,3,5])
        #place the enemy at the centre of the screen
        Game.enemies.append(self)
    def draw(self,surface):
        surface.blit(self.image,self.rect)

    def step(self):
        if self.type == 0:
            if (self.rect.left < 0 or self.rect.right > Constants.SCREEN_WIDTH):
                self.dx *= -1
            if (self.rect.top < 0 or self.rect.bottom > Constants.SCREEN_HEIGHT):
                self.dy *= -1
        else:
            if self.type == 1:
                self.target = Game.player.player.rect.center
            elif self.type == 2:
                self.target = Game.player.shadow.rect.center

            self.dx = self.target[0] - self.rect.x
            self.dy = self.target[1] - self.rect.y
            mag = math.sqrt(self.dx**2+self.dy**2)
            self.dx = float(Enemy.follow_speed*self.dx/mag)
            self.dy = float(Enemy.follow_speed*self.dy/mag)

        self.rect = self.rect.move(self.dx,self.dy)
    def shot(self):
        b = self.rect.collidelist(Game.bullets)
        if b >= 0:
            Game.bullets.pop(b)
            Game.score += 1

            return True
        return False

