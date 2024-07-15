class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in nums:
            ind = abs(i)
            if nums[ind] < 0: return ind
            nums[ind] = -nums[ind]