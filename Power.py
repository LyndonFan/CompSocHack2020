import pygame
from Game import Game
class Power(pygame.sprite.Sprite):
    powerTime = 1000
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
        self.mode = random.randint(0,2)
        Game.powers.append(self)

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

