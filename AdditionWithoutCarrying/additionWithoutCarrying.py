def solution(param1, param2):

    param1=str(param1)
    param2=str(param2)
    
    # add leading zeros to add numbers
    if len(str(param1))<len(str(param2)):
        param1=str('0'*(len(str(param2))-len(str(param1))))+str(param1)
        
    if len(str(param2))<len(str(param1)):
        param2=str('0'*(len(str(param1))-len(str(param2))))+str(param2)

    s=[]
    for i in range(len(param1)):
        p1=int(param1[i])
        p2=int(param2[i])
        
        # add 2 digits, mod 10, then add to s sum string
        summ=(p1+p2)%10
        s+=str(summ)
    return int("".join(s))

if __name__ == "__main__":
    print(solution(456,1734))