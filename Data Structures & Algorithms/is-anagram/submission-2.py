class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Ideas: 
        # Use a hashmap to count the frequencies of each letter within each word
        # sort the letters and then compare
        sorted_s = sorted(s)
        sorted_t = sorted(t)\


        if sorted_s == sorted_t:
            return True
        return False
        
        
        