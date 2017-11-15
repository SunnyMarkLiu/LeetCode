#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
1. 负数不是回文数
2. 对于正数,将数字反转, 在判断和原数是否相等

@author: MarkLiu
@time  : 17-11-15 下午8:07
"""


class Solution(object):
    def reverse(self, x):
        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x /= 10
        return result

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:   # 负数不是回文数
            return False
        return self.reverse(x) == x


print Solution().isPalindrome(-2147447412)
