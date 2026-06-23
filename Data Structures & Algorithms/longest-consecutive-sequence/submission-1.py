class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # an array of ntegers num
        # output : longest consecutive sequence of elements 
        # an elemnt that has to be exactly 1 greater than the previous element 
        # the trick here to check the begining of each new sequece and count 

        #to avaoid duplictation turn the array into set 
        numSet = set(nums)
        # track the longest sequece 
        # initialise a variable 
        longestsequence = 0 
        for num in nums:
            if (num- 1 ) not in numSet:
                currlength = 0
                while (num + currlength) in numSet:
                    currlength += 1
                longestsequence = max (longestsequence, currlength)
        return longestsequence
            
               


    
        