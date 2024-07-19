class Solution:
    def maxScore(self, arr: List[int], k: int) -> int:
        n = len(arr)
        k = n - k

        pre = []
        s = 0
        for i in arr:
            s += i
            pre.append(s)

        print(n, k, pre)
        maxi = pre[k - 1]

        for i in range(1, n - k + 1):
            print(i, i + k - 1, i - 1)
            maxi = min(maxi, pre[i + k - 1] - pre[i - 1])

        return sum(arr) - maxi

        
        
