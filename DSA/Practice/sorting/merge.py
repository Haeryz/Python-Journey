"""
Problem: Implement Merge Sort
Given an array of integers, sort it in ascending order using the merge sort algorithm.

Hint: Merge sort is a divide-and-conquer algorithm that splits the array into halves,
recursively sorts each half, and then merges the sorted halves.

Example:
Input: [38, 27, 43, 3, 9, 82, 10]
Output: [3, 9, 10, 27, 38, 43, 82]
"""

from typing import List


class Solution:
	def mergeSort(self, nums: List[int]) -> List[int]:
		if len(nums) <= 1:
			return nums

		mid = len(nums) // 2
		left = self.mergeSort(nums[:mid])
		right = self.mergeSort(nums[mid:])
		return self._merge(left, right)

	def _merge(self, left: List[int], right: List[int]) -> List[int]:
		merged: List[int] = []
		i = j = 0

		while i < len(left) and j < len(right):
			if left[i] <= right[j]:
				merged.append(left[i])
				i += 1
			else:
				merged.append(right[j])
				j += 1

		merged.extend(left[i:])
		merged.extend(right[j:])
		return merged


if __name__ == "__main__":
	solution = Solution()
	test_cases = [
		[38, 27, 43, 3, 9, 82, 10],
		[1, 2, 3, 4, 5],
		[5, 4, 3, 2, 1],
		[]
	]

	for i, nums in enumerate(test_cases):
		result = solution.mergeSort(nums.copy())
		print(f"Test case {i+1}: {result}")
