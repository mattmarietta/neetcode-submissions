class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two pointer solution
        # Left = 0 , right = len(numbers) 
        # Go through array, check if numbers[left] + numbers[right] == target
        # If it is less than target, then move left up
        # If it is more, then move right down

        left, right = 0, len(numbers) - 1

        # Condition of left <= right
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            if numbers[left] + numbers[right] < target:
                left += 1
            if numbers[left] + numbers[right] > target:
                right -= 1