from PlayerController import PlayerController
class Game:
    enemies = []
    bullets = []
    score = 0
    player = PlayerController()
    def initPlayer():
        Game.player = PlayerController()