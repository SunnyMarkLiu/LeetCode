#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-19 上午9:48
"""
import sys


class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        if not list1 or not list2:
            return None

        if len(list1) == 0 or len(list2) == 0:
            return None

        # 将其中一个数组的值和下标映射到 hashmap 中，后续操作是O(1)
        list1_map = {val: index for index, val in enumerate(list1)}

        min_sum = sys.maxsize
        result = []
        for i in range(len(list2)):
            if list2[i] in list1_map:
                s = i + list1_map[list2[i]]
                if s == min_sum:
                    result.append(list2[i])

                if s < min_sum:
                    min_sum = s
                    result.clear()
                    result.append(list2[i])

        return result
