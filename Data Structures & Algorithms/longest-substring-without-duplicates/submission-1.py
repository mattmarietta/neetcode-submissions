class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characterset = set()
        l = 0
        res = 0

        # Sliding window with our right pointer in a for loop
        for r in range(len(s)):
            # If it is in our set then we have a duplicate and remove it
            while s[r] in characterset:
                characterset.remove(s[l])
                l += 1
            # If it isnt then we can add it
            characterset.add(s[r])
            res = max(res, r - l + 1)
        return res