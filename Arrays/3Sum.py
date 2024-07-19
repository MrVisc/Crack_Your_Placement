class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sl = sorted(nums)
        n = len(nums)
        result = []
        prev = ''
        prev_i = None
        for i in range(n - 2):
            if sl[i] > 0:
                break
            if not prev_i == sl[i]: 
                p1 = i + 1
                p2 = n - 1
                while p1 < p2:
                    if sl[i] + sl[p1] + sl[p2] == 0 and not prev == str(sl[i]) + str(sl[p1]) + str(sl[p2]):
                        result.append([ sl[i], sl[p1], sl[p2] ])
                        prev = str(sl[i]) + str(sl[p1]) + str(sl[p2])
                        p1 += 1
                        p2 -= 1
                    elif sl[i] + sl[p1] + sl[p2] < 0:
                        p1 += 1
                    else:
                        p2 -= 1
                    if p1 == p2:
                        break
                prev_i = sl[i]
        return result
