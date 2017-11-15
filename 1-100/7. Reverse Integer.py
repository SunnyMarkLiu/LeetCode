#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
思路1: 循环通过对10取模得到尾部数字，一步步乘10构造新的翻转后的整数即可。然而要注意首先判断结果是否溢出，最后还要判断原数字的正负进行调整。
思路2: 将数字转成字符串, 利用字符串的反转操作实现

@author: MarkLiu
@time  : 17-11-15 下午6:58
"""


class Solution(object):
    def reverse2(self, x):
        """
        beat 78.62%
        :type x: int
        :rtype: int
        """
        result = 0
        is_neg = False
        if x < 0:
            is_neg = True
            x *= -1

        while x > 0:
            result = result * 10 + x % 10
            x /= 10

        result = 0 if result > 2 ** 31 else result  # 判断是否溢出
        if is_neg:
            result *= -1
        return result

    def reverse(self, x):
        """
        beat 44.74%
        :type x: int
        :rtype: int
        """
        is_neg = False
        if x < 0:
            is_neg = True
            x *= -1

        result = int(str(x)[::-1])
        result = 0 if result > 2 ** 31 else result  # 判断是否溢出
        if is_neg:
            result *= -1

        return result


print Solution().reverse(-123)
print Solution().reverse2(-2147483648)
