#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-1-6 下午9:52
"""


class Solution(object):
    def rotate2(self, nums, k):
        """
        Time Limit Exceeded
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for i in range(k):
            tmp = nums[-1]
            nums[1:] = nums[:-1]
            nums[0] = tmp

    def rotate(self, nums, k):
        """
        Time Limit Exceeded
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[n - k:] + nums[:n - k]


n = [1, 2, 3, 4, 5, 6, 7]
Solution().rotate(n, 3)
print(n)
