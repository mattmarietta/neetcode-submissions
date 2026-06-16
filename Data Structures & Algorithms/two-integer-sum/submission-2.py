class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #hash
        hasharu = {}
        for i in range(len(nums)):
            # 7 - 3 = 4
            # so if bangaru exists within hashmap then 
            # return the index of nums i and that one
            hasharu[nums[i]] = i
            # 0 : num1, 1: num2
        for index, num in enumerate(nums):
            bangaru = target - num
            # it must be in it and it cant be same index
            if bangaru in hasharu and hasharu[bangaru] != index:
                return [index, hasharu[bangaru]]
        return []