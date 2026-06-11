class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #frequency map for each and then compare the frequency map
        # or sort both string a to z and then if its the same word return 
        #true othrwise return false 
        
        # i can add an early length check 
        if len(s) != len(t):
            return False
        sorted_s = ''.join(sorted(s))
        sorted_t = ''.join(sorted(t))
        if sorted_s == sorted_t :
            return True
        else:
            return False
        # here it can be directly return sorted_s == sorted_t and it will 
        # return True or False 


        