# encoding: utf-8

"""
@author: Shelly An
@contact: 81247054@qq.com
@software: PyCharm
@file: 两数之和.py
@time: 2019/1/23 18:06
"""

'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

import datetime

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None


# test
t = Solution()
begin = datetime.datetime.now()
print(t.twoSum([2, 7, 11, 15], 9))
end = datetime.datetime.now()
print('运行时间：', end-begin)