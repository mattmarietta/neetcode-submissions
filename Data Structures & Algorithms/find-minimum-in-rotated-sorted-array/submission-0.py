class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Use binary search to look for it
        left, right = 0, len(nums) - 1

        #what is target??
        target = nums[0]


        while left <= right:

            if nums[left] < nums[right]:
                target = min(target, nums[left])
                break
            mid = left + (right - left) // 2
            target = min(target, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return target
