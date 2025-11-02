import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..')))
from benchmark import benchmark

class Solution:
    def isPalindrome(self, x: int) -> bool:
        ohio = str(x)
        if ohio != ohio[::-1]:
            return False
        else:
            return True

if __name__ == "__main__":
    s = Solution()
    # Test cases with increasing digit lengths to observe O(n) behavior
    test_inputs = [121, 12321, 1234567890123456789012345678901234567890]
    times = benchmark(lambda inp: s.isPalindrome(inp), test_inputs)
    print("Benchmark times:", times)