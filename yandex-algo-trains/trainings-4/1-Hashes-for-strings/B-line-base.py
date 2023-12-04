'''
Основание строки
Строка S была записана много раз подряд, после чего от получившейся строки взяли префикс и дали вам.
Ваша задача определить минимально возможную длину исходной строки S.

Формат ввода
В первой и единственной строке входного файла записана строка, которая содержит только латинские буквы,
длина строки не превышает 50000 символов.

Формат вывода
Выведите ответ на задачу.

Пример 1
Ввод
zzz
Вывод
1
Пример 2
Ввод
bcabcab
Вывод
3
'''

def base_string(string: str) -> int:
    length = len(string)
    z_values = [0] * length
    right = 0
    for left in range(1, length):
        while right > 0 and string[left] != string[right]:
            right = z_values[right - 1]
        if string[left] == string[right]:
            right += 1
        z_values[left] = right
    return length - z_values[-1]

if __name__ == '__main__':
    assert base_string('zzz') == 1, 'Test 1'
    assert base_string('bcabcab') == 3, 'Test 2'
    print(base_string(input()))