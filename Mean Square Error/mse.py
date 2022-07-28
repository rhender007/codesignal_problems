
def solution(array_a, array_b):
    zip_arr = zip(array_a,array_b)
    
    sum_sq = 0
    for i in zip_arr:
        sum_sq += (i[0]-i[1])**2
    return sum_sq/len(array_a)