#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
需要用一个计数器来记录重复的次数，如果重复次数大于等于2，采用双指针的方式去除数据。
如果不是重复元素了，我们将计数器清零。

@author: SunnyMarkLiu
@time  : 18-2-28 下午2:50
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        去掉至少重复三次的数
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        # 双指针法
        i = 0
        dup_count = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                dup_count = 0  # 重复计数器清 0
            else:  # 出现相等，重复次数计数
                dup_count += 1

            if dup_count <= 1:
                i += 1
                nums[i] = nums[j]

        return i + 1
