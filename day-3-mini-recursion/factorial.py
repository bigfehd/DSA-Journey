"""we want to get the factorial of a number say 5
so the concept of recursion is that on e we have a problem
we try to break the problem down into smaller problems
until we get to a point where the problem is entirely solvable
just like the russian doll, we have a very large doll
we remove the cover then we see a doll that is not as large as the main doll
we keep on removing the cover of each doll and might a smaller
version until we get to the last one whose cover cannot be removed again
"""

"""So in this we want to get factorial of a number say 5
we know 5! = 5*4*3*2*1 also we can say 5! = 5*4!
that will stil work and we can also say from 4! we know
4! = 4*3! then 3! = 3*2! then 2! = 2*1!

so replacing all this back to the initial we know
5! = 5*4!
5! = 5*4*3!
5! = 5*4*3*2!
5! = 5*4*3*2*1!
 so from this it is save to say for a factorial(5) it is equal to
 5*factorial(4), the factorial of 5 is solved below"""
 
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
n = 5

print(factorial(n))

"""then we try to solve for adding num, say we have to find the sum of 5
say 5 = 5+4+3+2+1 = 15 to do this we know
5 = 5+sum(4) || 5 = 5+4
5 = 5+4 + sum(3) || 4 = 4+3
5 = 5+4+3+sum(2)
5 = 5+4+3+2+sum(1), to solve this we would have, we want to
stop the recursion when n=1, we return 1"""

def sum_to_n(n):
    if n == 1:
        return 1
    return n + sum_to_n(n-1)

n = 5

print(sum_to_n(n))
 
