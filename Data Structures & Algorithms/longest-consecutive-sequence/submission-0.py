class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Make a set of the numbers
        numset = set(nums)
        # Store the overall maximum number to return (sequence of nmbers)
        overallMax = 0

        # Loop through the numbers and get to a valid starting point 
        for num in nums:
            # Starting point check: we want number to start at the minimum
            if num - 1 in numset:
                continue
            
            # Set a new variable to current number
            currNumber = num
            # If that number is in our set, then go through and iterated on how long that is
            # currNumber - num shows us how far our length is, for ex: start at 2, end at 6 then 6 - 2 = 4 length
            while currNumber in numset:
                currNumber += 1
            overallMax = max(overallMax, currNumber - num)
        return overallMax
                
            