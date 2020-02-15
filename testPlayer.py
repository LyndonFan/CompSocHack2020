import pygame
from Player import *

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TRANS = (255, 255, 255, 170)
BLUE = (50, 50, 255)
 
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 
# Set the title of the window
pygame.display.set_caption('Test')
 
# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()
 
# Create the player paddle object
player1 = Player(SCREEN_WIDTH//2 - 50, SCREEN_HEIGHT//2, WHITE)
player2 = Player(SCREEN_WIDTH//2 + 50, SCREEN_HEIGHT//2, TRANS)


all_sprite_list.add(player1)
all_sprite_list.add(player2)


clock = pygame.time.Clock()
 
done = False
 
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1.changespeed(-3, 0)
                player2.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player1.changespeed(3, 0)
                player2.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player1.changespeed(0, -3)
                player2.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player1.changespeed(0, 3)
                player2.changespeed(0, -3)
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player2.changespeed(-3, 0)
                player1.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player2.changespeed(3, 0)
                player1.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player2.changespeed(0, -3)
                player1.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player2.changespeed(0, 3)
                player1.changespeed(0, -3)
     
    all_sprite_list.update()
 
    screen.fill(BLACK)
 
    all_sprite_list.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()