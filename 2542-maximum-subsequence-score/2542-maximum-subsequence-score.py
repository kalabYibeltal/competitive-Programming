class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        heap = []
        for j in range(len(nums1)):
            heap.append([nums2[j], nums1[j]])
            
        
        heap.sort()
        running_sum = 0
        
        
        heapsum = []
        for i in range(len(heap)-1,len(heap)-k-1,-1):
            heappush(heapsum, heap[i][1])
            running_sum += heap[i][1]
        
        answer = heap[len(heap)-k][0] * running_sum

        for i in range(len(heap)-k-1,-1,-1):
            if heap[i][1] > heapsum[0]:
                running_sum = running_sum - heappop(heapsum) + heap[i][1]
                heappush(heapsum, heap[i][1])
                answer = max(answer, heap[i][0] * running_sum)
            
        
        return answer
