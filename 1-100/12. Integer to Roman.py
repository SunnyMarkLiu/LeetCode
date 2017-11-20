#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
例如整数 1437 的罗马数字为 MCDXXXVII， 我们不难发现，千位，百位，十位和个位上的数分别用罗马数字表示了。
所以我们要做的就是用取商法分别提取各个位上的数字，然后分别表示出来：

100 - C
200 - CC
300 - CCC

400 - CD

500 - D
600 - DC
700 - DCC
800 - DCCC

900 - CM

我们可以分为四类，100到300一类，400一类，500到800一类，900最后一类。每一位上的情况都是类似的

@author: MarkLiu
@time  : 17-11-20 上午10:43
"""


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        roman = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        value = [1000, 500, 100, 50, 10, 5, 1]

        for i in range(0, len(value), 2):
            x = num / value[i]
            if x < 4:
                j = 1
                while j <= x:
                    res += roman[i]
                    j += 1
            elif x == 4:
                res = res + roman[i] + roman[i - 1]
            elif (x > 4) and (x < 9):
                res += roman[i - 1]
                j = 6
                while j <= x:
                    res += roman[i]
                    j += 1
            elif x == 9:
                res = res + roman[i] + roman[i - 2]
            num %= value[i]

        return res

print Solution().intToRoman(100)
