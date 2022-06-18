import collections


class Solution1:
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


class Solution:
    def longestPalindrome(self, s):
        ans = 0
        for v in collections.Counter(s).itervalues():
            ans += v / 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans

if __name__ == '__main__':
    Solution().longestPalindrome("aaabbb")