import pygame
from Game import Game
from Constants import Constants
import random
class Power(pygame.sprite.Sprite):
    powerTime = 100
    def __init__(self,x,y):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Set height, width
        self.mode = random.randint(1,2)
        Game.powers.append(self)
        pic_name = ['','fast.png','radial.png']
        self.image = pygame.transform.scale(pygame.image.load(pic_name[self.mode]), (15,15))
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.centerx = x
        

    def draw(self,surface):
        surface.blit(self.image,self.rect)

    def update(self):
        if self.rect.colliderect(Game.player.player.rect):
            Game.player.player.shoot_mode = self.mode
            Game.player.player.power_counter = Power.powerTime
            Game.powers.remove(self)
        if self.rect.colliderect(Game.player.shadow.rect):
            Game.player.shadow.shoot_mode = self.mode
            Game.player.shadow.power_counter = Power.powerTime
            Game.powers.remove(self)

