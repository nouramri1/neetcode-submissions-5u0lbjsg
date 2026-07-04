class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t, count_window = {} , {}
        l = 0 
        res , res_length = [-1, -1] , float("infinity")

        for c in t:
            count_t[c] = 1 +  count_t.get(c,0)
        # initialise two counters to check what we need and what we have
        have, need = 0 , len(count_t)   

        for r in range(len(s)):
            count_window[s[r]] = 1 + count_window.get(s[r], 0)
            if s[r] in count_t and count_window[s[r]] == count_t[s[r]]:
                have += 1
            while need == have:
                #update or res
                if (r - l + 1) < res_length:
                    res = [l,r]
                    res_length = r - l + 1
                # pop from the left 
                count_window[s[l]] -= 1
                if s[l] in count_t and count_window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        return s[l:r+1] if res_length != float("infinity") else ""






    

        