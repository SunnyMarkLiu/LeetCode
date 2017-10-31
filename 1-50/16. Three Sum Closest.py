#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
(1) 数组排序
(2) 遍历排序后的数组第一个数到倒数第三个数, 假设为 a (下标为 i), 剩余的两个值一个比a小，在a的左边数组中，一个比a大，在a的右边数组中。
    (3) 左边的数 l 从 i 的下一个数开始, 右边的数 r 从最后一个数开始, 遍历, 并求和 s = i + l + r
        (4) 如果 s == target, 直接返回该 s
        (5) 如果 s < target 左边的值太小,需要右动
        (6) 如果 s > target 右边的值太大,需要左动
        (7) 注意保留 closest tmp

@author: MarkLiu
@time  : 17-10-31 下午7:37
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return None

        closest_sum = float("inf")
        nums.sort()
        for i in xrange(len(nums) - 2):
            l_index, r_index = i + 1, len(nums) - 1
            while l_index < r_index:
                s = nums[i] + nums[l_index] + nums[r_index]
                if s == target:
                    return s
                elif s < target:  # 左边的值太小,需要右动
                    l_index += 1
                elif s > target:
                    r_index -= 1

                if abs(target - s) < abs(target - closest_sum):
                    closest_sum = s
        return closest_sum


print Solution().threeSumClosest([-1, 2, 1, -4], 2)
