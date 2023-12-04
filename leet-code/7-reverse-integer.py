'''
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed
32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Constraints:
-231 <= x <= 231 - 1
'''

class Solution:
    def reverse(self, x: int) -> int:
        reversed = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        while x > 0:
            reversed = reversed * 10 + x % 10
            x //= 10
        
        reversed *= sign
        
        if reversed < -2**31 or reversed > 2**31-1:
            return 0
        
        return reversed
    

if __name__ == "__main__":
    assert Solution().reverse(123) == 321, 'Test 1'
    assert Solution().reverse(-123) == -321, 'Test 2'
    assert Solution().reverse(120) == 21, 'Test 3'
    assert Solution().reverse(1534236469) == 0, 'Test 4'