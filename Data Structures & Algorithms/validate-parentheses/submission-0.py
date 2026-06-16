class Solution:
    def isValid(self, s: str) -> bool:
        #Use a stack and a dictionary to store the parentheses
        parenth_dict = {')': '(', ']' : '[', '}': '{'}
        stack = []

        #Stack should be empty when we finish if it is opened and closed correctly
        for c in s:
            if c in parenth_dict:
                if stack and stack[-1] == parenth_dict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if not stack:
            return True
        else:
            return False
                