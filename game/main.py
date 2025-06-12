from game import Game
from constants import DEFAULT_WIDTH, DEFAULT_HEIGHT

if __name__ == '__main__':
    print('=== Forest Fire Hero ===')
    try:
        w=int(input(f'Ширина ({DEFAULT_WIDTH}) » ') or DEFAULT_WIDTH)
        h=int(input(f'Высота  ({DEFAULT_HEIGHT}) » ') or DEFAULT_HEIGHT)
    except ValueError:
        w,h=DEFAULT_WIDTH,DEFAULT_HEIGHT

    Game(w,h).run()
