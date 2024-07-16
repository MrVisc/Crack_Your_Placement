class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        i = 0
        while 1:
            if nums[i] in d: return [i, d[nums[i]]]
            d[target - nums[i]] = i
            i += 1
