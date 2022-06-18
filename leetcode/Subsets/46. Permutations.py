from typing import List


class Solution_rec:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # loop on all numbers
        # consider this number as first element in the array
        # recursively do the same for the remainder of the array
        # append the first element to each of the elements returned by the array
        # keep track of which element is taken in a mask

        mask = 0

        return self.permute_rec(nums, mask)

    def permute_rec(self, nums, mask, header=[]):
        if pow(2, len(nums)) == mask+1:
            return [header]

        ret = []

        for i in range(len(nums)):
            if (mask & (1 << i)) >> i == 0:  # element not used before
                ret += self.permute_rec(nums, mask | (1 << i), header+[nums[i]])

        return ret

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        permutation = [[]]

        for num in nums:
            for i in range(len(permutation)):
                perm = permutation[i]
                permutation.pop(i)
                for j in range(len(perm)+1):
                    new_perm = [perm[0:j]+[num]+perm[j:]]

                    if len(new_perm) == len(nums):
                        ret.append(new_perm)
                    else:
                        permutation.append(new_perm)

        return ret

if __name__ == '__main__':
    print(Solution().permute([1, 2]))