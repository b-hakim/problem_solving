from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]

        for num in nums:
            for i in range(len(subsets)):
                sub = subsets[i]
                subsets.append(sub + [num])

        return subsets

print(Solution().subsets([1, 2, 3]))