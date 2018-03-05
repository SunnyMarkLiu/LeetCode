#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-5 下午9:49
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return True

        if len(s) != len(t):
            return False

        # 依次添加字符到 set 中，若存在记录１不存在记录０，最后比较两次记录的序列是否相等
        check_s = self.check_is_contain(s)
        check_t = self.check_is_contain(t)

        return check_s == check_t

    def check_is_contain(self, s):
        check_res = ''
        n = len(s)

        check = {}
        for i in range(n):
            if s[i] not in check:
                check[s[i]] = i
                check_res += str(i)
            else:
                check_res += str(check.get(s[i]))

        return check_res
