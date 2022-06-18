from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # loop on the string s, and track a window
        # if the current letter exiss in p, remove it from the dictionary representing s
        # else ignore
        # if the count of the window is > len of p, then shring window from beginning

        win_start = 0
        sdict = {}
        ret = []
        match_count = 0

        for c in p:
            if c in sdict:
                sdict[c] += 1
            else:
                sdict[c] = 1

        for win_end in range(len(s)):
            c = s[win_end]

            if s[win_end] in sdict:
                sdict[c] -= 1

                if sdict[c] == 0:
                    match_count += 1

            win_size = win_end - win_start + 1

            if win_size > len(p):
                if s[win_start] in sdict:
                    if sdict[s[win_start]] == 0:
                        match_count -= 1

                    sdict[s[win_start]] += 1
                win_start += 1

            if match_count == len(sdict):
                ret.append(win_start)

                sdict[s[win_start]] += 1
                match_count -= 1

                win_start += 1

        return ret


if __name__ == '__main__':
    print(Solution().findAnagrams("baa", "aa"))