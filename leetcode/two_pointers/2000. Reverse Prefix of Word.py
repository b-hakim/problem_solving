class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        j = word.find(ch)
        if j == -1:
            return word
        return word[0:j+1][::-1]+word[j+1:]