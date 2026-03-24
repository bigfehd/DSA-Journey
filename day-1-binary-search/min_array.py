"""we are trying to find the index of the minimum of the value of the sub array
"""
array = [12,3,14,5,16,17,8]

n = len(array)

start =2
end = 5
min_index = start

for i in range(start, end+1):
    if array[i] < array[min_index] :
       min_index = i


print(min_index)