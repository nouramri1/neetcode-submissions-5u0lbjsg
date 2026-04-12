from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we have an integer arra nums
        # integer k 
        # return k frequest element is the list 
        # creat a dic with the frequecies of all the numbersiin the lis 
        # freq = defaultdict{int} intialises the dict with
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
            
                
        # k most frequent
        # sort freq. values 
        sorted_dict = sorted(freq, key = freq.get, reverse = True)
        # return the top k keys 
        return sorted_dict[:k]