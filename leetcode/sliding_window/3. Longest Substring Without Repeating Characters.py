class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        start_idx = 0
        count = 0
        max_count = 0

        for i, c in enumerate(s):
            if c not in dict:
                dict[c] = i
                count += 1
            else:
                for j in range(start_idx, dict[c]):
                    dict.pop(s[j])

                start_idx = dict[c] + 1
                count = i - start_idx + 1
                dict[c] = i
            max_count = max(count, max_count)

        return max_count