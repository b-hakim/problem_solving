class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')

        p1 = 0
        p2 = 0

        # v1 = [1, 1, 0]
        # v2 = [1, 1]
        # p1 = 3
        # p2 = 2
        # r_v1 = 0
        # r_v2 =

        while p1 < len(version1):
            # compare with p2
            r_v1 = int(version1[p1])
            p1 += 1

            if p2 < len(version2):
                r_v2 = int(version2[p2])
                p2 += 1
            else:
                r_v2 = 0

            if r_v1 < r_v2:
                return -1
            elif r_v1 > r_v2:
                return 1

        r_v1 = 0

        while p2 < len(version2):
            if int(version2[p2]) > r_v1:
                return -1
            p2 += 1

        return 0

