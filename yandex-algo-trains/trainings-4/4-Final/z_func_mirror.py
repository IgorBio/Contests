'''
Зеркальная z-функция
Строка S состоит из N букв. Зеркальная z-функция определяется для индекса i как максимально 
возможное k, такое что:

S[1] + S[2] + S[3] + … + S[k] = S[i] + S[i–1] + S[i–2] + ... + S[i–k+1]

Определите значение зеркальной z-функции для всех i от 1 до N.

Формат ввода
В первой строке записано одно число N (1 ≤ N ≤ 200000). 
Во второй строке записана строка длиной N символов, состоящая только из заглавных и строчных латинских букв.

Формат вывода
Выведите N чисел — значения функции для i от 1 до N.

Пример 1
Ввод	
5
BBABB
Вывод
1 2 0 1 5
Пример 2
Ввод
49
burannarubabyrrybaglipspiritmatankollokvzumbboyus
Вывод
1 0 0 0 0 0 0 0 0 10 0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0
'''

def mirror_z_function(N, S):
    z_function = [0] * N
    l, r = 0, 0  # Индексы самого правого отрезка [l, r], где S[l:r] совпадает с зеркальным S[0:r-l]

    for i in range(1, N):
        if i <= r:
            z_function[i] = min(r - i + 1, z_function[i - l])

        while i + z_function[i] < N and S[i - z_function[i]] == S[i + z_function[i]]:
            z_function[i] += 1

        if i + z_function[i] - 1 > r:
            l, r = i, i + z_function[i] - 1

    return z_function


if __name__ == "__main__":
    N = int(input())
    S = input()
    print(*mirror_z_function(N, S))