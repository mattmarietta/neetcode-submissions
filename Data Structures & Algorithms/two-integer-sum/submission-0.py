class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force: Loop through 2 arrays, return i  + j


        # [ 3, 4, 5, 6]   target = 7
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


