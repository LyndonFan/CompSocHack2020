import pygame
from Enemy import Enemy
from Constants import Constants
from PlayerController import PlayerController
from pygame.locals import *
import sys
import random
import math
from Player import Player
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((Constants.SCREEN_WIDTH,Constants.SCREEN_HEIGHT))
enemies = []

player = PlayerController()

for i in range(-10,10):
    th = random.random()*math.pi*2
    dx = i*math.cos(th)
    dy = i*math.sin(th)
    enemies.append(Enemy(Constants.SCREEN_WIDTH/2 ,Constants.SCREEN_HEIGHT/2 , dx, dy))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type in (pygame.KEYUP,pygame.KEYDOWN):
            if event.key in (pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN):
                player.handleEvent(event)


    screen.fill((0,0,0))
    for en in enemies:
        en.step()
        en.draw(screen)
    player.update()
    player.draw(screen)

    pygame.display.update()
    clock.tick(60)