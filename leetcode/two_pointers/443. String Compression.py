class Solution:
    def compress(self, chars: List[str]) -> int:
        # ["a","b","b"]
        # p=1
        # write_ptr = 0
        # group_start = 0
        if len(chars) == 1:
            return 1

        p = 1
        group_start = 0
        ret_s = ""

        while p <= len(chars):
            if len(chars) != p and chars[p - 1] == chars[p]:
                p += 1
            else:
                group_len = p - group_start  # 1

                if group_len == 1:
                    ret_s += chars[group_start]  # "a"
                else:
                    ret_s += chars[group_start] + str(group_len)

                group_start = p
                p += 1

        for i, c in enumerate(ret_s):
            chars[i] = c

        return len(ret_s)