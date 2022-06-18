class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # loop on s
        # keep track of a dictionary with matched characters of t
        # if all keys are matched then compare with the minimum length window,
        td = {}

        for c in t:
            if c in td:
                td[c] += 1
            else:
                td[c] = 1

        win_start = 0
        match_count = 0

        min_win_size = 1000000000
        min_win_start_end = 0, -1

        for win_end in range(len(s)):
            if s[win_end] in td:
                td[s[win_end]] -= 1

                if td[s[win_end]] == 0:
                    match_count += 1

                if match_count == len(td):
                    # try to shrink from the left
                    for j in range(win_start, win_end+1):
                        win_size = win_end - win_start + 1

                        if win_size < min_win_size:
                            min_win_size = win_size
                            min_win_start_end = win_start, win_end

                        if s[j] in td:
                            if td[s[j]]+1 > 0:
                                break

                            td[s[j]] += 1

                        win_start = j+1

        return s[min_win_start_end[0]:min_win_start_end[1]+1]

if __name__ == '__main__':

    print(Solution().minWindow("ADOBECODEBANC", "ABC"))