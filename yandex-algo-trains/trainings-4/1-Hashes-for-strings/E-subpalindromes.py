'''
Подпалиндромы
Строка называется палиндромом, если она читается одинаково как слева направо, так и справа налево.
Например, строки abba, ata являются палиндромами.
Вам дана строка. Ее подстрокой называется некоторая непустая последовательность подряд идущих символов.
Напишите программу, которая определит, сколько подстрок данной строки является палиндромами.

Формат ввода
Вводится одна строка, состоящая из прописных латинских букв. Длина строки не превышает 100000 символов.

Формат вывода
Выведите одно число — количество подстрок данной строки, которые являются палиндромами

Пример 1
Ввод
aaa
Вывод
6
Пример 2
Ввод
aba
Вывод
4
'''

def manacher(string: str) -> int:
    seq = '#' + '#'.join(string) + '#'
    length = len(seq)
    z_values = [0] * length
    left_idx, right_idx = 0, 0
    count = 0
    for idx in range(length):
        if idx <= right_idx:
            z_values[idx] = min(right_idx - idx, z_values[2 * left_idx - idx])
        else:
            z_values[idx] = 0
        left, right = idx - z_values[idx] - 1, idx + z_values[idx] + 1
        while left >= 0 and right < length and seq[left] == seq[right]:
            z_values[idx] += 1
            left, right = left - 1, right + 1
        count += (z_values[idx] + 1) // 2
        if idx + z_values[idx] > right_idx:
            left_idx, right_idx = idx, idx + z_values[idx]
    return count

if __name__ == '__main__':
    assert manacher('aaa') == 6, 'Test 1'
    assert manacher('aba') == 4, 'Test 2'
    print(manacher(input()))