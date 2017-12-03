#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
@author: MarkLiu
@time  : 17-12-2 下午7:12
"""


class Solution(object):
    def addBinary2(self, a, b):
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
            else:
                carry = 1
                result[i] = str(s % 2)

        if carry == 1:
            result.insert(0, '1')
        return ''.join(result)

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a
        if a[-1] == '1' and b[-1] == '1':
            # 此处的 '1' 表示进位
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'
        elif a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        else:  # a=1, b=0; a=0, b=1
            return self.addBinary(a[:-1], b[:-1]) + '1'


print Solution().addBinary('11', '1')
