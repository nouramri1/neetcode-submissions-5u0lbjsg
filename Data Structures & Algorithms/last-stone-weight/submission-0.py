class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we are creating a max heap
        maxHeap = [ - stone for stone in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            x = - heapq.heappop(maxHeap)
            y = - heapq.heappop(maxHeap)
            if x != y:
                heapq.heappush(maxHeap, -(x-y))
        if maxHeap:
            return - maxHeap[0]
        return 0




        