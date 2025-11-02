class solution:
    def swap_novar(self, a: int, b: int) -> tuple[int, int]:
        a = a + b
        b = a - b
        a = a - b
        return a, b


if __name__ == "__main__":
    s = solution()
    print(s.swap_novar(10, 5))