def position_of_array(primes,target):
    """ so if we have an array of numbers say prime numbers
     we want to find out if a number say 67 is there we make use of binary search to find it"
    we would not use linear search because it would be too long and time complexity is o(logn)
    so in the numbers what we want to do first is know the range from left to right, we might not know
    where the number stops but we know it starts from 0 at least so we say the left = 0 then the right is
    lenght of the array -1, due to indexing principle... so now we have the range we want our program to work inside
    so what we wanna do next is to use a while loop to help our program know wat to do, then we write the condition 
    of the while loop... now our program will keep on looping as long as the left value is always less or equal to the right
    e,g left<=right... immediately right>left the program ends.. so in the loop first thing is we want to always find the 
    mid point, which is left+right/2 after finding the mid point check if it is less than the value we are trying to find,
    then also check if it is greater than the value we are trying to find...
     
     Three case scenarios
    i) if our midpoint is less than the target number we increase our initial midpoint by 1; "this means we no longer need
    the numbers that come before that midpoint, so we set our left to the new position, so left =  midpoint + 1"
    ii) if our midpoint is higher than the target number we decrease our initial midpoint by 1; this means we no longer
    need the numbers after the current midpoint.so the right part of our array becomes right = midpoint + 1
    iii) when right> left that means the number is no longer in the array; then we return -1
    
    the loop keeps running until we find the index position of our target
    
    """
    
    left = 0
    right = len(primes) -1
    
    while left<=right:
        mid = (left+right) // 2
        
        if primes[mid] == target:
            return mid
        elif primes[mid] < target:
            left = mid + 1
        elif primes[mid] > target:
            right = mid -1
    else:
        return -1 
    
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
target = 99

print(position_of_array(primes,target))
    
        