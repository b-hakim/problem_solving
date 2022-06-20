class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        l = [0] * n

        l[:3] = [1, 2, 3]

        for i in range(3, n):
            l[i] = l[i - 1] + l[i - 2]

        return l[n - 1]
