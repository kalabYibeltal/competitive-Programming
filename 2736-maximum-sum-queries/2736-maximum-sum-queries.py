class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.l = None
        self.r = None

class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        
        
        nums = [[x, y] for x, y in zip(nums1, nums2)]
        nums.sort()
        stack = []
        
        out = []
        
        for x, y in nums:
            
            
            while stack and y >= stack[-1][1]:
                stack.pop()
            
            stack.append([x,y])
        
        
        
        # create the segment tree
        sumtree = [x+y for x,y in stack]
        # print(sumtree)

        while (math.ceil(math.log(len(sumtree), 2)) != math.floor(math.log(len(sumtree), 2))):
            sumtree.append(0)
         
        def segmentC(l, r):
            node = Node(0)
            
            if l != r:
                node.left = segmentC(l, l + (r-l)//2)
                node.right = segmentC( l + (r-l)//2 + 1, r)
                node.l = l
                node.r = r
                ans = max( node.left.data, node.right.data)
            else:
                node.l = l
                node.r = r
                ans = sumtree[l]
            
            node.data = ans
            return node
        
        root = segmentC(0, len(sumtree) - 1)
        
        #maximum number founder from left and right bound in the segment tree
        def find(l,r, node):
            if l > r: return 0
            
            if l == node.l and r == node.r:
                return node.data
            
            return max(find( l, min(node.left.r, r), node.left),  find( max(l, node.right.l),  r, node.right ) )
        
            
        
        for x, y in queries:   
            #find left bound of the search space
            left, right = 0, len(stack) -1
            
            l = -1
            
            while left <= right:
                mid = (left + right)// 2 
                if stack[mid][0] >= x:
                    l = mid
                    right = mid - 1
                
                else: left = mid + 1
            
            #find right bound of the search space
            left, right = 0, len(stack) -1
            
            r = -1
            
            while left <= right:
                mid = (left + right)// 2 
                if stack[mid][1] >= y:
                    r = mid
                    left = mid + 1
                
                else: right = mid - 1
           
            if l == -1 or r == -1 or l > r:
                out.append(-1)
                continue
                
            # find maximum sum from left and right bound from the segment tree
            out.append(find(l,r, root))
            
    
        return out