#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
@author: MarkLiu
@time  : 17-11-5 下午12:55
"""
import collections


class Solution(object):
    def findTheDifference2(self, s, t):
        """
        beats 7.31%
        :type s: str
        :type t: str
        :rtype: str
        """
        return [i for i in t if i not in s or s.count(i) != t.count(i)][0]

    def findTheDifference3(self, s, t):
        """
        beats 16.18%
        :type s: str
        :type t: str
        :rtype: str
        """
        s_count = collections.Counter(s)
        st_count = collections.Counter(s + t)

        for key in st_count.iterkeys():
            if st_count[key] > 2 * s_count[key]:
                return key
        return None

    def findTheDifference(self, s, t):
        """
        beats 27.42%
        :type s: str
        :type t: str
        :rtype: str
        """
        s_count = collections.Counter(s)
        t_count = collections.Counter(t)
        return (t_count - s_count).keys()[0]


print Solution().findTheDifference('abcd', 'abcdt')
