# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 11:46:01 2021

@author: BB
"""
import numpy as np
class Solution(object):
    def duplicateZeros(  arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
# solution1 
        arr=[1,0,2,3,0,4,5,0]
        arr=np.array(arr)
        zer= np.where(arr==0)[0]
        inser=np.insert(arr,zer,0)
        obj=np.count_nonzero(arr==0) 
        #count how many zeros
        
        # deleting the count of zeros 
        np.delete(inser,range(-1,-obj-1,-1))
         

# solution two failed, look at note below 
        arr=[1,0,2,3,0,4,5,0]  
        i=0 
        while i < len(arr):
             if arr[i]==0:
                 arr.insert(i+1,0)
                 arr.pop()
                 i = i+1
             i +=1 
        arr    
#tried for loop 
    # cant not move skip a index 
    # target list can not be alter. use while loop insted        
# worked on grader but run time is super slow 



# solution 3
        possible_dups = 0
        length_ = len(arr) - 1

        # Find the number of zeros to be duplicated
        for left in range(length_ + 1):
         # index of an array 
                       # 
            # Stop when left points beyond the last element in the original list
            # which would be part of the modified list
            if left > length_ - possible_dups:
                break

            # Count the zeros
            if arr[left] == 0:
                # Edge case: This zero can't be duplicated. We have no more space,
                # as left is pointing to the last element which could be included  
                if left == length_ - possible_dups:
                    arr[length_] = 0 # For this zero we just copy it without duplication.
                    length_ -= 1
                    break
                possible_dups += 1

        # Start backwards from the last element which would be part of new list.
        last = length_ - possible_dups

        # Copy zero twice, and non zero once.
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]



