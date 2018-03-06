#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-6 下午2:46
"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        空间换时间，每次操作爆炸　O(1)，考虑使用　HashMap 记录状态

        [3, 4, 200, 1, 5, 2]

        :type nums: List[int]
        :rtype: int
        """
        # 记录每个数字相邻数的个数
        neighbors = {}
        # 初始化每个数出现一次，注意数字可能重复
        for num in nums:
            neighbors[num] = neighbors.get(num, 1)

        max_count = 0
        for num in nums:
            # 对 num 查找时，先确定num是否存在
            if num not in neighbors:
                continue

            # 向上查找
            count = 1  # 初始化只有一个当前元素
            target = num + 1  # 待查找的目标
            while target in neighbors:  # 向上如果找到
                # 注意如果找到了上一个目标，则这个目标下次可以不用再找了
                neighbors.pop(target)
                target += 1
                count += 1

            # 向下查找
            target = num - 1
            while target in neighbors:
                neighbors.pop(target)
                target -= 1
                count += 1

            # num 查找结束，注意此处也删除 num
            neighbors.pop(num)
            max_count = max(max_count, count)

        return max_count
