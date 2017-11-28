#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
类似于时间窗(长度为待匹配的 needle 的长度)滑动的方式进行匹配
@author: MarkLiu
@time  : 17-11-28 下午8:37
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_needle = len(needle)
        len_haystack = len(haystack)

        if len_needle > len_haystack:
            return -1

        for i in range(len_haystack - len_needle + 1):
            if haystack[i:i + len_needle] == needle:
                return i

        return -1
