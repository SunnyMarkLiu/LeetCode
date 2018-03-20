#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-20 上午10:51
"""


class Solution:

    def __init__(self):
        self.pstart = 0  # 最长回文的开始下标
        self.max_plen = 0  # 最大回文的长度

    def longestPalindrome(self, s):
        """
        方法一：中心扩展法。遍历字符串的每一个字符，如果存在回文子串，那么中心是某一个字符（奇数）或两个字符的空隙（偶数），
        然后分两种情况（奇数或偶数）向两边扩展。
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s

        for i in range(len(s)):  # 以每个字符为中心
            # 如果回文是奇数
            self.check_palindrome(s, i, i)
            # 如果回文是偶数
            self.check_palindrome(s, i, i + 1)

        return s[self.pstart: self.pstart + self.max_plen]

    def check_palindrome(self, s, start, end):
        """ start 向左移动，end向右移动"""
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1

        # 计算此时的回文的长度
        cur_plen = end - start - 1
        if cur_plen > self.max_plen:
            self.max_plen = cur_plen
            self.pstart = start + 1
