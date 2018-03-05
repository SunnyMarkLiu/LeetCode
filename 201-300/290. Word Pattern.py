#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-5 下午9:49
"""


class Solution(object):
    def wordPattern(self, pattern, check_str):
        """
        :type pattern: str
        :type check_str: str
        :rtype: bool
        """
        check_str = check_str.split(' ')

        if len(pattern) != len(check_str):
            return False

        check_p = ''
        check = {}
        for i in range(len(pattern)):
            if pattern[i] not in check:
                check[pattern[i]] = i
                check_p += str(i)
            else:
                check_p += str(check.get(pattern[i]))

        check_s = ''
        check = {}
        for i in range(len(check_str)):
            if check_str[i] not in check:
                check[check_str[i]] = i
                check_s += str(i)
            else:
                check_s += str(check.get(check_str[i]))

        return check_s == check_p
