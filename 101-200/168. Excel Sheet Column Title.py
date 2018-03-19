#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-19 上午10:25
"""


class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if not isinstance(n, int) or n < 1:
            return None

        result = ''
        while n > 0:
            n -= 1  # 此处减一，方便后续的偏移量操作
            result = chr(ord('A') + n % 26) + result
            n = n // 26

        return result
