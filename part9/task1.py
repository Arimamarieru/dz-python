from math import factorial

def make_factorial_list(n: int) -> list[int]:

    k = factorial(n)
    return [factorial(i) for i in range(k, 0, -1)]

if __name__ == '__main__':
    n = int(input('Введите натуральное число: '))
    print(make_factorial_list(n))
