#!/usr/local/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
1）将数组排序。
2）对数组中每一个元素，假设其值为 a，则问题可化为在剩余的数组中（除了当前元素）找 target 为 -a 的TwoSum问题。
3）由于数组是有序的，剩余的两个值一个比a小，在a的左边数组中，一个比a大，在a的右边数组中。
4）指定数组中最小的数（即最左边的数）为第一个数 low ，指定数组中最大的数为第二个数 high。
5）比较这两个数的和 sum 跟 target 的大小，如果 sum < target，表明 low 位置的值太小，则 low位置的数要往前移（low++），如果sum > target，则 high 位置的值太大，high往后移（high--），在移动过程，判断是否达到a所在的位置，如果忆经达a所在的位置，还没有找到，则说明，不存在这样的组合。
6）如果存在这样的组合，判断是否存在这样的组合，如果不存在这样的组合，则将其添加进结果列表中，如果存在，则舍弃它。
7）对于同样的值 a ，剩余数组中可能存在不只一对元素的和等于 -a，所以不像TwoSum问题直接退出，要继续向前移动 low 和向后移动 high，找出同样满足条件的数值对。
8）由于数组中有可能存在重复的数，在排序后的数组中，它们是连在一起的，那么当找到第一对数值对的时候，继续找的时候，要判断下一个位置的数是否跟当前位置的置相同，如果相同，可忽略，因为这个值同样满足条件，但是其会造成重复的组合。

@author: MarkLiu
@time  : 17-9-25 下午8:59
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        solutions = []
        nums.sort()  # 注意先排序
        for i in xrange(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # 去除重复数据
                continue

            l_index, r_index = i + 1, len(nums) - 1
            while l_index < r_index:
                s = nums[i] + nums[l_index] + nums[r_index]
                if s < 0:
                    l_index += 1
                elif s > 0:
                    r_index -= 1
                else:
                    solutions.append((nums[i], nums[l_index], nums[r_index]))
                    while l_index < r_index and nums[l_index] == nums[l_index + 1]:  # 去除重复数据
                        l_index += 1
                    while l_index < r_index and nums[r_index] == nums[r_index - 1]:
                        r_index -= 1

                    l_index += 1
                    r_index -= 1

        return solutions


print Solution().threeSum([-1, 0, 1, 2, -1, -4])
