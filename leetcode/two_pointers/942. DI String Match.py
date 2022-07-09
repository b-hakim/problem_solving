class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        """
        DDD ==> 3210
        IDD ==> 0321

        D=0

        if I add from 0 if D add from N
        IDID
        N_high=2
        N_low =2
        0,4,1,3
        """

        low, high = 0, len(s)
        ret = []

        for c in s:
            if c == "I":
                ret.append(low)
                low += 1
            else:
                ret.append(high)
                high -= 1


        ret.append(low)

        return ret
