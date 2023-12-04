'''
Все перестановки заданной длины
По данному числу N (0<N<10) выведите все перестановки чисел от 1 до N в лексикографическом порядке.

Пример 1
Ввод
1
Вывод
1
Пример 2
Ввод
2
Вывод
12
21
Пример 3
Ввод
3
Вывод
123
132
213
231
312
321
'''

from itertools import permutations


def range_permutations(N: int) -> str:
    for permutation in permutations(str(i) for i in range(1, N + 1)):
        yield ''.join(permutation)


if __name__ == '__main__':
    assert list(range_permutations(1)) == ['1']
    assert list(range_permutations(2)) == ['12', '21']
    assert list(range_permutations(3)) == ['123', '132', '213', '231', '312', '321']
    N = int(input())
    print('\n'.join(range_permutations(N)))