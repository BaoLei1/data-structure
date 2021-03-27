"""
looking fot max consecutinve ones 
  
Created on Mon Mar 15 16:57:18 2021

@author: BB
"""
 
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
      
        
        count=max_count=0
        for i in nums:
            if (i==1 ):
                count = count+1
            else:
               
                max_count = max(max_count, count) # return the bigest item
                # Reset count of 1.
                count = 0
        return max(max_count, count)   
