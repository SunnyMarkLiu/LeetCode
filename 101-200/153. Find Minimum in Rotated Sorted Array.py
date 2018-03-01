#!/home/sunnymarkliu/softwares/anaconda3/bin/python
# _*_ coding: utf-8 _*_

"""
@author: SunnyMarkLiu
@time  : 18-3-1 上午10:22
"""


class Solution(object):
    def findMin(self, nums):
        """
        0　　1　　2　　 *4　　5　　6　　7*
        7　　0　　1　　 *2　　4　　5　　6*
        6　　7　　0　　 *1　　2　　4　　5*
        5　　6　　7　　 *0　　1　　2　　4*
        *4　　5　　6　　 7* 　0　　1　　2
        *2　　4　　5　　 6*　　7　　0　　1
        *1　　2　　4　　 5*　　6　　7　　0

        二分搜索法的关键在于获得了中间数后，判断下面要搜索左半段还是右半段
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        low, high = 0, len(nums) - 1
        while low < high - 1:
            # 对于一个区间A，如果A[start] < A[stop]，那么该区间一定是有序的，直接返回最低位的值
            if nums[low] < nums[high]:
                return nums[low]

            mid = (low + high) // 2

            if nums[mid] < nums[low]:  # 最小值在左半段
                high = mid
            else:  # 最小值在右半段
                low = mid

        return min(nums[low], nums[high])
