# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
       
    
        root_arr = []
        que = deque()
        que.append(root)
        
        while que:
            node = que.popleft()
            if node:
                root_arr.append(node.val)
            else:
                root_arr.append("#")
                continue
            
            que.append(node.left)
            que.append(node.right)
        

        right = len(root_arr)
        i =  len(root_arr)-1
        while i > -1 :
            if root_arr[i] == "#":
                right = i
                i -=  1
            else:
                break
   
        return "".join([str(i) + "," for i in root_arr[:right]])
            
            
        

    def deserialize(self, data):
        
        child_ptr = 1
        parent_ptr = 0
        
        que = deque()
        
        

        data_arr = list(data.split(","))
        
        data = data_arr[:len(data_arr) - 1]
        
        
        if len(data) == 0:
            return None
        
        root = TreeNode(int(data[0]))
        que.append(root)
        
        while que:
            if child_ptr >= len(data):
                return root
            
            node = que.popleft()
            
            if data[child_ptr] != "#":
    
                left = TreeNode(int(data[child_ptr]))
            else:
                left = None
            

            if child_ptr + 1 >= len(data) or data[child_ptr + 1] == "#":
                right = None
            else:
                right = TreeNode(int(data[child_ptr + 1]))
           
        
            node.left = left
            node.right = right
            
            if left:
                que.append(left)
            if right:
                que.append(right)
        
            
            child_ptr += 2
        
        
        return root
       
          
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))