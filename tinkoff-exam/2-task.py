'''
Тинькофф начал разрабатывать новый проект. Для этого было подобрано n разработчиков.
У i-го разработчика есть порог социальности ai, это значит, что он готов контактировать напрямую с не более чем ai другими разработчиками.
Определите, можно ли наладить контакт между какими-то парами разработчиков, так чтобы любые два контактировали либо напрямую, либо через других разработчиков.

Формат входных данных
Каждый тест состоит из нескольких наборов входных данных.
В первой строке находится одно целое число t(1≤t≤1000) — количество наборов входных данных. Далее следует описание наборов входных данных.
Первая строка каждого набора входных данных содержит одно число n(1≤n≤10^5) — количество разработчиков.
Вторая строка содержит n натуральных чисел ai(1≤ai≤10^9) — пороги социальностей разработчиков. Гарантируется, что сумма значений n по всем наборам входных данных не превосходит 10^5.

Формат выходных данных
Для каждого набора входных данных, выведите «Yes», если можно наладить контакт между программистами, и «No» иначе.
Вы можете выводить каждую букву в любом регистре (строчную или заглавную). Вы можете выводить каждую букву в любом регистре (строчную или заглавную).
Например, строки «yEs», «yes», «Yes» и «YES» будут приняты как положительный ответ.

Примеры данных
Ввод:
4
1
1000000000
2
1 1
3
1 1 1
4
1 1 2 2
Вывод:
Yes
Yes
No
Yes
'''

from typing import List

def match_developers(n: int, thresholds: List[int]) -> bool:
    return sum(thresholds) >= 2 * (n - 1)

if __name__ == '__main__':
    assert match_developers(1, [1]) is True, 'Test 1'
    assert match_developers(2, [1, 1]) is True, 'Test 2'
    assert match_developers(3, [1, 1, 1]) is False, 'Test 3'
    assert match_developers(3, [1, 1, 2]) is True, 'Test 4'
    assert match_developers(4, [1, 1, 2, 2]) is True, 'Test 5'
    assert match_developers(4, [1, 1, 2, 1]) is False, 'Test 6'
    assert match_developers(5, [1, 1, 2, 2, 2]) is True, 'Test 7'
    assert match_developers(5, [1, 1, 1, 2, 3]) is True, 'Test 8'
    assert match_developers(6, [1, 1, 2, 2, 2, 2]) is True, 'Test 9'
    for _ in range(int(input())):
        n = int(input())
        thresholds = list(map(int, input().split()))
        print('Yes' if match_developers(n, thresholds) else 'No')