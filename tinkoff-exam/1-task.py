'''
Для вывески нового офиса Тинькофф были заказаны неоновые буквы.

В офис привезли какой-то набор из больших латинских букв. Проверьте, что из них действительно можно составить строку «TINKOFF» для вывески.
Тинькофф не хочет платить за лишние буквы, поэтому должны быть использованы все привезённые буквы.

Формат входных данных
Каждый тест состоит из нескольких наборов входных данных. В первой строке находится одно целое число t(1≤t≤100) — количество наборов входных данных.
Далее следует описание наборов входных данных. Единственная строка каждого набора входных данных содержит одну непустую строку из больших латинских букв длиной не более 20 символов — привезённый набор букв. 

Формат выходных данных
Для каждого набора входных данных, в отдельной строке, выведите «Yes» (без кавычек), если из всех привезённых букв можно составить строку «TINKOFF», и «No» иначе.
Вы можете выводить каждую букву в любом регистре (строчную или заглавную). Например, строки «yEs», «yes», «Yes» и «YES» будут приняты как положительный ответ.

Примеры данных
Ввод:
4
TINKOFF
TINKOFFF
AAAA
FFOKNIT
Вывод:
Yes
No
No
Yes
'''

from collections import Counter

def match_letters(word: str, letters: set) -> bool:
    if len(word) != len(letters):
        return False
    return Counter(word) == Counter(letters)


if __name__ == '__main__':
    assert match_letters('TINKOFF', 'TINKOFF'), 'Test 1'
    assert not match_letters('TINKOFF', 'TINKOFFF'), 'Test 2'
    assert not match_letters('TINKOFF', 'AAAA'), 'Test 3'
    assert match_letters('TINKOFF', 'FFOKNIT'), 'Test 4'
    n = int(input())
    for _ in range(n):
        letters = input()
        print('Yes' if match_letters('TINKOFF', letters) else 'No')