""""we are trying to compute the powers of a number so we would tackle this
problem using recursion, say we want to do 2^5, we can say 2 =  2 * 2^4,
 and 2^4 =  2 * 2^3, and 2^3 = 2 * 2^2, and 2^2 = 2 * 2^1, and 2^1 = 2 * 2^0. and 
 we know 2^0 is 1 so we can safely say that is our base case. because in recursion we must have a base case
 we can write the code as follows, but from 2^5 = 2 * 2^4, lets assume its x^n, so x^n = x * x^(n-1)"""
 
def power(x,n):
    if n == 0:
        return 1
    return x * power(x, n-1)
x = 2
n =5

result = power(x,n)
print(result)  

### time complexity of this code is O(n) because we are doing n recursive calls, and space complexity is also O(n) because of the call stack that is being used for the recursive calls.
 
 
 