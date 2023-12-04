'''
Longest Substring Without Repeating Characters
Given a string s, find the length of the longest  substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.

Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

'''
The code uses a sliding window approach to keep track of the current substring
and a dictionary to store the last occurrence index of each character.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        result = 0
        start = 0
        
        for end in range(len(s)):
            if s[end] in chars:
                start = max(start, chars[s[end]] + 1)
            
            chars[s[end]] = end
            result = max(result, end - start + 1)
        
        return result
    
if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3, "Test 1"
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1, "Test 2"
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3, "Test 3"
