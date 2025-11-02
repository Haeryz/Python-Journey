from typing import List, Optional

class Solution:
    def find_largest(self, nums: list[int]) -> Optional[int]:
        for i in range(len(nums)):
            if nums[i] == max(nums):
                return nums[i]
            
if __name__ == "__main__":
    s = Solution()
    print(s.find_largest([10, 20, 30, 40, 50]))