# -*- coding: utf-8 -*-
"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Created on Mon Mar 22 16:16:17 2021

@author: BB
"""
class Solution(object):
    def merge( nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:]=nums2
        sorted(nums1)
        
nums1 = [1,2,3,0,0,0]; m = 3;nums2 = [2,5,6]; n = 3

#Output: [1,2,2,3,5,6]