#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
3 的幂特点: x / y == 0,  x 是 3 的幂, 则 y 一定是 3 的幂
任何一个3的x次方一定能被int型里最大的3的x次方整除

1. 求出 int 最大的 3 的幂 max_int_3
2. 判断 max_int_3 是否被 n 整除

@author: MarkLiu
@time  : 17-12-6 下午8:32
"""
import math


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        # 求出 int 最大的 3 的幂 max_int_3, 先求出 log3(maxint) 的整数, 再 3 次方
        max_int = 0x7fffffff
        k = int(math.log10(max_int) / math.log10(3))
        max_int_3 = math.pow(3, k)

        return max_int_3 % n == 0

print Solution().isPowerOfThree(3)
