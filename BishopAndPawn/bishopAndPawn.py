def solution(bishop, pawn):
    #a1
    bishop_x=bishop[0]
    bishop_y=int(bishop[1])
    
    pawn_x=pawn[0]
    pawn_y=int(pawn[1])
    
    bishop_x=ord(bishop_x)-ord('a')
    pawn_x=ord(pawn_x)-ord('a')
    
    # the x and y coord need to be equidistant
    if abs(bishop_x-pawn_x) == abs(bishop_y-pawn_y):
        return True
    else:
        return False

if __name__ == "__main__":
    print(solution(bishop = "a1", pawn = "c3"))
    print(solution(bishop = "h1", pawn = "h3"))