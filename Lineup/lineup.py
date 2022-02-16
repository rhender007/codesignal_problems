def solution(commands):

    size = len(commands)
    deg = 0
    ret = 0
    for i in range(0,size):
        if commands[i] == 'L':
            deg += -90
        elif commands[i] == 'R':
            deg += 90
        elif commands[i] == 'A':
            deg += 180
        if deg%180==0:
            ret += 1
            deg = 0
    return ret
    
if __name__ == "__main__":
    print(solution("LLARL"))
