class CashBox:

    def __init__(self, amount: int = 0) -> None:
        if amount < 0:
            raise ValueError("Начальная сумма не может быть отрицательной.")
        self._amount = amount

    def top_up(self, x: int) -> None:
        if x <= 0:
            raise ValueError("Сумма пополнения должна быть положительной.")
        self._amount += x

    def count_1000(self) -> int:

        return self._amount // 1000

    def take_away(self, x: int) -> None:
      
        if x <= 0:
            raise ValueError("Сумма снятия должна быть положительной.")
        if x > self._amount:
            raise ValueError("Недостаточно денег в кассе.")
        self._amount -= x

    @property
    def amount(self) -> int:
    
        return self._amount



if __name__ == "__main__":
    cash = CashBox(3700)
    cash.top_up(800)          
    print(cash.count_1000()) 
    cash.take_away(2000)
    print(cash.amount)        
