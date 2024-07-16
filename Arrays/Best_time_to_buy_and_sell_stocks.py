class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = max(prices) 
        maxi = 0                
        for price in prices:
            mini = min(mini, price) 
            maxi = max(maxi, price - mini) 
        
        return maxi
