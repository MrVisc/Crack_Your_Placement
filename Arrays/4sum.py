class Solution:
    def fourSum(self, arr: List[int], t: int) -> List[List[int]]:
        arr.sort()
        res = []
        temp = []
        n = len(arr)

        if n <= 3:
            return []

        for i in range(n - 3):
            temp.append(arr[i])
            for j in range(i + 1, n - 2):
                temp.append(arr[j])
                p1 = j + 1
                p2 = n - 1

                while p1 < p2:
                    s = arr[p1] + arr[p2] + arr[i] + arr[j]
                    if s == t:
                        temp.extend([arr[p1], arr[p2]])
                        res.append(temp.copy())
                        temp.pop()
                        temp.pop()
                        p2 -= 1
                        p1 += 1
                    elif s > t:
                        p2 -= 1
                    else:
                        p1 += 1
                    
                temp.pop()
            temp.pop()

        if res == []:
            return []
        
        res.sort(key = lambda x: (x[0], x[1], x[2]))
        ans = [res[0]]
        for i in range(1, len(res)):
            if res[i - 1] == res[i]: continue

            ans.append(res[i])

        return ans
            
                
