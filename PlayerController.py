from Player import Player
from Constants import Constants
import pygame
class PlayerController:
    def __init__(self):
        self.player = Player(Constants.SCREEN_WIDTH // 2 - 50, Constants.SCREEN_HEIGHT // 2, Constants.WHITE)
        self.shadow = Player(0,0,Constants.TRANS)
    def handleEvent(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.player.changespeed(-3, 0)
                self.shadow.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                self.player.changespeed(3, 0)
                self.shadow.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                self.player.changespeed(0, -3)
                self.shadow.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                self.player.changespeed(0, 3)
                self.shadow.changespeed(0, -3)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.shadow.changespeed(-3, 0)
                self.player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                self.shadow.changespeed(3, 0)
                self.player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                self.shadow.changespeed(0, -3)
                self.player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                self.shadow.changespeed(0, 3)
                self.player.changespeed(0, -3)
    def update(self):
        self.player.update()
        self.shadow.rect.x = Constants.SCREEN_WIDTH-self.player.rect.x
        self.shadow.rect.y = Constants.SCREEN_HEIGHT - self.player.rect.y
    def draw(self,surface):
        self.player.draw(surface)
        self.shadow.draw(surface)
