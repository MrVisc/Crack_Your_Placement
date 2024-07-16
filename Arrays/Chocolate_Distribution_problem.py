class Solution:

    def findMinDiff(self, A,N,M):
        p1 = 0
        p2 = M
        
        res = float('inf')
        A.sort()
        
        for p1 in range(N - M + 1):
            res = min(res, A[p1 + M - 1] - A[p1])
        return res
