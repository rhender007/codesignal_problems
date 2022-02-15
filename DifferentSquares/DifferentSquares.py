def solution(matrix):
    # start at the top left, then right, then down, then right

    rows=len(matrix)
    cols=len(matrix[0])
    
    # these 2 cases are ez. no need to enter
    if rows<2 or cols <2:
        return 0
    if rows ==2 or cols ==2:
        return 1
        
    mat_list=[]
    for i in range(len(matrix)-1):
        for j in range(len(matrix[i])-1):
            mat=[[matrix[i][j],matrix[i][j+1]],[matrix[i+1][j],matrix[i+1][j+1]]]
            if mat not in mat_list:
                mat_list.append(mat)
            # print(mat_list)
    return len(mat_list)

if __name__ == "__main__":
    print(solution([[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]))