# 1. Biggie Size - Given a list, write a function that changes all
#    positive numbers in the list to "big". Example: biggie_size([-1, 3, 5, -5])
#    returns that same list, but whose values are now [-1, "big", "big", -5].

def Biggie(data):
    for number in range(len(datatest)):
        if data[number]>0:
            data[number]="big"
    return data

datatest = [-1,-2,4,6,12,-3]
print(datatest)
print(Biggie(datatest))

# 2. Count Positives - Given a list of numbers, create a function to replace
#    the last value with the number of positive values. (Note that zero is not
#    considered to be a positive number).
#    Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it.
#    Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it.

def Positive(data):
    sum=0
    for number in range(len(data)):
        if data[number]>0:
            sum=sum+1
    data[len(data)-1]=sum
    return data

datatest = [-1,-2,4,6,12,7]
print(datatest)
print(Positive(datatest))

# 3. Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
#    Example: sum_total([1,2,3,4]) should return 10
#    Example: sum_total([6,3,-2]) should return 7

def GetSum(data):
    sum=0
    for number in range(len(data)):
        sum=sum+data[number]
    return sum

datatest = [1,2,1,2,1,2,1]
print(datatest)
print(GetSum(datatest))

# 4. Average - Create a function that takes a list and returns the average of all the values.
#    Example: average([1,2,3,4]) should return 2.5

def GetAve(data):
    sum=0
    for number in range(len(data)):
        sum=sum+data[number]
    return sum/len(data)

datatest = [1,2,3,4]
print(datatest)
print(GetAve(datatest))

# 5. Length - Create a function that takes a list and returns the length of the list.
     # Example: length([37,2,1,-9]) should return 4
     # Example: length([]) should return 0

def GetLen(data):
    return len(data)

datatest = [-1,-2,4,6,12,-3]
print(datatest)
print(GetLen(datatest))

# 6. Minimum - Create a function that takes a list of numbers and returns the minimum value in the list.
#    If the list is empty, have the function return False.
     # Example: minimum([37,2,1,-9]) should return -9
     # Example: minimum([]) should return False

def GetMin(data):
    minval=1e10
    for number in range(len(data)):
        if data[number] < minval:
            minval=data[number]
    return minval

datatest = [1,2,3,4]
print(datatest)
print(GetMin(datatest))

# 7. Maximum - Create a function that takes a list and returns the maximum value in the array.
#    If the list is empty, have the function return False.
     # Example: maximum([37,2,1,-9]) should return 37
     # Example: maximum([]) should return False

def GetMax(data):
    maxval=-1e10
    for number in range(len(data)):
        if data[number] > maxval:
            maxval=data[number]
    return maxval

datatest = [1,2,3,4]
print(datatest)
print(GetMax(datatest))

# 8. Ultimate Analysis - Create a function that takes a list and returns a dictionary that has
#    the sumTotal, average, minimum, maximum and length of the list.
#    Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def UA(data):
    results={"sumTotal":0,"average":0,"minimum":1e5,"maximum":-1e5,"length":0}
    for i in range(0,len(data)):
        results['sumTotal']=results['sumTotal']+data[i]
        if(data[i]<results['minimum']):
            results['minimum']=data[i]
        if(data[i]>results['maximum']):
            results['maximum']=data[i]
    results['average']=results['sumTotal']/len(data)
    results['length']=len(data)
    return results

datatest = [1, 2, 3, 4]
print(datatest)
print(UA(datatest))