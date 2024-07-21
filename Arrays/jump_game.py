class Solution:
    def canJump(self, nums: List[int]) -> bool:
        val = 0
        n = len(nums)

        for i in range(n - 1):
            if val == 0 and nums[i] == 0:
                return 
            
            val = max(val, nums[i])
            val -= 1

        return 1
