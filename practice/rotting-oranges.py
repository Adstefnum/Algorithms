#O(nm) time and same for space at worst if all squares contain oranges either fresh 
#that will become rotten or original rotten
def orangesRotting(self, grid: List[List[int]]) -> int:
    q = deque()
    rows,cols = len(grid),len(grid[0])
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    time,fresh = 0,0

    #preprocessing to add originally rotten oranges to queue
    #and get number of frresh oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh += 1
            if grid[r][c]==2:
                q.append([r,c])

    while q and fresh >0:
        #this original length does not change until after a complete 
        #iteration by those originally in the queue which is when the time will
        #increase
        for _ in range(len(q)):
            r,c = q.popleft()
            for dr,dc in directions:
                row, col = dr+r, dc+c
                if (row <0 or row == len(grid) or 
                    col <0 or col == len(grid[0]) or 
                    grid[row][col] != 1) : 
                    continue
                grid[row][col] = 2
                fresh -= 1
                q.append([row,col])
        #after each collection of rotten oranges have all infected others
        time += 1
    return time if fresh ==0 else -1
