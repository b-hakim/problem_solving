class Solution:
    def fib(self, n: int) -> int:
        i_1, i = 0, 1

        if n < 2:
            return n

        for j in range(2, n + 1):
            i_1, i = i, i + i_1

        return i
