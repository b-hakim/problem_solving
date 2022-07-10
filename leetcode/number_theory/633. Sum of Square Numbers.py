class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # bound: [0, sqrt(c)]

        for a in range(0, int(sqrt(c) + 1)):
            b = sqrt(c - a * a)

            if (b // 1) == b:
                return True

        return False