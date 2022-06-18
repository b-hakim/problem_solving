# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(version: int) -> bool:
    return 1

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n

        while left <= right:
            middle = (left + right) // 2
            a = isBadVersion(middle)

            if a:
                right = middle - 1
            else:
                left = middle + 1

        return left