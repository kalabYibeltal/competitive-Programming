import sys
sys.setrecursionlimit(250000)
def color(matrix,image,row,col,newc,val):
    if row > (len(image)-1) or col > (len(image[0])-1) or row < 0 or col<0:
        return image
    image[row][col]=newc
    matrix[row][col]=1
    if row+1 <= (len(image)-1) and matrix[row+1][col]==0 and image[row+1][col]==val:
        color(matrix,image,row+1,col,newc,val)
    if  col+1 <= (len(image[0])-1) and matrix[row][col+1]==0 and image[row][col+1]==val:
        color(matrix,image,row,col+1,newc,val)
    if image[row-1][col]==val and matrix[row-1][col]==0:
        color(matrix,image,row-1,col,newc,val)
    if image[row][col-1]==val and matrix[row][col-1]==0:
        color(matrix,image,row,col-1,newc,val)
    return image
    
    
    
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        matrix = [ [ 0 for i in range(len(image[0])) ] for j in range(len(image)) ]
        return color(matrix,image,sr,sc,newColor,image[sr][sc])
