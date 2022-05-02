#depth first search
#O(nm) time, n*m being the area of the space to be filled
#O(nm) space as this is what will fill the call stack??
def floodFill(image, sr:int, sc:int, newColor:int):
    rows = len(image)
    cols = len(image[0])
    def dfs(image, sr: int, sc: int, newColor: int,oldColor: int):
        
        if sr>=rows or sr < 0 or sc >= cols or sc < 0 or image[sr][sc]!= oldColor:
            return
        image[sr][sc] = newColor
        #down
        dfs(image,sr+1,sc,newColor,oldColor)
        #up
        dfs(image,sr-1,sc,newColor,oldColor)
        #left
        dfs(image,sr,sc-1,newColor,oldColor)
        #right
        dfs(image,sr,sc+1,newColor,oldColor)
    
    oldColor = image[sr][sc]
    #if this is true we would have to refill the image already filled with the proper color
    if oldColor == newColor:
        return
    else:
        dfs(image,sr,sc,newColor,oldColor)

# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1
# sc = 1
# newColor = 2
image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
newColor = 2
floodFill(image,sr,sc,newColor)
print(image)
