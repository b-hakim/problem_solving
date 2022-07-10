from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            is_pal = True
            for i in range(len(word) // 2):
                if word[i] != word[len(word) - i - 1]:
                    is_pal = False
                    break
            if is_pal:
                return word

        return ""