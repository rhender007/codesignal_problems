def solution(inputString):
    dict_d = dict()
    
    for char in inputString:
        # check to see if char number in the dict
        if char in dict_d:
            dict_d[char] += 1
        else:
            dict_d[char] = 1

    # go through the keys and make sure we have count b<a, c<b, etc.
    for i in dict_d.keys():
        # base case, continue
        if i == 'a':
            continue
        if chr(ord(i)-1) in dict_d:
            # if any letter count is greater than the prev alpha letter count, ret False
            if dict_d[i] > dict_d[chr(ord(i)-1)]:
                return False
        else: 
            return False
    return True

if __name__ == "__main__":
    print(solution("bbbaacdafe"))
    print(solution("aabbb"))
    print(solution("bbc"))