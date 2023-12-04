'''
Анаграмма?
Задано две строки, нужно проверить, является ли одна анаграммой другой.
Анаграммой называется строка, полученная из другой перестановкой букв.

Формат ввода
Строки состоят из строчных латинских букв, их длина не превосходит 100000.
Каждая записана в отдельной строке.

Формат вывода
Выведите "YES" если одна из строк является анаграммой другой и "NO" в противном случае.

Пример 1
Ввод
dusty
study
Вывод
YES
Пример 2
Ввод
rat
bat
Вывод
NO
'''

def anagrams(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False

    char_count = {}

    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1

    for char in str2:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1

    return True
    

if __name__ == "__main__":
    str1 = input().strip()
    str2 = input().strip()
    print("YES" if anagrams(str1, str2) else "NO")