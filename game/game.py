import os, json, random
from constants import *
from board      import Board
from weather    import Weather
from helicopter import Helicopter


class Game:
    """Главный игровой цикл и обработка ввода/вывода."""

    def __init__(self, w: int = DEFAULT_WIDTH, h: int = DEFAULT_HEIGHT):
        # Создаём поле
        self.board = Board(w, h)

        # вертолёт-случайная пустая клетка
        while True:
            y, x = random.randrange(h), random.randrange(w)
            if self.board.grid[y][x] == TILE_EMPTY:
                break
        self.heli    = Helicopter(y, x)
        self.weather = Weather()

        self.running = True
        self.status: str = '' 

    # ────────────────────────────────────────────────────
    #  Основной цикл
    # ────────────────────────────────────────────────────
    def run(self):
        while self.running and self.heli.lives > 0:
            self.tick()
            self.render()
            self.handle()
        print('Game over!')

    # ────────────────────────────────────────────────────
    #  Обновление состояния
    # ────────────────────────────────────────────────────
    def tick(self):
        self.weather.tick()
        self.board.tick(self.weather)

        # получаем урон, если стоим в огне
        if self.board.grid[self.heli.y][self.heli.x] == TILE_FIRE:
            self.heli.lives -= 1
            self.status = f'🔥 Обожглись! Жизней: {self.heli.lives}'

        # штраф очков за пепел под ногами
        if self.board.burned(self.heli.y, self.heli.x):
            self.heli.score -= 1

    # ────────────────────────────────────────────────────
    #  Отрисовка
    # ────────────────────────────────────────────────────
    def render(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        # карта
        for y in range(self.board.h):
            row = []
            for x in range(self.board.w):
                cell = TILE_HELICOPTER if (y, x) == (self.heli.y, self.heli.x) else self.board.grid[y][x]
                row.append(cell)
            print(''.join(row))

        # статус-панель
        print(f'Water {self.heli.water}/{self.heli.cap}'
              f' | Score {self.heli.score}'
              f' | Lives {self.heli.lives}'
              f' | Weather {self.weather.icon}')
        if self.status:
            print(self.status)
            self.status = ''

        # строка-подсказка
        print(f'[WASD] move  [{WATER_RELOAD_KEY}] reload  '
              f'[{EXTINGUISH_KEY}] extinguish  '
              f'[{HEAL_KEY}] heal  '
              f'[{UPGRADE_KEY}] upgrade  '
              '[*] save  [L] load  [X] exit')

    # ────────────────────────────────────────────────────
    #  Обработка ввода
    # ────────────────────────────────────────────────────
    def handle(self):
        raw = input('> ').strip()
        if not raw:
            return
        cmd = raw[0]

        # немодальные действия (работают в любом месте карты)
        if cmd in ('X', 'x'):
            self.running = False
            return
        if cmd == '*':
            self.save()
            return
        if cmd in ('L', 'l'):
            self.load()
            return

        # игровые действия
        low = cmd.lower()

        # движение
        if low in 'wasd':
            self.heli.move(low, self.board.w, self.board.h)

        # набор воды
        elif low == WATER_RELOAD_KEY:
            if self.board.is_water(self.heli.y, self.heli.x):
                self.heli.reload()
            else:
                self.status = '💧 рядом нет воды'

        # тушение
        elif low == EXTINGUISH_KEY:
            self.heli.extinguish(self.board)

        # лечение в больнице
        elif low == HEAL_KEY and self.board.is_hosp(self.heli.y, self.heli.x):
            if not self.heli.heal():
                self.status = '⛑ очков не хватает'

        # апгрейд в магазине
        elif low == UPGRADE_KEY and (self.heli.y, self.heli.x) == self.board.shop:
            if not self.heli.upgrade():
                self.status = '💰 очков не хватает'

    # ────────────────────────────────────────────────────
    #  Сохранение / загрузка
    # ────────────────────────────────────────────────────
    def save(self):
        with open(SAVE_FILE, 'w', encoding='utf-8') as f:
            json.dump({
                'board': self.board.save_dict(),
                'heli': self.heli.save_dict(),
                'weather': self.weather.state
            }, f, ensure_ascii=False)
        self.status = '💾 сохранено'

    def load(self):
        try:
            with open(SAVE_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
            self.board         = Board.from_dict(data['board'])
            self.heli          = Helicopter.from_dict(data['heli'])
            self.weather.state = data['weather']
            self.status = '📂 загружено'
        except FileNotFoundError:
            self.status = 'Файл не найден.'