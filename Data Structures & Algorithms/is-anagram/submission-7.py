class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Ideas: 
        # Use a hashmap to count how many times each letter show up
        s_hash, t_hash = {}, {}
        if len(s) != len(t):
            return False

        '''
        for i in range(len(s)):
            sorteds = sorted(s)
            sortedt = sorted(t)
            sorted_strings = "".join(sorteds)
            sorted_stringt = "".join(sortedt)
        
        return sorted_strings == sorted_stringt
            '''

        for i in range(len(s)):
            #For each list compare the letter to each, if they dont match then we know its not an anagram
            #Return default value 0 if not found and add 1 if we have a instance
            s_hash[s[i]] = 1 + s_hash.get(s[i], 1)
            t_hash[t[i]] = 1 + t_hash.get(t[i], 1)
        return t_hash == s_hash
            


        
        
        