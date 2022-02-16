def solution(a0):
    
    a=[]

    x=a0
    while x not in a:
        a.append(x)
        x=str(x)
        summ=0
        sum_dig_sq=0
        for c in x:
            digsq=int(c)*int(c)
            sum_dig_sq+=digsq

        x=sum_dig_sq

    # +1 for the last one that is already in the list
    return len(a)+1

if __name__ == "__main__":
    print(solution(16))
    print(solution(a0 = 103))