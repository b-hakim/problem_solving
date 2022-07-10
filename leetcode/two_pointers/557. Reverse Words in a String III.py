class Solution:
    def reverseWords(self, s: str) -> str:
        p1 = 0
        p2 = -1
        ret = []

        # 012345
        " ac ba"
        # p1 = 1
        # p2 = 3

        while p1 != len(s):
            w = None

            if s[p1] == " ":
                p1 += 1
            elif p2 == -1:
                p2 = p1 + 1
            elif p2 == len(s):
                w = s[p1:p2][::-1]
                p1 = p2
            elif s[p2] != " ":
                p2 += 1
            else:
                w = s[p1:p2][::-1]
                p1 = p2 + 1
                p2 = -1

            if w is not None:
                ret.append(w)
                w = None

        return " ".join(ret)