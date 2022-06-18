class Solution_o_n2:
    def isSubsequence(self, s: str, t: str) -> bool:
        start_idx = 0

        for i in range(len(s)):
            # for j in range(start_idx, len(t)):
                idx = t[start_idx:].find(s[i])

                if idx == -1:
                    return False

                start_idx = idx + start_idx + 1
                print(start_idx)

        return True

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        curr_pos = 0

        for i in range(len(t)):
            if curr_pos == len(s):
                break

            if t[i] == s[curr_pos]:
                curr_pos += 1

        if curr_pos == len(s):
            return True
        else:
            return False
