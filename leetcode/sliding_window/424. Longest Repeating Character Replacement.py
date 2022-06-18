class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l_freq = {}
        start = 0
        max_repeating_count = 0
        window_repeating_count = 0
        max_valid_window_size = 0

        for i in range(0, len(s)):
            if s[i] not in l_freq:
                l_freq[s[i]] = 1
            else:
                l_freq[s[i]] += 1

            if l_freq[s[i]] > max_repeating_count:
                max_repeating_count = l_freq[s[i]]

            window_size = i - start + 1

            if window_size >= max_repeating_count:
                others = window_size - max_repeating_count
                if k < others:
                    for j in range(start, i):
                        l_freq[s[j]] -= 1
                        window_size = i - (j+1) + 1
                        others = window_size - max_repeating_count
                        start += 1
                        if k >= others:
                            break

                if max_valid_window_size < window_size:
                    max_valid_window_size = window_size

        return max_valid_window_size

print(Solution().characterReplacement("axxxjx",
                                      1))
