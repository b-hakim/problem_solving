class Solution:
    def isHappy(self, n: int) -> bool:
        p1, p2 = n, n

        # 2 > 4 > 16 > 1+36 = 37 > 9 + 49 > 58 > 25+64=89 > 64+81 = 145 > 1 + 16 + 25 = > 42 > 8+4 > 12
        # >5 > 25 > 29 > 85 > 64 + 25 = 89 > cycle!
        def sqs(n):
            s = 0

            while n != 0:
                i = n % 10
                s += i * i
                n //= 10

            return s

        while p2 != 1:
            p1 = sqs(p1)
            p2 = sqs(sqs(p2))

            if p1 == p2:
                break

        return p2 == 1
