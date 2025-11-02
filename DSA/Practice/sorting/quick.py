"""
Problem: Implement Quick Sort
Given an array of integers, sort it in ascending order using the quick sort algorithm.

Hint: Quick sort selects a pivot, partitions the array into elements less than and
greater than the pivot, and recursively sorts the partitions.

Example:
Input: [10, 7, 8, 9, 1, 5]
Output: [1, 5, 7, 8, 9, 10]
"""

from typing import List


class Solution:
	def quickSort(self, nums: List[int]) -> List[int]:
		self._quickSort(nums, 0, len(nums) - 1)
		return nums

	def _quickSort(self, nums: List[int], low: int, high: int) -> None:
		if low < high:
			pivot_index = self._partition(nums, low, high)
			self._quickSort(nums, low, pivot_index - 1)
			self._quickSort(nums, pivot_index + 1, high)

	def _partition(self, nums: List[int], low: int, high: int) -> int:
		pivot = nums[high]
		i = low - 1

		for j in range(low, high):
			if nums[j] <= pivot:
				i += 1
				nums[i], nums[j] = nums[j], nums[i]

		nums[i + 1], nums[high] = nums[high], nums[i + 1]
		return i + 1


if __name__ == "__main__":
	solution = Solution()
	test_cases = [
		[10, 7, 8, 9, 1, 5],
		[1, 2, 3, 4, 5],
		[5, 4, 3, 2, 1],
		[]
	]

	for i, nums in enumerate(test_cases):
		result = solution.quickSort(nums.copy())
		print(f"Test case {i+1}: {result}")
