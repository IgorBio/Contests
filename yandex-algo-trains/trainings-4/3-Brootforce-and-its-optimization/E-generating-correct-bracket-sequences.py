'''
Генерация правильных скобочных последовательностей
По данному числу n выведите все правильные скобочные последовательности из
круглых и квадратных скобок длины n в лексикографическом порядке.

Формат ввода
Одно целое число n (0≤n≤16).

Формат вывода
Выведите все правильные скобочные последовательности из круглых и квадратных скобок длины n в лексикографическом порядке.
Каждая последовательность должна выводиться в новой строке.

Пример
Ввод
4
Вывод
(())
([])
()()
()[]
[()]
[[]]
[]()
[][]
'''

from typing import List


def generate_brackets(sequence: List[str], n: int, open_count: int, close_brackets: List[str]) -> None:
    if len(sequence) == 2 * n:
        print(''.join(sequence))
        return

    if open_count < n:
        sequence.append('(')
        close_brackets.append(')')
        generate_brackets(sequence, n, open_count + 1, close_brackets)
        close_brackets.pop()
        sequence.pop()

        sequence.append('[')
        close_brackets.append(']')
        generate_brackets(sequence, n, open_count + 1, close_brackets)
        close_brackets.pop()
        sequence.pop()

    if close_brackets:
        bracket = close_brackets.pop()
        sequence.append(bracket)
        generate_brackets(sequence, n, open_count, close_brackets)
        close_brackets.append(bracket)
        sequence.pop()


if __name__ == "__main__":
    n = int(input())
    if n > 0 and n % 2 == 0:
        sequence = []
        close_brackets = []
        generate_brackets(sequence, n / 2, 0, close_brackets)