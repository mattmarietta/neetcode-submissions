class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Hashmap? Set?
        # Lets make a set first
        seen = set()
        # Add what we have seen to the set, if its already in there then we return true
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
                print(f"This is seen set {seen}")
            seen.add(nums[i])
        return False

