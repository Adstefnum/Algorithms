
  #O(2nm) time and space
  def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
      q = deque()
      rows = len(mat)
      cols = len(mat[0])
      directions = [[1,0],[-1,0],[0,1],[0,-1]]

      for r in range(rows):
          for c in range(cols):
              if mat[r][c] == 0:
                  q.append([r,c])
              else:
                  mat[r][c] = float("inf")

      while q:
          r,c = q.popleft()
          for dr,dc in directions:
              row,col = r+dr,c+dc
              if 0<= row < len(mat) and 0 <= col < len(mat[0]) and mat[row][col] > mat[r][c]+1:
                  q.append([row,col])
                  mat[row][col] = mat[r][c]+1



      return mat
