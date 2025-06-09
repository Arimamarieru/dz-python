import random
from typing import List, Tuple
from .objects import CellType
from .config import GameConfig

class GameMap:
    def __init__(self, cfg: GameConfig):
        self.cfg = cfg
        self.grid: List[List[CellType]] = [
            [CellType.EMPTY for _ in range(cfg.width)]
            for _ in range(cfg.height)
        ]
        self._generate_rivers()
        self._generate_trees()

        # координаты госпиталя и магазина
        self.hospital_pos = (0, 0)
        self.shop_pos     = (0, cfg.height - 1)

    # ---------- генерация ----------
    def _generate_rivers(self) -> None:
        for _ in range(self.cfg.river_count):
            self._carve_random_river()

    def _carve_random_river(self) -> None:
        if random.choice([True, False]):  # вертикальная река
            x = random.randrange(self.cfg.width)
            for y in range(self.cfg.height):
                self.grid[y][x] = CellType.RIVER
        else:                             # горизонтальная
            y = random.randrange(self.cfg.height)
            for x in range(self.cfg.width):
                self.grid[y][x] = CellType.RIVER

    def _generate_trees(self) -> None:
        placed = 0
        while placed < self.cfg.initial_trees:
            x, y = self.random_empty_cell()
            self.grid[y][x] = CellType.TREE
            placed += 1

    # ---------- утилиты ----------
    def inside(self, x: int, y: int) -> bool:
        return 0 <= x < self.cfg.width and 0 <= y < self.cfg.height

    def random_empty_cell(self) -> Tuple[int, int]:
        while True:
            x = random.randrange(self.cfg.width)
            y = random.randrange(self.cfg.height)
            if self.grid[y][x] == CellType.EMPTY:
                return x, y

    # ---------- обновление ----------
    def grow_trees(self) -> None:
        for y in range(self.cfg.height):
            for x in range(self.cfg.width):
                if (self.grid[y][x] == CellType.EMPTY and
                        random.random() < self.cfg.tree_growth_chance):
                    self.grid[y][x] = CellType.TREE

    def ignite_random_tree(self) -> None:
        if random.random() > self.cfg.fire_start_chance:
            return
        choices = [
            (x, y) for y in range(self.cfg.height)
                    for x in range(self.cfg.width)
                    if self.grid[y][x] == CellType.TREE
        ]
        if choices:
            x, y = random.choice(choices)
            self.grid[y][x] = CellType.FIRE

    def spread_fire(self) -> None:
        new_fires = []
        for y in range(self.cfg.height):
            for x in range(self.cfg.width):
                if self.grid[y][x] == CellType.FIRE:
                    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nx, ny = x+dx, y+dy
                        if (self.inside(nx,ny) and
                                self.grid[ny][nx] == CellType.TREE and
                                random.random() < self.cfg.fire_spread_chance):
                            new_fires.append((nx,ny))
                    self.grid[y][x] = CellType.BURNT
        for x, y in new_fires:
            self.grid[y][x] = CellType.FIRE

    # ---------- вывод ----------
    def render(self, heli) -> str:
        rows = []
        for y in range(self.cfg.height):
            row = ""
            for x in range(self.cfg.width):
                if (x, y) == (heli.x, heli.y):
                    row += "H"
                elif (x, y) == self.hospital_pos:
                    row += "♥"
                elif (x, y) == self.shop_pos:
                    row += "$"
                else:
                    row += self.grid[y][x]
            rows.append(row)
        return "\n".join(rows)

