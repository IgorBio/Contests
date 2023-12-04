'''
The string "PAYPALISHIRING" is written in a zigzag pattern
on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
 
Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"

Constraints:
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = ['' for _ in range(numRows)]
        row, direction = 0, -1
        for char in s:
            rows[row] += char
            if row == 0 or row == numRows - 1:
                direction = -direction
            row += direction
        
        return ''.join(rows)
    
if __name__ == '__main__':
    assert Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR", 'Test 1'
    assert Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI", 'Test 2'
    assert Solution().convert("A", 1) == "A", 'Test 3'