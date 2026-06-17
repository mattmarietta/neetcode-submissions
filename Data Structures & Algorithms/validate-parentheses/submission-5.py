class Solution:
    def isValid(self, s: str) -> bool:
        parentharu = {')' : '(', ']' : '[', '}' : '{'}
        stack = []
        for c in s:
            if c in parentharu:
                if stack and stack[-1] == parentharu[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False