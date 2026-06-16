class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #append both to a new list or string and then check them

        if len(s) != len(t):
            return False
        if sorted(s) == sorted(t):
            return True
        return False
        
        
        