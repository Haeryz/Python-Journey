class solution:
    def factorial(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

if __name__ == "__main__":
    s = solution()
    print(s.factorial(5))
    
