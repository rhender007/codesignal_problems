def fizzbuzz(n):
    
    ret=[]
    for i in range(1, n+1):
        if i%3==0 and i%5==0:
            ret.append("FizzBuzz")
        elif i%3==0:
            ret.append("Fizz")
        elif i%5==0:
            ret.append("Buzz")
        else:
            ret.append(i)
    return ret

test.describe('Fizzbuzz')
test.it('Should fizzify 10 numbers correctly')
expected = [1,2,'Fizz',4,'Buzz','Fizz',7,8,'Fizz','Buzz']
test.assert_equals(fizzbuzz(10), expected)
