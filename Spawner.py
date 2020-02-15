
from Game import Game
class Spawner:
    threshhold = 10000.0
    minEnemies = 1
    maxEnemies = 50
    lastSpawn = 0.0
    def canSpawn(self,t):
        if len(Game.enemies) < Spawner.minEnemies:
            Spawner.lastSpawn = t
            return True
        if len(Game.enemies) >= Spawner.maxEnemies:
            return False
        dt = lastSpawn - t
        if (dt>Spawner.threshhold/Game.score**1.1):
            Spawner.lastSpawn = t
            return True
        return False