# -*- coding: utf-8 -*-
"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number

Created on Thu Mar 18 17:09:09 2021

@author: BB
"""
# square each number in a list 
# sorted() returns a list in aceding order 


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x=[]
        for i in nums:
          x.append(  i**2)
          
        return sorted(x)    
    
  # one liner 
       #  return sortretuned(x*x for x in A)