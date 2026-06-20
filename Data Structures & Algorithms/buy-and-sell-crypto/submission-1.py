class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left and right pointer
        # Left is buy day and right is sell day
        left = 0
        right = 1

        #Keep track of profit?
        maxProfit = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                maxProfit = max(maxProfit, prices[right] - prices[left])
            else:
                left = right
            right += 1
        
        return maxProfit
            
                 