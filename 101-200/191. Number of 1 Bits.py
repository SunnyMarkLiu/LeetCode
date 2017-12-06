#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
使用n&(n-1)的方法
假使 n =0x110101
            n             n-1            n&(n-1)
step1:   110101          110100          110100
step2:   110100          110011          110000
step3:   110000          101111          100000
step4:   100000          011111          000000
发现有几个1，就循环几次n&(n-1)得到0
时间复杂度：O(M),M是n中1的个数

@author: MarkLiu
@time  : 17-12-6 下午8:13
"""


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n = n & (n - 1)  # 最低位置为 0
            count += 1

        return count
