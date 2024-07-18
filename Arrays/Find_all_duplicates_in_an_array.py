class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answerList = []

        for i in nums:
            indexValue = abs(i) - 1
            if nums[indexValue] < 0:
                answerList.append(abs(i))
            else:
                nums[indexValue] = - nums[indexValue]


        return answerList

