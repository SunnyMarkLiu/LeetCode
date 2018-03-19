#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-18 下午3:54
"""


class Solution:

    def getKth(self, A, B, k):
        lenA = len(A)
        lenB = len(B)

        # 保证lena < lenb
        if lenA > lenB:
            return self.getKth(B, A, k)
        if lenA == 0:
            return B[k - 1]
        if k == 1:
            return min(A[0], B[0])

        pa = min(k // 2, lenA)
        pb = k - pa
        if A[pa - 1] <= B[pb - 1]:
            return self.getKth(A[pa:], B, pb)
        else:
            return self.getKth(A, B[pb:], pa)

    def findMedianSortedArrays(self, A, B):
        lenA = len(A);
        lenB = len(B)
        if (lenA + lenB) % 2 == 1:
            return self.getKth(A, B, (lenA + lenB) // 2 + 1)
        else:
            return (self.getKth(A, B, (lenA + lenB) // 2) +
                    self.getKth(A, B, (lenA + lenB) // 2 + 1)) * 0.5
