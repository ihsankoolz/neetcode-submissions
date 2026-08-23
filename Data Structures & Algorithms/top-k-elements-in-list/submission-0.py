class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for i,x in enumerate(nums):
            if x not in dict:
                dict[x] = 1
            else:
                dict[x] += 1
        heap = []
        for num, freq in dict.items():
            heapq.heappush(heap,(freq,num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for freq, num in heap]
        
        
        