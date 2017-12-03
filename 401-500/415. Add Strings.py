#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
@author: MarkLiu
@time  : 17-12-3 下午3:52
"""


class Solution(object):
    def addStrings2(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len_1 = len(num1)
        len_2 = len(num2)
        # 对于短的字符串, 按0补全
        while len_1 > len_2:
            num2 = '0' + num2
            len_2 = len(num2)

        while len_1 < len_2:
            num1 = '0' + num1
            len_1 = len(num1)

        # 从最后一位开始按位相加并判断是否进位
        carry = 0
        result = [' '] * len_1
        for i in range(len_1 - 1, -1, -1):
            s = int(num1[i]) + int(num2[i]) + carry
            if s <= 9:
                carry = 0
                result[i] = str(s)
            else:
                carry = s / 10
                result[i] = str(s % 10)

        if carry > 0:
            result.insert(0, str(carry))

        return ''.join(result)

    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) == 0:
            return num2
        if len(num2) == 0:
            return num1

        s = int(num1[-1]) + int(num2[-1])
        if s >= 10:
            return self.addStrings(self.addStrings(num1[:-1], num2[:-1]), str(s / 10)) + str(s % 10)
        else:
            return self.addStrings(num1[:-1], num2[:-1]) + str(s)


print Solution().addStrings('99', '9')
