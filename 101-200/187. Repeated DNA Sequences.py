#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-5 下午9:06
"""


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if s is None or len(s) < 10:
            return []

        result = set()
        tmp_check = set()
        for i in range(len(s) - 10 + 1):
            sub_str = s[i: i + 10]
            # 不存在重复值
            if sub_str not in tmp_check:
                tmp_check.add(sub_str)
            else:
                result.add(sub_str)

        return list(result)
