import math
def solution(grid):
                                
    if CheckCols(grid) and CheckRows(grid) and ValidateBoxes(grid) == True:
        return True
    return False
    
def ValidateBoxes(grid):
    # box starting x
    for row in range(0,len(grid),int(math.sqrt(len(grid)))):
        # box starting y
        for col in range(0, len(grid),int(math.sqrt(len(grid)))):
            if ValidateBox(grid,row,col) == False:
                return False
    return True

def ValidateBox(grid,row,col):
    nums=[]
    for i in range(int(math.sqrt(len(grid)))):
        for j in range(int(math.sqrt(len(grid)))):
            nums.append(grid[row+i][col+j])
    if len(set(nums))==len(nums):
        return True
    else:
        return False
    
def CheckCols(matrix):
    # for each row index i 
    for i in range(len(matrix)):
        column=[matrix[j][i] for j in range(len(matrix))]
        if CheckColumn(column) == False:
            return False
    return True
    
def CheckRows(matrix):
    # a=[]
    # iterate over the rows
    for row in matrix:
        if CheckRow(row)==False:
            return False
    return True
    
def CheckRow(row):
    a=[]
    # iterate over the rows
    for r in row:
        if r not in a:
            a.append(r)
        else:
            return False
    return True

def CheckColumn(column):
    a=[]
    # iterate over the columns
    for c in column:
        if c not in a:
            a.append(c)
        else:
            return False
    return True
    
if __name__ == "__main__":
	test = solution(grid = [[1, 3, 2, 5, 4, 6, 9, 8, 7],
        [4, 6, 5, 8, 7, 9, 3, 2, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]])
	print(test)