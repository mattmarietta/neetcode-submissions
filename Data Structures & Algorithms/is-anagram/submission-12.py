class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s) == sorted(t)
        if len(s) != len(t):
            return False

        # Now use a hashmap to solve the anagram
        # Make 2 hashmaps and compare them if they are equal
        # occurences of word, so for 2 ts i would need to add a counter + get
        wordS, wordT = {}, {}
        for char in range(len(s)):
            # Add an occurence to that letter, if it doesnt exist then def value 0
            wordS[s[char]] = 1 + wordS.get(s[char], 0)
            wordT[t[char]] = 1 + wordT.get(t[char], 0)
        if wordS == wordT:
            return True
        return False



