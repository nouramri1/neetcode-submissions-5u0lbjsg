class Solution:
    def longestPalindrome(self, s: str) -> str:
        # think of each cahrater as the middle 
        
        longest = ""
        res = 0 
       
        for i in range(len(s)):
            l,r = i,i
            while l>=0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res:
                    longest = s[l: r+1]
                    res = r - l + 1
                l -= 1
                r += 1
                
        
        for i in range(len(s)):
            l,r = i , i +1 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res:
                    longest = s[l: r + 1]
                    res = r - l + 1
                l-= 1
                r +=1
        return longest
            
            
                    
        