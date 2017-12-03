#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
@author: MarkLiu
@time  : 17-12-2 下午7:12
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a = len(a)
        len_b = len(b)
        # 对于短的字符串, 按0补全
        while len_a > len_b:
            b = '0' + b
            len_b = len(b)

        while len_a < len_b:
            a = '0' + a
            len_a = len(a)

        # 从最后一位开始按位相加并判断是否进位
        carry = 0
        result = [' '] * len_a
        for i in range(len_a - 1, -1, -1):
            s = int(a[i]) + int(b[i]) + carry
            if s <= 1:
                carry = 0
                result[i] = str(s)
            elif s == 2:
                carry = 1
                result[i] = '0'
            elif s == 3:
                carry = 1
                result[i] = '1'

        if carry == 1:
            result.insert(0, '1')
        return ''.join(result)


print Solution().addBinary('11', '1')
