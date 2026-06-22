class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map, we can store this now
        hashmap = {}

        for i in range(len(nums)):
            # Store each value associated with index
            hashmap[nums[i]] = i

            # [3,4,5,6]
            # -> 3: 0, 4: 1, 5: 2, 6: 3
        
        for index, num in enumerate(nums):
            counter = target - num
            if counter in hashmap and hashmap[counter] != index:
                return [index, hashmap[counter]]
        