class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        c = 1
        n = len(nums)
        while c < n:
            if nums[i] == nums[i - 1]:
                nums.pop(i)
                i -= 1
            i += 1
            c += 1
        return len(nums)