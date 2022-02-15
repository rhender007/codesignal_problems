def solution(time):
    pattern = r"([\d]{2}:){1}[\d]{2}"
    import re
    pat = re.match(pattern,time)
    if pat==None:
        return False
    
    hours=time[:2]
    mins=time[3:]
    
    if 0 <= int(hours) < 24 and 0<= int(mins) <60:
        return True
    else:
        return False
        
if __name__ == "__main__":

    print(solution("13:58"))
    print(solution("25:51"))
    print(solution("02:76"))
