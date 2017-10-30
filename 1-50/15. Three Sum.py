#!/usr/local/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
(1) 数组排序
(2) 遍历排序后的数组第一个数到倒数第三个数, 假设为 a (下标为 i), 剩余的两个值一个比a小，在a的左边数组中，一个比a大，在a的右边数组中。
    (3) 左边的数 l 从 i 的下一个数开始, 右边的数 r 从最后一个数开始, 遍历, 并求和 s = i + l + r
        (4) 如果 s = 0, 记录该 solution
        (5) 如果 s < 0, 表明 l 位置的值太小，则 l 位置的数要往右移, l++
        (6) 如果 s > 0, 表明 r 位置的值太大，则 r 位置的数要往左移, r--
        (7) 注意判断避免重复值

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
