class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #loop through the array and multiply every other
        #position except itself

        # Prefix and Postfix 

        # Define results array
        results = [1] * (len(nums))
        # Prefix starts at 1 for index 0
        prefix = 1
        for i in range(len(nums)):
            # Store each result with the prefix as we move then update prefix
            results[i] = prefix
            prefix *= nums[i]
        # Intialize the backward postfix
        postfix = 1
        for j in range((len(nums) - 1), -1, -1):
            results[j] *= postfix
            postfix *= nums[j]
        return results

