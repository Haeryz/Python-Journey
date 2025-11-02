"""
Problem: Implement Bubble Sort
Given an array of integers, sort it in ascending order using bubble sort algorithm.

Hint: Bubble sort works by repeatedly stepping through the list, comparing adjacent elements and swapping them if they are in the wrong order.
The pass through the list is repeated until the list is sorted.

Example:
Input: [64, 34, 25, 12, 22, 11, 90]
Output: [11, 12, 22, 25, 34, 64, 90]
"""

from typing import List

class Solution:
    def bubbleSort(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if (nums[j] > nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums

if __name__ == "__main__":
    solution = Solution()
    # Test cases
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        []
    ]
    for i, nums in enumerate(test_cases):
        result = solution.bubbleSort(nums.copy())
        print(f"Test case {i+1}: {result}")
