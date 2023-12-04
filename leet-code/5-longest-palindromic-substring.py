'''
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
 
Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        # Преобразование строки для обработки четных и нечетных палиндромов
        processed_str = "#".join("#" + s + "#")
        n = len(processed_str)

        # Массив для хранения длин палиндромов в каждой позиции
        p = [0] * n

        # Центр и правая граница самого правого палиндрома
        center = right_boundary = 0

        # Длина самого длинного палиндрома и его центр
        max_len = 0
        max_center = 0

        for i in range(n):
            if i < right_boundary:
                mirror = 2 * center - i
                p[i] = min(right_boundary - i, p[mirror])

            # Попытка расширить палиндром вокруг текущей позиции
            a = i + (1 + p[i])
            b = i - (1 + p[i])

            while a < n and b >= 0 and processed_str[a] == processed_str[b]:
                p[i] += 1
                a += 1
                b -= 1

            # Обновление центра и правой границы, если текущий палиндром выходит за пределы текущей границы
            if i + p[i] > right_boundary:
                center = i
                right_boundary = i + p[i]

            # Обновление информации о самом длинном палиндроме
            if p[i] > max_len:
                max_len = p[i]
                max_center = i

        # Извлечение самой длинной палиндромной подстроки
        start = (max_center - max_len) // 2
        end = start + max_len
        return s[start:end]
    
if __name__ == "__main__":
    assert Solution().longestPalindrome("babad") == "bab", "Test 1"
    assert Solution().longestPalindrome("cbbd") == "bb", "Test 2"