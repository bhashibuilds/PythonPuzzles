# In graphs we have matrix, adjacent matrices and adjacency lists. The most used ones are matrices and adjacency lists. 
# Matrices are columns and rows that are represented in a nested array. 
# Depth First search is used to traverse through all workable positions within a matrix

# Matrix DFS
# Matrix (2D Grid)
grid = [[0, 0, 0, 0], # This is an example grid 
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

# Count paths (backtracking)
def dfs(grid, r, c, visit): # defining dfs function with grid, row columns and a hashset visit that will tell us if we have visited something or not
    ROWS, COLS = len(grid), len(grid[0])
    if (min(r, c) < 0 or
        r == ROWS or c == COLS or
        (r, c) in visit or grid[r][c] == 1):
        return 0
    if r == ROWS - 1 and c == COLS - 1:
        return 1

    visit.add((r, c))

    count = 0
    count += dfs(grid, r + 1, c, visit)
    count += dfs(grid, r - 1, c, visit)
    count += dfs(grid, r, c + 1, visit)
    count += dfs(grid, r, c - 1, visit)

    visit.remove((r, c))
    return count

# Given a 2d grid where 1 represents land and 0 represents water, count and
# return the number of islands
# The main purpose of this code is to count the number of islands in a grid (or the group of 1's in the grid which are surrounded by water or 0's)
class Solution: # The solution is wrapped inside a class for later solution testing purposes
    def numIslands(self, grid: List[List[str]]) -> int: # the function numislands contains parameters self, grid, and will return an int saying how many islands there are 
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # this directions list gives us all the possible
        # moves for direction and traversal in the grid, you can move right left up and down moving in the x axis 
        # means (1,0) but to go left means to (-1,0) and its like that to go up or down as well 
        # going up down and left right is the general movements for bfs 
        ROWS, COLS = len(grid), len(grid[0]) # the row is the total length of the grid 
        # remember the grid is a nested array, so however many nested arrays there are is the amount of grids 
        # the rows and cols basically stores the x * y of the grid 
        # so far we have a list that has the directions stored aswell as 2 variables storing the length and width 
        # of the given array
        islands = 0 # we are initializing a variable island which will be set to 0 because we will add to this later 

        def bfs(r, c): # a helper function is created to perform the bfs search starting from a given position 
            # (r,c) in the grid r, c is the position on the grid that we have to input 
            q = deque() # an empty deque (which is a double ended queue that we can pop and push characters to)
            # it stores the nodes that have to be explored in bfs 
            grid[r][c] = "0" # this marks the starting cell in the grid to the value 0, to make sure that we do not visit this 
            # cell again
            q.append((r, c)) # adds the starting cell to the queue 

            while q: 
                row, col = q.popleft()  
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= ROWS or
                        nc >= COLS or grid[nr][nc] == "0"
                    ):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands

# fronm this i can understand that a block of land is an island and it 
# contains 1's It is asking us how many islands there are totally 
# but they can only be connected horizontally or diagonally not vertically 

 