# encoding: utf-8

"""
@author: Shelly An
@contact: 81247054@qq.com
@software: PyCharm
@file: 整数反转.py
@time: 2019/1/25 9:13
"""
'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21

注意:
如果反转后整数溢出那么就返回 0。
'''


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_reverse = 0

        for i in range(len(str(abs(x)))):
            x_reverse += int(str(abs(x))[i]) * (10 ** i)

        if x < 0:
            x_reverse = - x_reverse

        if x >= (-2) ** 31 and x <= (2 ** 31) - 1:
            return x_reverse
        else:
            return 0
