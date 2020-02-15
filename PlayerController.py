from Player import Player
from Constants import Constants
import pygame
class PlayerController:
    def __init__(self):
        self.alive = True
        self.player = Player(Constants.SCREEN_WIDTH // 2 - 50, Constants.SCREEN_HEIGHT // 2, Constants.WHITE)
        self.shadow = Player(0,0,Constants.TRANS)
    def handleEvent(self,event):
        if self.alive:
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
                if event.key == pygame.K_SPACE:
                    print("TEST")
                    (mx,my) = pygame.mouse.get_pos()
                    self.player.shoot(mx,my)
                    self.shadow.shoot(mx,my)
                    #all_sprite_list.add(player1.bullets[-1])
                    #all_sprite_list.add(player2.bullets[-1])

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
           


    def update(self,en):
        if self.player.rect.collidelist(en) >= 0:
            print("Collided with enemy")
            self.alive = False
        if self.shadow.rect.collidelist(en) >= 0:
            print("Collided with shadow")
            self.alive = False
        self.player.update()
        self.shadow.rect.x = Constants.SCREEN_WIDTH - self.player.rect.x - self.player.rect.width
        self.shadow.rect.y = Constants.SCREEN_HEIGHT - self.player.rect.y - self.player.rect.height

    def draw(self,surface):
        self.player.draw(surface)
        self.shadow.draw(surface)
