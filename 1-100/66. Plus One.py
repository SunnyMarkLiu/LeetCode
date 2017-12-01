#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
@author: MarkLiu
@time  : 17-12-1 下午4:14
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # 当前需要加的一位等于 9, 加1进位, 直到出现不进位
            digits[i] = 0

        # 极端情况, 进位到最高位, 最高位设置为 1
        digits.insert(0, 1)
        return digits


print Solution().plusOne([9, 9, 9])
