class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for index in range(len(edges)):
            graph[edges[index][0]].append([edges[index][1], succProb[index]])
            graph[edges[index][1]].append([edges[index][0], succProb[index]])
        
        visited = set()
        heap = []
        heappush(heap, [-1,start_node])
        
        while heap:
            prob, node = heappop(heap)
            visited.add(node)
            if node == end_node: return  -prob
            
            for nei, probn in graph[node]:
                if nei not in visited:
                    heappush(heap, [prob * probn, nei])
            
        
        return 0
                
            