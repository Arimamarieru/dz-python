import random, json
from typing import List, Tuple
from constants import *

# ── параметры горения ──────────────────────────────────
FIRE_MIN_TICKS = 10   # дерево горит минимум 10 тиков
FIRE_MAX_TICKS = 25   # и максимум 25

class Board:
    """Игровое поле (лес, реки, строения) с живым огнём."""

    # ── создание карты ─────────────────────────────────
    def __init__(self, w: int = DEFAULT_WIDTH, h: int = DEFAULT_HEIGHT):
        self.w, self.h = w, h
        self.grid: List[List[str]] = [[TILE_EMPTY for _ in range(w)] for _ in range(h)]
        self.fire_age: List[List[int]] = [[0 for _ in range(w)] for _ in range(h)]

        self._gen_rivers()
        self._gen_trees()

        self.hospitals: List[Tuple[int, int]] = [
            self._place_unique(TILE_HOSPITAL) for _ in range(random.randint(1, 4))
        ]
        self.shop: Tuple[int, int] = self._place_unique(TILE_SHOP)

    # ── генерация окружения ─────────────────────────────
    def _inside(self, y, x) -> bool:
        return 0 <= y < self.h and 0 <= x < self.w

    def _place_unique(self, tile: str) -> Tuple[int, int]:
        while True:
            y, x = random.randrange(self.h), random.randrange(self.w)
            if self.grid[y][x] == TILE_EMPTY:
                self.grid[y][x] = tile
                return y, x

    def _gen_rivers(self, cnt: int = 2):
        for _ in range(cnt):
            if random.choice([True, False]):           # вертикальная река
                x = random.randrange(self.w)
                for y in range(self.h):
                    self.grid[y][x] = TILE_RIVER
            else:                                      # горизонтальная
                y = random.randrange(self.h)
                for x in range(self.w):
                    self.grid[y][x] = TILE_RIVER

    def _gen_trees(self, dens: float = 0.15):
        for y in range(self.h):
            for x in range(self.w):
                if self.grid[y][x] == TILE_EMPTY and random.random() < dens:
                    self.grid[y][x] = TILE_TREE

    def tick(self, weather):
        new_grid = [row[:] for row in self.grid]
        new_age  = [row[:] for row in self.fire_age]

        for y in range(self.h):
            for x in range(self.w):
                tile = self.grid[y][x]
                age  = self.fire_age[y][x]

                # рост деревьев
                if tile == TILE_EMPTY and random.random() < TREE_GROW_BASE * weather.grow_factor:
                    new_grid[y][x] = TILE_TREE

                # самовозгорание
                elif tile == TILE_TREE and random.random() < FIRE_START_BASE * weather.fire_factor:
                    new_grid[y][x] = TILE_FIRE
                    new_age[y][x] = random.randint(FIRE_MIN_TICKS, FIRE_MAX_TICKS)

                # жизнь огня
                elif tile == TILE_FIRE:
                    # распространение на соседей
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = y + dy, x + dx
                        if self._inside(ny, nx) and self.grid[ny][nx] == TILE_TREE and \
                                random.random() < FIRE_SPREAD_CH:
                            new_grid[ny][nx] = TILE_FIRE
                            new_age[ny][nx] = random.randint(FIRE_MIN_TICKS, FIRE_MAX_TICKS)
                    # тик_возраст
                    new_age[y][x] = age - 1
                    if new_age[y][x] <= 0:
                        new_grid[y][x] = TILE_ASH
                        new_age[y][x] = 0

        # молния в грозу
        if weather.is_storm() and random.random() < LIGHTNING_CH:
            y, x = random.randrange(self.h), random.randrange(self.w)
            if new_grid[y][x] == TILE_TREE:
                new_grid[y][x] = TILE_FIRE
                new_age[y][x] = random.randint(FIRE_MIN_TICKS, FIRE_MAX_TICKS)

        self.grid, self.fire_age = new_grid, new_age

    # ── действия игрока ─────────────────────────────────
    def extinguish(self, y: int, x: int) -> bool:
        if self._inside(y, x) and self.grid[y][x] == TILE_FIRE:
            self.grid[y][x] = TILE_TREE
            self.fire_age[y][x] = 0
            return True
        return False

    def burned(self, y, x) -> bool:
        return self._inside(y, x) and self.grid[y][x] == TILE_ASH

    def is_water(self, y, x) -> bool:
        """Вода под вертолётом *или* в соседней клетке."""
        if self._inside(y, x) and self.grid[y][x] == TILE_RIVER:
            return True
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx
            if self._inside(ny, nx) and self.grid[ny][nx] == TILE_RIVER:
                return True
        return False

    def is_hosp(self, y, x) -> bool:
        return (y, x) in self.hospitals

    # ── сохранение / загрузка ───────────────────────────
    def save_dict(self):
        return dict(
            w=self.w, h=self.h,
            grid=self.grid,
            fire_age=self.fire_age,
            hosp=self.hospitals,
            shop=self.shop,
        )

    @classmethod
    def from_dict(cls, d):
        b = cls(d['w'], d['h'])
        b.grid      = d['grid']
        b.fire_age  = d.get('fire_age', [[0]*b.w for _ in range(b.h)])
        b.hospitals = [tuple(p) for p in d['hosp']]
        b.shop      = tuple(d['shop'])
        return b
