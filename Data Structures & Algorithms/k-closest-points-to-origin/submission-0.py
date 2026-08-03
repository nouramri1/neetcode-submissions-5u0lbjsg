class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []

        for i, point in enumerate(points):
            x, y = point
            distance = x ** 2 + y ** 2
            heapq.heappush(heap, (distance, i))

        for _ in range(k):
            distance, index = heapq.heappop(heap)
            res.append(points[index])

        return res
    
        