#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
对于一个非负数n，它的平方根不会大于（n/2+1）, 在[0, n/2+1]这个范围内可以进行二分搜索，求出n的平方根。

@author: MarkLiu
@time  : 17-12-4 上午10:06
"""


class Solution(object):
    def mySqrt2(self, x):
        """
        二分搜索
        :type x: int
        :rtype: int
        """
        i = 0
        j = x / 2 + 1

        while i <= j:
            mid = (i + j) / 2
            if mid * mid == x:
                return mid

            if mid * mid > x:
                j = mid - 1
            else:
                i = mid + 1

        return j

    def mySqrt(self, n):
        """
        牛顿法求解
        ref: http://www.cnblogs.com/AnnieKim/archive/2013/04/18/3028607.html
        x_i+1 = (x_i + n/x_i) / 2
        x_i+1 无线逼近 x_i

        :type x: int
        :rtype: int
        """
        x_i = n
        while x_i * x_i > n:
            x_i = (x_i + n / x_i) / 2

        return x_i
