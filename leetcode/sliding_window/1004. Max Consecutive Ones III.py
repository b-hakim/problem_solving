from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        max_length = 0
        count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                ws = i - start + 1
                zeros = ws - count
                if k < zeros:
                    for j in range(start, i+1):
                        if nums[j] == 0:
                            start = j + 1
                            break
                        else:
                            count -= 1

            ws = i - start + 1

            if max_length < ws:
                max_length = ws

        return max_length

print(Solution().longestOnes([0,0,1,1,1,0,0], 0))