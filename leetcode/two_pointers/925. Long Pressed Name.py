class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        p1 = 0
        p2 = 0

        while p1 < len(name):
            if p2 == len(typed):
                return False

            if name[p1] == typed[p2]:
                p1 += 1
                p2 += 1
            else:
                if p1 == 0 or name[p1 - 1] != typed[p2]:
                    return False
                p2 += 1

            # print(p1, p2)

        while p2 != len(typed):
            if name[p1 - 1] != typed[p2]:
                return False

            p2 += 1

        return p2 == len(typed)