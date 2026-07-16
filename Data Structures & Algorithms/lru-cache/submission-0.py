class LRUCache:

    def __init__(self, capacity: int):
        # initiate always we use use self , ecause w eare creating a data structure
        self.cache = []
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                tmp = self.cache.pop(i)
                self.cache.append(tmp)
                return tmp[1]
        return -1

        

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                self.cache.pop(i)
                self.cache.append([key, value])
                return

        if self.capacity == len(self.cache):
            self.cache.pop(0)
        self.cache.append([key,value])
