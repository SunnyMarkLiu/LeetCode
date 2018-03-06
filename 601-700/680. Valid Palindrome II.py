#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-6 上午10:23
"""


class Solution(object):

    def isPalindrome(self, s, l, r):
        """
        :type s: str
        :rtype: bool
        """
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 2:
            return True

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                # 可能删除左边的，也可能删除右边的
                return self.isPalindrome(s, l + 1, r) or self.isPalindrome(s, l, r - 1)
            l += 1
            r -= 1

        return True
