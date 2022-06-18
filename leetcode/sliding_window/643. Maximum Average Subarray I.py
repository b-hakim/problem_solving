class Solution(object):
    def findMaxAverage(self, nums, K):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sums = sum(nums[0:K])
        avgs = [sums / float(K)]

        for i in range(K, len(nums)):
            sums = sums - nums[i - K] + nums[i]
            avgs.append(sums / float(K))

        return max(avgs)

if __name__ == '__main__':
    print(Solution().findMaxAverage([4,0,4,3,3], 5))