class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = {}
        n = len(prices)
        def solve(ind, f):
            if ind == n - 1:
                if f:
                    return prices[ind]
                return 0
            
            if (ind, f) in dp: return dp[(ind, f)]
            if f:
                res = max(solve(ind + 1, f), prices[ind] + solve(ind + 1, 0))
            else:
                res = max(solve(ind + 1, f), -prices[ind] + solve(ind + 1, 1))
            
            dp[(ind, f)] = res
            return res
        return solve(0, 0)


        
