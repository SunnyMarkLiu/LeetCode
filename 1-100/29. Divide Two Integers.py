#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-20 下午3:14
"""
import sys


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return sys.maxsize

        # 除数和被除数是否同号
        plus = 1
        if dividend * divisor < 0:
            plus = -1

        dividend = abs(dividend)
        divisor = abs(divisor)

        print(dividend, divisor)
        result = 0
        count = 0
        while result <= dividend:
            result += divisor
            if result <= dividend:
                count += 1

        return count * plus
