import math
def list_squared(m, n):
    list = []
    for i in range(m, n + 1, 1):
        sumOfSqrs = getSumOfSqrs(i)
        num = math.sqrt(sumOfSqrs)
        if num.is_integer():
            
            list.append([i, sumOfSqrs])
    return list
            
    
    
def getSumOfSqrs(num):
    list = []

    for i in range(1, int(math.sqrt(num) + 1), 1):
        if (num % i == 0):
            if (num / i == i):
                list.append(i**2)
            else:
                list.append(i**2)
                list.append(int(num/i)**2)
    return sum(list)

# Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764. The sum of the squared divisors is 2500 which is 50 * 50, a square!

# Given two integers m, n (1 <= m <= n) we want to find all integers between m and n whose sum of squared divisors is itself a square. 42 is such a number.

# The result will be an array of arrays or of tuples (in C an array of Pair) or a string, each subarray having two elements, first the number whose squared divisors is a square and then the sum of the squared divisors.

# #Examples:

# list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
# list_squared(42, 250) --> [[42, 2500], [246, 84100]]