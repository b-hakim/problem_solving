class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums = [-1,-100,3,  99,2]
        # nums = [99, 2,-1,-100,3]
        # k = 2
        # n = 5
        # rotated_elements = [99, 2]
        # i = 0
        # s1 = 2

        n = len(nums)
        k %= n
        rotated_elements = nums[n - k:].copy()

        s1 = n - k - 1

        for i in range(s1, -1, -1):
            nums[i + k] = nums[i]

        for i in range(k):
            nums[i] = rotated_elements[i]
