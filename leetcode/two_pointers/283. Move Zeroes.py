class Solution_suboptimal_operations:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = 0
        num_zeros = 0
        # [0,1,0,3,12]
        # p1 = 0
        # p2 = 1
        # num_zeros = 1

        while p2 < len(nums):
            if nums[p2] != 0:
                nums[p1] = nums[p2]
                p1 += 1
            else:
                num_zeros += 1

            p2 += 1

        offset = len(nums) - num_zeros

        for i in range(num_zeros):
            nums[i + offset] = 0


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = 0
        # [0,1,0,3,12]
        # p1 = 0
        # p2 = 1
        # num_zeros = 1

        while p2 < len(nums):
            if nums[p2] != 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
            p2 += 1
