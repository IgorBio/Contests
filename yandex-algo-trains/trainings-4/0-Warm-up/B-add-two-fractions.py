'''
Сложить две дроби
Даны две рациональные дроби: a/b и c/d. Сложите их и результат представьте в виде несократимой дроби m/n.

Формат ввода
Программа получает на вход 4 натуральных числа a, b, c, d, каждое из которых не больше 100.

Формат вывода
Программа должна вывести два натуральных числа m и n такие, что m/n=a/b+c/d и дробь m/n – несократима.

Пример
Ввод
1 2 1 2
Вывод
1 1
'''

from typing import Tuple

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def add_fractions(a: int, b: int, c: int, d: int) -> Tuple[int, int]:
    numerator = a * d + b * c
    denominator = b * d
    common_divisor = gcd(numerator, denominator)

    m = numerator // common_divisor
    n = denominator // common_divisor

    return m, n


if __name__ == "__main__":
    a, b, c, d = map(int, input().split())
    m, n = add_fractions(a, b, c, d)
    print(m, n)