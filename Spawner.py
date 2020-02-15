
from Game import Game
from Enemy import Enemy
from Power import Power
from Constants import Constants
import random
import math
class Spawner:
    threshhold = 10000.0
    powerHold = 5000
    minEnemies = 1
    maxEnemies = 50
    lastSpawn = 0.0


    lastPower = 0.0
    def canPower(t):
        if t-Spawner.lastPower > Spawner.powerHold:
            Spawner.lastPower = t
            return True
        return False

    def power():
        spawned = False
        while not spawned:
            px = random.randint(0,Constants.SCREEN_WIDTH)
            py = random.randint(0,Constants.SCREEN_HEIGHT)
            if ((px-Game.player.player.rect.centerx)**2 + (py-Game.player.player.rect.centery)**2 > Constants.SAFE_ZONE**2):
                if ((px - Game.player.shadow.rect.centerx) ** 2 + (py - Game.player.shadow.rect.centery) ** 2 > Constants.SAFE_ZONE ** 2):
                    spawned = True
                    Power(px,py)

    def canSpawn(t):
        Spawner.minEnemies = 1.0+math.log(max(Game.score,1.0))
        if len(Game.enemies) < Spawner.minEnemies:
            Spawner.lastSpawn = t
            return True
        if len(Game.enemies) >= Spawner.maxEnemies:
            return False
        dt = t - Spawner.lastSpawn
        if (dt>Spawner.threshhold/(1.0+Game.score**0.1)):
            Spawner.lastSpawn = t
            return True
        return False
    def spawn():
        spawned = False
        while not spawned:
            px = random.randint(0,Constants.SCREEN_WIDTH)
            py = random.randint(0,Constants.SCREEN_HEIGHT)
            if ((px-Game.player.player.rect.centerx)**2 + (py-Game.player.player.rect.centery)**2 > Constants.SAFE_ZONE**2):
                if ((px - Game.player.shadow.rect.centerx) ** 2 + (py - Game.player.shadow.rect.centery) ** 2 > Constants.SAFE_ZONE ** 2):
                    spawned = True
                    Enemy(px,py,10,10)