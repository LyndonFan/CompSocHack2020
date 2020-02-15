import pygame
from Enemy import Enemy
from Constants import Constants
from Game import Game
from pygame.locals import *
import sys
import random
import math
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((Constants.SCREEN_WIDTH,Constants.SCREEN_HEIGHT))

font = pygame.font.SysFont("arial", 24)

while True:

    Game.score = 0
    Game.enemies = []
    Game.bullets = []
    for i in range(10):
        th = random.random()*math.pi*2
        dx = i*math.cos(th)
        dy = i*math.sin(th)
        Game.enemies.append(Enemy(Constants.SCREEN_WIDTH/2 ,Constants.SCREEN_HEIGHT/2 , dx, dy))

    while Game.player.alive:
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

        text = font.render("SCORE: "+str(Game.score), True, (255, 255, 255))

        Game.player.draw(screen)
        screen.blit(text,(text.get_width() // 2, text.get_height() // 2))

        pygame.display.update()
        clock.tick(60)

    while not(Game.player.alive):
        for event in pygame.event.get():
            if event.type == QUIT:
                print("Score = " , Game.score)
                sys.exit()

        text = font.render("YOU DIED\nSCORE: "+str(Game.score)+"\nCLICK TO RESTART", True, (255, 255, 255))

        screen.fill((50,0,0))
        Game.player.draw(screen)
        screen.blit(text,(Constants.SCREEN_WIDTH//2 - text.get_width() // 2, Constants.SCREEN_HEIGHT//2 - text.get_height() // 2))
        pygame.display.update()
        clock.tick(60)
