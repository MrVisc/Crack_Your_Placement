class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        res = 0
        while start < end:
            mini = min(height[start], height[end])
            temp = mini * (end - start)
            if temp > res:
                res = temp
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return res
