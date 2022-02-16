def solution(score1, score2):
    if CheckEasyCase(score1,score2)==True:
        return True
    elif CheckSpecialCase(score1,score2)==True:
        return True
    return False

# 6, win by 2 case
def CheckEasyCase(score1,score2):
    if abs(score1-score2) >= 2 and max(score1, score2)==6:
        return True

# continue until one player has won 7 case, (win by 1 or 2)
def CheckSpecialCase(score1,score2):
    if max(score1, score2)==7 and 1<=abs(score1-score2)<=2:
        return True
        
if __name__ == "__main__":
    print(solution(3,6))
    print(solution(8,5))
    print(solution(6,5))