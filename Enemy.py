import pygame
from Constants import Constants
from Game import Game
import random
import math
import os
class Enemy(pygame.sprite.Sprite):


    width = 30
    height = 30
    follow_speed = 2.0

    def __init__(self, px,py,dx,dy):

        self.type = random.randint(0,2)
        pygame.sprite.Sprite.__init__(self)
        if self.type==0:
        	self.image = pygame.transform.scale(pygame.image.load('sanic.png'), (Enemy.width,Enemy.height))
        elif self.type==2:
        	self.image = pygame.transform.scale(pygame.image.load('sandow.png'), (Enemy.width,Enemy.height))
        else:
        	self.image = pygame.transform.scale(pygame.image.load('sonic.png'), (Enemy.width,Enemy.height))
        #self.image.fill((0,200,0))

        self.rect = pygame.Rect(px-Enemy.width/2, py-Enemy.height/2, Enemy.width,Enemy.height)

        self.dx = 0
        self.dy = 0
        if self.type == 0:
            self.dx = random.choice([-5,-3,3,5])
            self.dy = random.choice([-5,-3,3,5])
            if self.dx<0:
            	self.image = pygame.transform.flip(self.image,True,False)
        #place the enemy at the centre of the screen
        Game.enemies.append(self)
    def draw(self,surface):
        surface.blit(self.image,self.rect)
        #pygame.draw.rect(surface,Constants.BLUE,self.rect,1)	#for testing

    def step(self):
        if self.type == 0:
            if (self.rect.left < 0 or self.rect.right > Constants.SCREEN_WIDTH):
                self.dx *= -1
                self.image = pygame.transform.flip(self.image,True,False)
            if (self.rect.top < 0 or self.rect.bottom > Constants.SCREEN_HEIGHT):
                self.dy *= -1
        else:
            if self.type == 1:
                self.target = Game.player.player.rect.center
            elif self.type == 2:
                self.target = Game.player.shadow.rect.center
            prev_dx = self.dx
            self.dx = self.target[0] - self.rect.x
            self.dy = self.target[1] - self.rect.y
            mag = math.sqrt(self.dx**2+self.dy**2)
            self.dx = float(Enemy.follow_speed*self.dx/mag)
            self.dy = float(Enemy.follow_speed*self.dy/mag)
            if (prev_dx==0 and self.dx<0) or prev_dx * self.dx < 0:
            	self.image = pygame.transform.flip(self.image,True,False)

        self.rect = self.rect.move(self.dx,self.dy)
    def shot(self):
        b = self.rect.collidelist(Game.bullets)
        if b >= 0:
            Game.bullets.pop(b)
            Game.score += 1

            return True
        return False

