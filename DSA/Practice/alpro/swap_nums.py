class Solution:
    def swap(self, a: int, b: int) -> tuple[int, int]:
        a, b = b, a
        return a, b

if __name__ == "__main__":
    s = Solution()
    print(s.swap(10, 20))