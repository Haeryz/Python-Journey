"""
Problem: Implement Insertion Sort
Given an array of integers, sort it in ascending order using insertion sort algorithm.

Hint: Insertion sort builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

Example:
Input: [12, 11, 13, 5, 6]
Output: [5, 6, 11, 12, 13]
"""
from typing import List

class Solution:
    def insertionSort(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
        return nums

if __name__ == "__main__":
    solution = Solution()
    # Test cases
    test_cases = [
        [12, 11, 13, 5, 6],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        []
    ]
    for i, nums in enumerate(test_cases):
        result = solution.insertionSort(nums.copy())
        print(f"Test case {i+1}: {result}")
