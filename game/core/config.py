from dataclasses import dataclass

@dataclass
class GameConfig:
    # размеры поля по умолчанию
    width: int = 20
    height: int = 10

    # генерация
    initial_trees: int = 30
    river_count: int = 2

    # шансы и скорость
    tick_delay: float = 0.3          # задержка цикла (сек)
    tree_growth_chance: float = 0.02
    fire_start_chance: float = 0.01
    fire_spread_chance: float = 0.15

    # вертолёт и экономика
    lives: int = 3
    water_capacity: int = 1
    score_per_tree: int = 5
    score_per_burnt: int = -3
    hospital_cost: int = 20
    shop_cost: int = 30

