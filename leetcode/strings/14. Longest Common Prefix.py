class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # loop on first's word letters
        # loop on all the words
        # keep track of the common letters
        common = []
        found = True

        for letter in range(len(strs[0])):
            for words_idx in range(1, len(strs)):
                if letter == len(strs[words_idx]) or strs[0][letter] != strs[words_idx][letter]:
                    found = False
                    break
            if found:
                common.append(strs[0][letter])
            else:
                break

        return "".join(common)