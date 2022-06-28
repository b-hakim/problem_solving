class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        number = 0
        num_started = False
        max_signed_int = pow(2, 31) - 1
        min_signed_int = pow(2, 31) * -1

        for i in range(len(s)):
            if s[i] == " " and not num_started:
                continue
            elif s[i] == " ":
                break

            if s[i] == "+" and not num_started:
                sign = 1
                num_started = True
                continue
            elif s[i] == "-" and not num_started:
                sign = -1
                num_started = True
                continue
            elif s[i] == "-" and num_started:
                break

            if '0' > s[i] or s[i] > '9':
                break

            num_started = True

            if number == 0:
                number += int(s[i])
            else:
                number *= 10
                number += int(s[i])

            if number * sign > max_signed_int:
                return max_signed_int
            if number * sign < min_signed_int:
                return min_signed_int

        return number * sign