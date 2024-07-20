class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = []
        c = 0

        for i in nums:
            c += i
            pre.append(c)

        res = 0
        d = {}

        for i in pre:
            if k == i:
                res += 1
            
            if i - k in d:
                res += d[i - k]
            
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        return res
