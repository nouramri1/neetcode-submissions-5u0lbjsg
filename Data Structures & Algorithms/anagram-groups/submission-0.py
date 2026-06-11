class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #group anagrams together
        #input: list of strings
        #output : list of list of strings
        # go over each one 
        # get a dictionary , the key wwill be each the sorted distinct words
        # return the values in a list of list 
        map = {}
        
        for word in strs:
            key = ''. join(sorted(word))
            if key not in map:
                map [key] = []
            map[key].append(word)
        return list(map.values())

        