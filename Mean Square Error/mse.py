
def solution(array_a, array_b):
    zip_arr = zip(array_a,array_b)
    
    sum_sq = 0
    for i in zip_arr:
        sum_sq += (i[0]-i[1])**2
    return sum_sq/len(array_a)

a1 = [1,2,3]
a2 = [4,5,6]
  
test.assert_approx_equals(solution(a1, a2), 9)

b1 = [10, 20, 10, 2]
b2 = [10, 25, 5, -2]

test.assert_approx_equals(solution(b1, b2), 16.5)

c1 = [0, -1]
c2 = [-1, 0]

test.assert_approx_equals(solution(c1, c2), 1)

d1 = [10, 10]
d2 = [10, 10]

test.assert_approx_equals(solution(d1, d2), 0)
