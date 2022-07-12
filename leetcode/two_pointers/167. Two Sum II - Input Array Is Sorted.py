class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # [2,7,15] # t=9
        # p1 = 0, p2=1
        #

        p1, p2 = 0, len(numbers) - 1

        while p1 < p2:
            if numbers[p1] + numbers[p2] == target:
                return p1 + 1, p2 + 1

            if numbers[p1] + numbers[p2] > target:
                p2 -= 1
            else:
                p1 += 1



