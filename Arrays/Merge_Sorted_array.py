class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = []
        p1 = 0
        p2 = 0
        while p1 < m and p2 < n:
            if nums1[p1] <= nums2[p2]:
                temp.append(nums1[p1])
                p1 += 1
            else:
                temp.append(nums2[p2])
                p2 += 1
        if p1 == m:
            for i in range(p2, n):
                temp.append(nums2[i])
        elif p2 == n:
            for i in range(p1, m):
                temp.append(nums1[i])
        for i in range(m + n):
            nums1[i] = temp[i]
