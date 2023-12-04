'''
Z-функция
Дана непустая строка S, длина которой N не превышает 106. Будем считать, что элементы строки нумеруются от 0 до N-1.
Вычислите z-функцию z[i] для всех i от 0 до N-1. z[i] определяется как максимальная длина подстроки,
начинающейся с позиции i и совпадающей с префиксом всей строки. z[0] = 0

Формат ввода
Одна строка длины N, 0 < N ≤ 106, состоящая из прописных латинских букв.

Формат вывода
Выведите N чисел — значения z-функции для каждой позиции, разделённые пробелом.

Пример
Ввод
abracadabra
Вывод
0 0 0 1 0 1 0 4 0 0 1 
'''

from typing import List

def z_function(string: str) -> List[int]:
    length = len(string)
    z_values = [0] * length
    left, right = 0, 0
    for idx in range(1, length):
        if idx <= right:
            z_values[idx] = min(right - idx + 1, z_values[idx - left])
        while idx + z_values[idx] < length and string[z_values[idx]] == string[idx + z_values[idx]]:
            z_values[idx] += 1
        if idx + z_values[idx] - 1 > right:
            left, right = idx, idx + z_values[idx] - 1
    return z_values

if __name__ == '__main__':
    assert z_function('abracadabra') == [0, 0, 0, 1, 0, 1, 0, 4, 0, 0, 1], 'Test 1'
    print(*z_function(input()))