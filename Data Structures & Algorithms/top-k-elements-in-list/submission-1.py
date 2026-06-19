class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # a frequency dictionary 
        count = {}
        for num in nums:
            count[num]= count.get(num, 0) + 1
        # sort  based on keys and reverse 
        sorted_num = sorted(count.keys(), key = lambda num: count[num], reverse = True)
        return sorted_num[: k]

            
            

        