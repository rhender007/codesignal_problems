def solution(n):
    s=str(n)
    return max([int(s[:i] + s[i+1:]) for i in range(len(s))])
    
if __name__ == "__main__":
    print(solution(152))
    print(solution(1001))