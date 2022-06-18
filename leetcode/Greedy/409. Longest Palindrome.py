import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = {}
        for c in s:
            if c in cnt:
                cnt[c] += 1
            else:
                cnt[c] = 1

        sume = 0
        sumo = 0
        is_odd = False

        for c in cnt.keys():
            if cnt[c] % 2 == 0:
                sume += cnt[c]
            else:
                sumo += cnt[c] - 1
                is_odd = True

        if is_odd:
            return sume + sumo + 1
        else:
            return sume + sumo


if __name__ == '__main__':
    Solution().longestPalindrome("aaabbb")