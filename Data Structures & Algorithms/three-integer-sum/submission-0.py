class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 2 pointers and check through a for loop if -i is equal to j + k?
        res = []
        # we will sort the array so it can be least to greatest
        nums.sort()

        for i, a in enumerate(nums):
            # Skip the number if a is equal to the one before to avoid dupes
            if i > 0 and a == nums[i - 1]:
                continue
            
            # Now we can compare our l, r to the number of a
            l = i + 1 
            r = len(nums) - 1
            while l < r:
                #Check the number at each index and set it to 3sum
                threesumaru = a + nums[l] + nums[r]
                #If it is greater than 0 that tells us
                if threesumaru > 0:
                    r -= 1
                elif threesumaru < 0:
                    l += 1
                #We know its equal to 0 so we append our indices
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
            