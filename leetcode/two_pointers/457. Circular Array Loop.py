class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        def sign(num):
            return 1 if num > 0 else -1

        for i in range(len(nums)):
            p1, p2 = i, i
            cycle_sign = sign(nums[i])

            """
            [2,-1,1,2,2]
            p1, p2 = 3, 0
            cycle_sign = +1
            """

            while True:
                p1 = (p1 + nums[p1]) % len(nums)  # one step
                p2 = (p2 + nums[p2]) % len(nums)
                s = sign(nums[p2])
                p2 = (p2 + nums[p2]) % len(nums)  # two steps

                if sign(nums[p1]) != cycle_sign or sign(nums[p2]) != cycle_sign or sign(s) != cycle_sign:
                    break

                if p1 == p2:
                    if p2 != (p2 + nums[p2]) % len(nums):
                        return True
                    else:
                        break