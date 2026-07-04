class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_len = len(s1)
        target_count = {}
        for c in s1:
            target_count[c] = 1 + target_count.get(c,0)
        new_s2 = ""
        for c in s2:
            if c not in s1:
                new_s2 += '#'
            else:
                new_s2 += c
            
        for c in range(len(new_s2)):
            sub = new_s2[c: c + target_len ]
            if '#' not in sub:
                sub_count = {}
                for c in sub:
                    sub_count[c] = 1 + sub_count.get(c, 0)
                if sub_count == target_count:
                    return True
                

                
        return False
