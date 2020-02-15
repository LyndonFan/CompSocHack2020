
class Game:
    enemies = []
    bullets = []
    powers = []
    score = 0
    def initPlayer():
        from PlayerController import PlayerController
        Game.player = PlayerController()