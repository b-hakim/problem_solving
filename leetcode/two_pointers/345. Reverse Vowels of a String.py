class Solution:
    def reverseVowels(self, s: str) -> str:
        p1, p2 = 0, len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', "O", "U"]
        s = list(s)

        while p1 < p2:
            if s[p1] in vowels and s[p2] in vowels:
                s[p1], s[p2] = s[p2], s[p1]
                p1 += 1
                p2 -= 1
            elif s[p1] in vowels:
                p2 -= 1
            elif s[p2] in vowels:
                p1 += 1
            else:
                p1 += 1
                p2 -= 1

        return "".join(s)