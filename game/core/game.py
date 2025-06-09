# core/game.py
from time import sleep

from .config import GameConfig
from .field import GameMap
from .helicopter import Helicopter

class Game:

    def __init__(self, cfg: GameConfig):
        self.cfg = cfg
        self.map = GameMap(cfg)
        self.heli = Helicopter(self.map)
        self.tick_counter = 0

    def run(self):
        while True:
            self.tick_counter += 1
            print(f"Tick #{self.tick_counter}")
            sleep(self.cfg.tick_delay)

