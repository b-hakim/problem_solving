class Solution:
    def validPalindrome(self, s: str) -> bool:
        p1, p2 = 0, len(s) - 1
        deleted_idx = -1
        alternative_path = None

        while p1 < p2:
            if s[p1] != s[p2]:
                if deleted_idx != -1:  # already deleted accured and new issue arised, then try the other alternative
                    if alternative_path is None:
                        return False
                    p1, p2 = alternative_path
                    alternative_path = None
                else:
                    deleted_idx = 0  # any value rather than -1

                    # must chose to delete p1 or p2
                    alternative_path = p1, p2 - 1
                    p1 += 1
            else:
                p1 += 1
                p2 -= 1

        return True
