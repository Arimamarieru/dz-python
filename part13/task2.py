from math import ceil

class Turtle:

    def __init__(self, x: int = 0, y: int = 0, s: int = 1) -> None:
        if s <= 0:
            raise ValueError("Скорость s должна быть положительной.")
        self.x = x
        self.y = y
        self.s = s

    def go_up(self) -> None:
        self.y += self.s

    def go_down(self) -> None:
        self.y -= self.s

    def go_left(self) -> None:
        self.x -= self.s

    def go_right(self) -> None:
        self.x += self.s    

    def evolve(self) -> None:
        self.s += 1

    def degrade(self) -> None:
        if self.s == 1:
            raise ValueError("Скорость не может стать ≤ 0.")
        self.s -= 1

    def count_moves(self, x2: int, y2: int) -> int:
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        return ceil(dx / self.s) + ceil(dy / self.s)


if __name__ == "__main__":
    t = Turtle(0, 0, 2)
    t.go_up()                 
    t.go_right()              
    print(t.count_moves(10, -6))  
    t.evolve()                
    print(t.count_moves(10, -6))  
