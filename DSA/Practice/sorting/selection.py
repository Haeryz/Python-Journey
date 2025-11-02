"""
Problem: Implement Selection Sort
Given an array of integers, sort it in ascending order using selection sort algorithm.

Hint: Selection sort divides the input list into two parts: a sorted sublist of items which is built up from left to right at the front (left) of the list and a sublist of the remaining unsorted items that occupy the rest of the list.

Example:
Input: [64, 25, 12, 22, 11]
Output: [11, 12, 22, 25, 64]
"""

class Solution:
    def selectionSort(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            min_idx = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
        return nums

if __name__ == "__main__":
    solution = Solution()
    # Test cases
    test_cases = [
        [64, 25, 12, 22, 11],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        []
    ]
    for i, nums in enumerate(test_cases):
        result = solution.selectionSort(nums.copy())
        print(f"Test case {i+1}: {result}")
