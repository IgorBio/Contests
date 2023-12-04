'''
Равенство подстрок
Дана строка S, состоящая из строчных латинских букв.
Определите, совпадают ли строки одинаковой длины L, начинающиеся с позиций A и B.

Формат ввода
В первой строке записана S (1 ≤ |S| ≤ 2 ⋅ 105), состоящая из строчных латинских букв.
Во второй строке записано число Q (1 ≤ Q ≤ 2 ⋅ 105) — количество запросов.
В следющих Q строках записаны запросы: целые числа L, A и B (1 ≤ L ≤ |S|, 0 ≤ A, B ≤ (|S| - L)) —
длина подстрок и позиции, с которых они начинаются.

Формат вывода
Если строки совпадают — выведите "yes", иначе — "no".

Пример 1
Ввод
acabaca
3
4 3 2
3 4 0
2 0 1
Вывод
no
yes
no
Пример 2
Ввод
caeabaeadedcbdcdccec
10
13 4 3
2 12 15
10 1 3
3 8 15
13 5 6
7 2 6
9 8 8
19 0 0
19 0 0
6 7 13
Вывод
no
no
no
no
no
no
yes
yes
yes
no
'''

def check_substring_equality(string: str, L, A, B) -> str:
    if string[A: A + L] == string[B: B + L]:
        return 'yes'
    return 'no'

if __name__ == '__main__':
    assert check_substring_equality('acabaca', 4, 3, 2) == 'no', 'Test 1'
    assert check_substring_equality('acabaca', 3, 4, 0) == 'yes', 'Test 2'
    assert check_substring_equality('acabaca', 2, 0, 1) == 'no', 'Test 3'
    assert check_substring_equality('caeabaeadedcbdcdccec', 13, 4, 3) == 'no', 'Test 4'
    assert check_substring_equality('caeabaeadedcbdcdccec', 2, 12, 15) == 'no', 'Test 5'
    assert check_substring_equality('caeabaeadedcbdcdccec', 10, 1, 3) == 'no', 'Test 6'
    assert check_substring_equality('caeabaeadedcbdcdccec', 3, 8, 15) == 'no', 'Test 7'
    assert check_substring_equality('caeabaeadedcbdcdccec', 13, 5, 6) == 'no', 'Test 8'
    assert check_substring_equality('caeabaeadedcbdcdccec', 7, 2, 6) == 'no', 'Test 9'
    assert check_substring_equality('caeabaeadedcbdcdccec', 9, 8, 8) == 'yes', 'Test 10'
    assert check_substring_equality('caeabaeadedcbdcdccec', 19, 0, 0) == 'yes', 'Test 11'
    assert check_substring_equality('caeabaeadedcbdcdccec', 19, 0, 0) == 'yes', 'Test 12'
    assert check_substring_equality('caeabaeadedcbdcdccec', 6, 7, 13) == 'no', 'Test 13'
    string = input()
    Q = int(input())
    for _ in range(Q):
        L, A, B = map(int, input().split())
        print(check_substring_equality(string, L, A, B))