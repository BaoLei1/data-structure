# -*- coding: utf-8 -*-
"""
Given an array nums of integers, return how many of them contain an even number of digits.

Created on Thu Mar 18 16:31:49 2021

@author: BB
"""

class Solution(object):
    def findNumbers( nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count =0
        for i in nums:
           if (len(str(i)) % 2 == 0):
                   count = count+1
        return count            


Solution.findNumbers( nums=[12,345,2,6,7896])
    
 

