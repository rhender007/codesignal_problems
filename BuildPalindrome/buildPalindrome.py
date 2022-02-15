def solution(st):
    if st == st[::-1]:  # Check for initial palindrome
        return st
    
    block=""
    for c in st:
        # iterate through the ori string and get add to block to build the pal
        block+=c
        
        poss=st+block[::-1]
        if poss==poss[::-1]:
            return poss
            
if __name__ == "__main__":
    print(solution("abcdc"))