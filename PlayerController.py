from Player import Player
from Constants import Constants
import pygame
class PlayerController:
    def __init__(self):
        self.alive = True
        self.player = Player(Constants.SCREEN_WIDTH // 2 - 50, Constants.SCREEN_HEIGHT // 2, Constants.BLUE)
        self.shadow = Player(0,0,Constants.TRANS)
    def handleEvent(self,event):
        if self.alive:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.player.changespeed(-3, 0)
                    self.shadow.changespeed(3, 0)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.player.changespeed(3, 0)
                    self.shadow.changespeed(-3, 0)
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.player.changespeed(0, -3)
                    self.shadow.changespeed(0, 3)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.player.changespeed(0, 3)
                    self.shadow.changespeed(0, -3)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.shadow.changespeed(-3, 0)
                    self.player.changespeed(3, 0)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.shadow.changespeed(3, 0)
                    self.player.changespeed(-3, 0)
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.shadow.changespeed(0, -3)
                    self.player.changespeed(0, 3)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.shadow.changespeed(0, 3)
                    self.player.changespeed(0, -3)
    def reset(self):
    	self.player.change_x = 0
    	self.player.change_y = 0
    	self.shadow.change_x = 0
    	self.player.change_y = 0 



    def update(self,en):
        if self.player.rect.collidelist(en) >= 0:
            print("Collided with enemy")
            self.alive = False
        if self.shadow.rect.collidelist(en) >= 0:
            print("Collided with shadow")
            self.alive = False
        self.shadow.rect.x = Constants.SCREEN_WIDTH - self.player.rect.x - self.player.rect.width
        self.shadow.rect.y = Constants.SCREEN_HEIGHT - self.player.rect.y - self.player.rect.height
        self.player.update()
        self.shadow.update()

    def draw(self,surface):
        self.player.draw(surface)
        self.shadow.draw(surface)
