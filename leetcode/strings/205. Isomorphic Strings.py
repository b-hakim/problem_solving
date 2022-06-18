class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_mapper = {}
        t_taken = {}

        for i in range(len(s)):
            if s[i] in s_mapper:
                if s_mapper[s[i]] != t[i]:
                    return False
            else:
                if t[i] in t_taken:
                    return False

                t_taken[t[i]] = True
                s_mapper[s[i]] = t[i]

        return True
