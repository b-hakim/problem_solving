from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rsum = sum(nums)
        lsum = 0

        for i in range(0, len(nums)):
            rsum -= nums[i]

            if lsum == rsum:
                return i

            lsum += nums[i]

        return -1