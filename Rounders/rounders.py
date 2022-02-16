def solution(n):

    # divide by 10 and round
    t=n
    for i in range(len(str(n))-1):
        t=t/(10**(i+1))
        t=int(t+.5)
        t=t*(10**(i+1))
        
    return t

if __name__ == "__main__":
    print(solution(15))
    print(solution(1234))
    print(solution(1445))
