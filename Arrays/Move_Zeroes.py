class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(len(nums)):
            if nums[k] == 0:
                nums.append(nums[k])
                nums.pop(k)
                k -= 1
            k += 1
