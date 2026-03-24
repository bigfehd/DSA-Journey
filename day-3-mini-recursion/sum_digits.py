"""Write a recursive function sum_digits(n) that returns sum of all
the digits of a positive integer n sum_digits(4321) = 10

just like in recursion we try to break it down and solve
in breaking it down first thing we have to do is we have to fund the best case
so in finding the best case lets use 4321 for example we want to do 4+3+2+1
how do we get 1, if we do 4321 divide 10 we get 432.1 thats 432 remainder 1
and 4321%10 will give us the remainder when we divide 4321 by 10, and the remainder here is 1
so that is what we need, so once we get the remainder 1 we say the remainder + sum_digits(432)
we do the same thing again for 432 % 10 remainder is 2 so we have sum_digits(43) + 2
then we do 43%10 we have 4 remainder 3 so thats sum_digits(4) + 3

    so for the last one we want it to return 4. so that is our best case
    safe to write formualr for our base case to be as far if n < 10: return n
    
    solving the code we have"""
    
def sum_digits(n):
    
    if n < 10 :
        return n
    return n%10 + sum_digits(n // 10)
n = 456378

print(sum_digits(n))


"""factorilal of a number say 3!, using recursion to solve this
we know 3! is 3x2x1 so the best case is when n =1 so we can writ the base case as n == 1 return 1 """

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

n = 3
print(factorial(n))
