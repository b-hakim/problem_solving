from typing import List


class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem = {}
        indices = {}

        for ind, i in enumerate(nums):
            rem[i] = target - i
            if i in indices:
                indices[i].append(ind)
            else:
                indices[i] = [ind]

        for idx, i in enumerate(nums):
            if rem[i] in indices:
                a = indices[rem[i]]
                if idx == a[0]:
                    if len(a) > 1:
                        return a[0], a[1]
                else:
                    return idx, a[0]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem = {}

        for ind, i in enumerate(nums):
            sub = target - i

            if sub in rem:
                return rem[sub], ind

            rem[i] = ind
