#!/home/sunnymarkliu/software/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
给定一个数组nums，编写函数将数组内所有0元素移至数组末尾，并保持非0元素相对顺序不变。
例如，给定nums = [0, 1, 0, 3, 12]，调用函数完毕后， nums应该是 [1, 3, 12, 0, 0]。

注意：

- 应该“就地”完成此操作，不要复制数组。(in-place)
- 最小化操作总数。

@author: MarkLiu
@time  : 17-11-19 下午5:25
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        beat 75.70%
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1

        while i < len(nums):
            nums[i] = 0
            i += 1

nums_ = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums_)
print nums_
