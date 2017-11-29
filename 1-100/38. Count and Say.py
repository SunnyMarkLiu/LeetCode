#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
@author: MarkLiu
@time  : 17-11-29 下午9:39
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'

        str_ = self.countAndSay(n - 1)
        count = 1
        s = ''
        for i, c in enumerate(str_):
            if i < len(str_) - 1 and str_[i+1] == c:
                count += 1
            else:   # 开始出现不同的字符
                s = s + str(count) + c
                count = 1
        return s

print Solution().countAndSay(3)
