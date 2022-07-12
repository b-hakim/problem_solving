class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        p = 0

        # [3,1,3,4,2]
        # p = 0

        while True:
            el = nums[p] - 1
            if el != p:
                if nums[el] - 1 == el:  # there is a duplicate
                    return el + 1
                else:
                    nums[p], nums[el] = nums[el], nums[p]
            else:
                p += 1
# this solution doesnt obey the constraint that arry shall be kept intact
