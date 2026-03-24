"""
This code explains how we would swap the numbers in an array using an 
optimized bubble sort algorithm with a time complexity of O(n).
the time complexity is O(n) because once we find out the array is sorted 
we just stop the program early the loop runs n times, and each iteration
performs constant work, if we were to use normal bubble sort the time 
complexity would be O(n^2). 

"""



array = [2,3,4,5,6,7,8,9]

n = len(array)
count = 0
for i in range(n):
    count = count+1
    swapped = False
    for items in range(n-1):
        if array[items] > array[items+1]:
            array[items],array[items+1] = array[items+1], array[items]
            swapped = True
        if swapped == False:
            break

print(array,count)
        


        