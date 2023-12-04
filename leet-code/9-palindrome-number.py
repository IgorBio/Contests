'''
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
Constraints:
-2^31 <= x <= 2^31 - 1
 
Follow up: Could you solve it without converting the integer to a string?
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        return str(x) == str(x)[::-1]

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed = 0
        original = x

        while x > 0:
            reversed = (reversed * 10) + (x % 10)
            x //= 10

        return original == reversed


if __name__ == "__main__":
    assert Solution().isPalindrome(121), 'Test 1'
    assert not Solution().isPalindrome(-121), 'Test 2'
    assert not Solution().isPalindrome(10), 'Test 3'