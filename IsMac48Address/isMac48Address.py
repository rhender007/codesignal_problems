def solution(inputString):
    import re

    # 5 sets of the ones w -, then one with no - end
    pattern = r"^([0-9a-fA-F]{2}-){5}[0-9a-fA-F]{2}$"
    if re.match(pattern, inputString):
        return True
    else:
        return False
if __name__ == "__main__":
    print(solution("00-1B-63-84-45-E6"))
    print(solution("Z1-1B-63-84-45-E6"))
    print(solution("01-23-45-67-89-AB"))