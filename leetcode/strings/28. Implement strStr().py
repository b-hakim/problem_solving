class Solution:
    def isValid(self, s: str) -> bool:
        # loop on all letters in s
        # push it if it is an open bracket
        # otherwise, pop and match with top of the stack

        stack = []
        brackets = {"(", "[", "{"}

        for c in s:
            if c in brackets:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                a = stack.pop()
                if a == "(" and c != ")" or a == "[" and c != "]" or a == "{" and c != "}":
                    return False

        if len(stack) != 0:
            return False

        return True



