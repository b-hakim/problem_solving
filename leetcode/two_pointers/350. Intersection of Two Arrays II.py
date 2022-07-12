class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # shorter, longer = nums1, nums2 if len(nums1) < len(nums2) else nums2, nums1

        counts1 = {}
        counts2 = {}

        for c in nums1:
            if c in counts1:
                counts1[c] += 1
            else:
                counts1[c] = 1
        for c in nums2:
            if c in counts2:
                counts2[c] += 1
            else:
                counts2[c] = 1

        ret = []

        for c in counts1:
            if c in counts2:
                ret.extend([c] * min(counts2[c], counts1[c]))

        return ret