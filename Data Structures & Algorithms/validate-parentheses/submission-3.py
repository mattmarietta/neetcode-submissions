class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        # Add opening brackets to our stack until we get to a closing one
        valid_dict = {"}" : "{", ")" : "(", "]" : "["}

        for char in s:
            #Case for opening brackets because we check if stack has anything
            if char in valid_dict:
                if stack and stack[-1] == valid_dict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False


