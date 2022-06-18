from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ret = []
        wd = {}
        wordsd = {}

        tot_len = 0

        for word in words:
            tot_len += len(word)

            if word in wordsd:
                wordsd[word] += 1
            else:
                wordsd[word] = 1

            for c in word:
                if c in wd:
                    wd[c] += 1
                else:
                    wd[c] = 1

        wordsd_bkup = wordsd.copy()

        win_start = 0
        match_count = 0

        for win_end in range(len(s)):
            if s[win_end] in wd:
                wd[s[win_end]] -= 1

                if wd[s[win_end]] == 0:
                    match_count += 1

            win_size = win_end - win_start + 1

            if tot_len < win_size:
                if s[win_start] in wd:
                    wd[s[win_start]] += 1

                    if wd[s[win_start]] == 1:
                        match_count -= 1

                win_start += 1

            win_size = win_end - win_start + 1

            if tot_len == win_size:
                if match_count == len(wd):
                    n = len(words[0])
                    append = True
                    w_matches = 0

                    for i in range(len(words)):
                        w = s[win_start + i * n: win_start + (i + 1) * n]
                        if  w not in wordsd:
                            append = False
                        else:
                            wordsd[w] -= 1
                            if wordsd[w] == 0:
                                w_matches += 1
                    if append and w_matches==len(wordsd):
                        ret.append(win_start)
                    wordsd = wordsd_bkup.copy()

        return ret

if __name__ == '__main__':
    print(Solution().findSubstring(s = "abababab", words = ["ab", "ba"]))


