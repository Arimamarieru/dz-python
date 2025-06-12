import random


class Weather:
    STATES = ("clear", "rain", "storm")

    def __init__(self):
        self.state = "clear"

    # ——— смена погоды ———
    def tick(self):
        r = random.random()
        if self.state == "clear" and r < 0.05:
            self.state = "rain"
        elif self.state == "rain" and r < 0.03:
            self.state = "storm"
        elif self.state == "rain" and r < 0.10:
            self.state = "clear"
        elif self.state == "storm" and r < 0.10:
            self.state = "rain"

    # ——— коэффициенты, зависящие от погоды ———
    @property
    def fire_factor(self) -> float:
        """Множитель вероятности пожара"""
        if self.state == "rain":
            return 0.5
        if self.state == "storm":
            return 2.0
        return 1.0

    @property
    def grow_factor(self) -> float:
        """Множитель роста деревьев"""
        return 1.2 if self.state == "rain" else 1.0

    # ——— вспомогательные ———
    def is_storm(self) -> bool:
        return self.state == "storm"

    @property
    def icon(self) -> str:
        """Символ в статусе"""
        return "☀" if self.state == "clear" else ("🌧" if self.state == "rain" else "⚡")
