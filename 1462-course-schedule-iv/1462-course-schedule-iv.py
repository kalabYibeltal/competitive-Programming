class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        ###floyd warshall
        adj_matrix = [[False for _ in range(numCourses)] for __ in range(numCourses)]
        
        for i, j in prerequisites:
            adj_matrix[i][j] = True
        
        for middle in range(numCourses):
            for child in range(numCourses):
                for parent in range(numCourses):
                    adj_matrix[parent][child] = adj_matrix[parent][child] or (adj_matrix[parent][middle] and adj_matrix[middle][child]) 
        
        out = []
        for i,j in queries:
            out.append(adj_matrix[i][j])
        
        return out