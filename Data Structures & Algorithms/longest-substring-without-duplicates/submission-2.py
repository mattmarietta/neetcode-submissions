class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        # Initialize a left pointer
        left = 0
        # Initialize results
        res = 0

        # Right pointer inside of for loop
        for r in range(len(s)):
            # Check if we have this within our seen set
            while s[r] in seen:
                # Remove it and increase the left pointer
                seen.remove(s[left])
                left += 1
            # Add it to set at the end no matter what
            seen.add(s[r])
            # Make results equal to itself or the length of the word currently
            res = max(res, len(seen))
        return res