
from Game import Game
from Enemy import Enemy
from Constants import Constants
import random
class Spawner:
    threshhold = 10000.0
    minEnemies = 1
    maxEnemies = 50
    lastSpawn = 0.0
    safeZone = 200.0
    def canSpawn(t):
        minEnemies = 1.0+math.max
        if len(Game.enemies) < Spawner.minEnemies:
            Spawner.lastSpawn = t
            return True
        if len(Game.enemies) >= Spawner.maxEnemies:
            return False
        dt = Spawner.lastSpawn - t
        if (dt>Spawner.threshhold/(1.0+Game.score**1.1)):
            Spawner.lastSpawn = t
            return True
        return False
    def spawn():
        spawned = False
        while not spawned:
            px = random.randint(0,Constants.SCREEN_WIDTH)
            py = random.randint(0,Constants.SCREEN_HEIGHT)
            if ((px-Game.player.player.rect.centerx)**2 + (py-Game.player.player.rect.centery)**2 > Spawner.safeZone**2):
                if ((px - Game.player.shadow.rect.centerx) ** 2 + (py - Game.player.shadow.rect.centery) ** 2 > Spawner.safeZone ** 2):
                    spawned = True
                    Enemy(px,py,10,10)