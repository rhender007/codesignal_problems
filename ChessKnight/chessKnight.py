class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)
    def __str__(self):
        return str(self.x)+","+str(self.y)

def solution(cell):
    # move 2 squares, 1 or 1, 2 in either direction as long not out of bounds
    x=ord(cell[0])-ord('a')+1
    y=int(cell[1])
    bounds = 8
    
    # 8 different ways the horse can go
    moves = []
    moves.append(Position(-1, -2))
    moves.append(Position(-2, -1))
    moves.append(Position(-2,1))
    moves.append(Position(-1,2))
    moves.append(Position(1,2))
    moves.append(Position(2,1))
    moves.append(Position(2,-1))
    moves.append(Position(1,-2))
     
    loc=Position(x,y)
    xy=[loc+p for p in moves]
    good_moves=sum([1 for p in xy if p.x>0 and p.y>0 and p.x<=8 and p.y<=8])
    
    return good_moves

if __name__ == "__main__":
    print(solution("a1"))
    print(solution("c2"))