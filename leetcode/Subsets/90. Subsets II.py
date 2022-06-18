from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        nums.sort()
        taken_nums = {}

        for num in nums:
            for i in range(len(subsets)):
                new_sub = tuple(subsets[i] + [num])
                if new_sub in taken_nums:
                   continue
                taken_nums[new_sub] = True
                subsets.append(list(new_sub))

        return subsets


if __name__ == '__main__':
    print(Solution().subsetsWithDup([1, 2, 2]))