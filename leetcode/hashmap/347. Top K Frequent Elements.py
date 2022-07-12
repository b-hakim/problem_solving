from typing import List
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ret = set()
        freq = collections.defaultdict(int)
        counts = []

        for i in range(len(nums)):
            counts.append(set([]))

        for n in nums:
            freq[n] += 1
            counts[freq[n] - 1].add(n)

        for i in range(len(counts) - 1, -1, -1):
            if len(counts[i]) == k:
                return list(counts[i])

        # return list(ret)

ans = Solution().topKFrequent( [4,1,-1,2,-1,2,3], 2)

print(ans)