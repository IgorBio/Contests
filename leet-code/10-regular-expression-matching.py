'''
Given an input string s and a pattern p, implement regular expression matching with support
for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'.
Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 
Constraints:
1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*',
there will be a previous valid character to match.
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def backtrack(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == -1:
                result = i == -1
            elif i == -1:
                result = j > 0 and p[j] == '*' and backtrack(i, j - 2)
            elif p[j] == '*':
                result = (backtrack(i, j - 2) or
                          (p[j - 1] == s[i] or p[j - 1] == '.') and backtrack(i - 1, j))
            else:
                result = (p[j] == '.' or s[i] == p[j]) and backtrack(i - 1, j - 1)

            memo[(i, j)] = result
            return result

        return backtrack(len(s) - 1, len(p) - 1)

class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        memo = {}
        return self.match(text, pattern, 0, 0, memo)
    
    def match(self, text: str, pattern: str, text_index: int, pattern_index: int, memo: dict) -> bool:
        if (text_index, pattern_index) in memo:
            return memo[(text_index, pattern_index)]

        if len(pattern) == pattern_index:
            result = len(text) == text_index
        elif pattern_index + 1 < len(pattern) and pattern[pattern_index + 1] == '*':
            result = (self.match_asterisk(text, pattern, text_index, pattern_index + 2, memo) or
                      (text_index < len(text) and (pattern[pattern_index] == '.' or pattern[pattern_index] == text[text_index]) and
                       self.match(text, pattern, text_index + 1, pattern_index, memo)))
        elif text_index < len(text) and (pattern[pattern_index] == '.' or pattern[pattern_index] == text[text_index]):
            result = self.match(text, pattern, text_index + 1, pattern_index + 1, memo)
        else:
            result = False

        memo[(text_index, pattern_index)] = result
        return result
    
    def match_asterisk(self, text: str, pattern: str, text_index: int, pattern_index: int, memo: dict) -> bool:
        while text_index < len(text) and (pattern[pattern_index - 1] == '.' or pattern[pattern_index - 1] == text[text_index]):
            if self.match(text, pattern, text_index, pattern_index, memo):
                return True
            text_index += 1
        result = self.match(text, pattern, text_index, pattern_index, memo)
        memo[(text_index, pattern_index)] = result
        return result


    

if __name__ == '__main__':
    assert Solution().isMatch("aa", "a") == False, 'Test 1'
    assert Solution().isMatch("aa", "a*") == True, 'Test 2'
    assert Solution().isMatch("ab", ".*") == True, 'Test 3'
    assert Solution().isMatch("aaaaaaaaaaaaaaaaaaa", "a*a*a*a*a*a*a*a*a*b") == False, 'Test 4'