def solution(inputString):
    b = dict()
    
    for char in inputString:
        
        # check to see if char number in the dict
        if ord(char) in b:
            b[ord(char)] += 1
        else:
            b[ord(char)] = 1

    # go through the keys and make sure we have 
    for i in b.keys():
        # base case, continue
        if i == 97:
            continue
        if i-1 in b:
            if b[i] > b[i-1]:
                return False
        else: return False
    return True

if __name__ == "__main__":
    print(solution("bbbaacdafe"))
    print(solution("aabbb"))
    print(solution("bbc"))