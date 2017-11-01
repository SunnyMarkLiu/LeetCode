#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
四个数求和, 分出两部分, AB求和存入字典, CD求和取相反数, 再检查 AB求和的字典

@author: MarkLiu
@time  : 17-11-1 下午9:33
"""


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ab_sum_dict = {}
        for a in A:
            for b in B:
                if a + b not in ab_sum_dict:
                    ab_sum_dict[a + b] = 0
                ab_sum_dict[a + b] += 1

        result = 0
        for c in C:
            for d in D:
                if -c - d in ab_sum_dict:
                    result += ab_sum_dict[-c - d]

        return result

print Solution().fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2])
