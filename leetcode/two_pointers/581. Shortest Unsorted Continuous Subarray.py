from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # find the start of the window that needs to be sorted
        # find the end of the window that needs to be sorted
        p1, p2 = -1, -1
        min_p2 = 10 ** 6
        max_num_so_far = nums[0]

        # [2,3,3,2,4]
        #
        # max_num_so_far = 2
        # min_p2 =
        # p1, p2 = -1, -1
        # i = 5

        for i in range(1, len(nums)):
            if nums[i] > max_num_so_far:
                max_num_so_far = nums[i]

            if p1 == -1:
                if nums[i - 1] > nums[i]:
                    p1 = i - 1
                    p2 = i
                    if nums[p2] < min_p2:
                        min_p2 = nums[p2]
            else:
                if nums[i - 1] > nums[i] or nums[i] < max_num_so_far:
                    p2 = i
                    if nums[p2] < min_p2:
                        min_p2 = nums[p2]

        if p1 == -1:
            return 0

        # [0,1,2,3, 4,5, 6]
        # [2,6,4,8,10,7,15]
        # max_num_so_far = 15
        # min_p2 = 4
        # p1, p2 = 1, 5
        # i = 5

        # print(p1, p2)

        for i in range(0, p1):
            if nums[i] > min_p2:
                # if i != 0:
                #     i -= 1
                p1 = i
                break

                # print(p1, p2)
        return p2 - p1 + 1


