def solution(inputString):
    dict_d = dict()
    
    for char in inputString:
        # check to see if char number in the dict
        if ord(char) in dict_d:
            dict_d[ord(char)] += 1
        else:
            dict_d[ord(char)] = 1

    # go through the keys and make sure we have 
    for i in dict_d.keys():
        # base case, continue
        if i == ord('a'):
            continue
        if i-1 in dict_d:
            if dict_d[i] > dict_d[i-1]:
                return False
        else: return False
    return True

if __name__ == "__main__":
    print(solution("bbbaacdafe"))
    print(solution("aabbb"))
    print(solution("bbc"))