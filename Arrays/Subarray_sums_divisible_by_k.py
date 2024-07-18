from itertools import accumulate

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ctr = [0]*k
        for mod in accumulate(nums, initial=0):
            ctr[mod%k]+=1

        ans = 0
        for freq in ctr:
            ans += freq*(freq-1)//2
        return ans
