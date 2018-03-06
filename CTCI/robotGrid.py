def robotGrid(r,c,matrix):
    arr = []
    arr = getPath(r,c,matrix,arr) 
    return arr
     

def getPath(r,c,matrix,arr):
    
    if r >= len(matrix):
        return arr
    
    if c >= len(matrix[0]):
        return arr
    
    if matrix[r][c] == None:
        return arr
   
    if r == len(matrix) -1 and c == len(matrix[0]) -1:
        return arr

    getPath(r+1,c,matrix,arr.add((r,c)))
    getPath(r,c+1,matrix,arr.add((r,c)))
        
