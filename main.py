import pygame
from Enemy import Enemy
from Constants import Constants
from PlayerController import PlayerController
from Game import Game
from pygame.locals import *
import sys
import random
import math
from Player import Player
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((Constants.SCREEN_WIDTH,Constants.SCREEN_HEIGHT))

for i in range(1):
    th = random.random()*math.pi*2
    dx = 1#i*math.cos(th)
    dy = 1#i/10*math.sin(th)
    Game.enemies.append(Enemy(Constants.SCREEN_WIDTH/2 ,Constants.SCREEN_HEIGHT/2 , dx, dy))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            print("Score = " , Game.score)
            sys.exit()
        elif event.type in (pygame.KEYUP,pygame.KEYDOWN):
            if event.key in (pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN,pygame.K_SPACE ):
                Game.player.handleEvent(event)


    screen.fill((0,0,0))
    for en in Game.enemies:
        en.step()
        en.draw(screen)
    Game.enemies = [x for x in Game.enemies if not x.shot()]
    for b in Game.bullets:
        b.update()
        b.draw(screen)
    Game.player.update(Game.enemies)
    Game.player.draw(screen)

    pygame.display.update()
    clock.tick(60)