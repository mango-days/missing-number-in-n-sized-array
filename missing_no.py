# Given an array with all integers between 1 and 100 except for one, find the missing number.
n=100
arr = []
for index in range ( 0 , n ) : arr.append ( index+1 )
arr.remove (18)

total = int ( (n+1) * n / 2 )
sum_of_arr = sum( arr )
print ( total - sum_of_arr )