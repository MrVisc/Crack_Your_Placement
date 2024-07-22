class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        c = 1
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] == nums[i - 1]:
                c += 1
            else:
                if c > n//2:
                    return nums[i - 1]
                c = 1
        return nums[-1]
