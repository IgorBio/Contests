'''
Палиндром наибольшей длины
На вход программы подается строка, содержащая заглавные латинские буквы (не обязательно различные).
Разрешается переставлять буквы, а также удалять некоторые из них. Напишите программу,
которая из данных букв по указанным правилам составит и выведет палиндром наибольшей длины,
а если таких палиндромов несколько, то необходимо вывести первый из них в алфавитном порядке.

Sample Input 1:
AAB
Sample Output 1:
ABA
'''


def greatest_palindrome(s: str) -> str:
    counters = [0] * 26
    for c in s:
        counters[ord(c) - ord('A')] += 1
    result = middle = ''
    for i in range(26):
        result += chr(i + ord('A')) * (counters[i] // 2)
        if middle == '' and counters[i] % 2 == 1:
            middle = chr(i + ord('A'))

    return result + middle + result[::-1]


if __name__ == '__main__':
    print(greatest_palindrome(input()))