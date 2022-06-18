class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # loop on s2 with a window size => len(s1)
        # check if all letters of s are in this window
        # if not, move the window one step, remove letter and add letter, check these new letters

        if len(s2) < len(s1):
            return False

        n = len(s1)
        start = 0
        end = n

        s1_count = {}

        for s in s1:
            if s in s1_count:
                s1_count[s] += 1
            else:
                s1_count[s] = 1

        win_size = 0
        win_start = 0

        for i in range(len(s2)):
            if s2[i] in s1_count:
                # add it to the s1_count
                s1_count[s2[i]] -= 1

                if s1_count[s2[i]] == 0:
                    s1_count.pop(s2[i])
            else:
                # in case s2 not in the s1_count, that means it is not a substring anymore, so
                # 1. loop over the window and for each char,
                # 2. increase the freq of each letter
                # 3. mark the start of the window to i+1
                # 4. if s2[i] becomes in the string, then stop looping, and mark the string start idx

                for j in range(win_start, i):
                    if s2[win_start] in s1_count:
                        s1_count[s2[win_start]] += 1
                    else:
                        s1_count[s2[win_start]] = 1

                    win_start += 1

                    if s2[i] in s1_count:
                        break

                if s2[i] in s1_count:
                    # add it to the s1_count
                    s1_count[s2[i]] -= 1

                    if s1_count[s2[i]] == 0:
                        s1_count.pop(s2[i])
                else:
                    win_start+=1
            # in the case of window == len(s1)

            # A. remove one letter from the beginning
            #   1. inc its frequency +1 in the dict
            #   2. if it is not in the dict then add it to the freq
            # B. Add one letter at the end
            #   1. dec the last letter from the dict
            #   2. check if it is 0

            win_size = i - win_start + 1

            if win_size > len(s1):
                if s2[win_start] in s1_count:
                    s1_count[s2[win_start]] += 1
                else:
                    s1_count[s2[win_start]] = 1

            if len(s1_count) == 0:
                return True

        return False

print(Solution().checkInclusion("ccc", "cbac"))
print(Solution().checkInclusion("rvwrk", "gwrvrk"))
print(Solution().checkInclusion("adc", "dcda"))
print(Solution().checkInclusion("ab", "eidboaoo"))
