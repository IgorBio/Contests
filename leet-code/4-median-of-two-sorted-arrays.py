'''
Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6
'''

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            mid1 = (low + high) // 2
            mid2 = (m + n + 1) // 2 - mid1

            max1 = float('-inf') if mid1 == 0 else nums1[mid1 - 1]
            min1 = float('inf') if mid1 == m else nums1[mid1]

            max2 = float('-inf') if mid2 == 0 else nums2[mid2 - 1]
            min2 = float('inf') if mid2 == n else nums2[mid2]

            if max1 <= min2 and max2 <= min1:
                if (m + n) % 2 == 0:
                    return (max(max1, max2) + min(min1, min2)) / 2
                else:
                    return max(max1, max2)
            elif max1 > min2:
                high = mid1 - 1
            else:
                low = mid1 + 1

    
if __name__ == '__main__':
    assert Solution().findMedianSortedArrays([1, 3], [2]) == 2.0, 'Test 1'
    assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5, 'Test 2'
    assert Solution().findMedianSortedArrays([0, 0], [0, 0]) == 0, 'Test 3'