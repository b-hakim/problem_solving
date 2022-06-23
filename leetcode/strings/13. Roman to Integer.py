class Solution:
    def romanToInt(self, s: str) -> int:
        # for each X add 10
        # for each V add 5
        # for each I add 1
        def get_val(c):
            if c == "I":
                return 1
            if c == "V":
                return 5
            if c == "X":
                return 10
            if c == "L":
                return 50
            if c == "C":
                return 100
            if c == "D":
                return 500
            if c == "M":
                return 1000

        n = len(s) - 1
        number = 0
        # cases:
        # IV ==> 4
        # IX ==> 9
        # XL ==> 40
        # XC ==> 90
        # CD ==> 400
        # CM ==> 900

        i = 0
        while i <= n:
            if i == n:
                number += get_val(s[i])
            else:
                if s[i] == "I":
                    if s[i + 1] == "V":
                        number += 4
                        i += 1
                    elif s[i + 1] == "X":
                        number += 9
                        i += 1
                    else:
                        number += 1
                elif s[i] == "V":
                    number += 5
                elif s[i] == "X":
                    if s[i + 1] == "L":
                        number += 40
                        i += 1
                    elif s[i + 1] == "C":
                        number += 90
                        i += 1
                    else:
                        number += 10
                elif s[i] == "L":
                    number += 50
                elif s[i] == "C":
                    if s[i + 1] == "D":
                        number += 400
                        i += 1
                    elif s[i + 1] == "M":
                        number += 900
                        i += 1
                    else:
                        number += 100
                elif s[i] == "D":
                    number += 500
                elif s[i] == "M":
                    number += 1000
            i += 1

        return number


