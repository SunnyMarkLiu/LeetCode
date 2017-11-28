#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
@author: MarkLiu
@time  : 17-11-28 下午9:20
"""


class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        # 粗粒度判断重复次数为 B 的长度除以 A 的长度向上取整
        times = -(-len(B) // len(A))    # // 操作实现向下取整, 利用负数相除的技巧实现 ceil
        # 细粒度判断 times 还是 times + 1
        for i in range(2):
            if B in (A * (times + i)):
                return times + i
        return -1

print Solution().repeatedStringMatch('abababaaba', 'aabaaba')
