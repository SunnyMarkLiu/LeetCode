#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
如果是power of two, 则2进制表达中,有且仅有一个1.  可以通过移位来数1的个数, 这里用了一个巧妙的办法,
即判断   N & (N-1) 是否为0.

n&(n-1)作用：将n的二进制表示中的最低位为1的改为0，先看一个简单的例子：
n = 10100(二进制），则(n-1) = 10011 ==》n&(n-1) = 10000

@author: MarkLiu
@time  : 17-12-6 下午8:00
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n > 0) & ((n & (n - 1)) == 0)
