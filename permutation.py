# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 19:01:36 2019

@author: 陈彪，版权所有
python递归实现"abcd"字符串全排列。这个问题的处理，主要是使用了回溯法来进行的数据
的全排列。
    针对这样一个全排列的问题的求解，我们的基本思路是，使用最好的方式是递归的方式进
行。分析字典序是怎么进行的，首先是层层递进的方式来进行的。下面是这个问题的题解。
"""

def permute(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        
        out = []
        
        perms = permute(nums[1:])
        for perm in perms:
            for i in range(0, len(perm)+1):
                p = perm[:i] + [nums[0]] + perm[i:]
                out.append(p)
        
        return out
    