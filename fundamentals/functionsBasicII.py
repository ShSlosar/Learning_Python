#1: CountDown Function
def coutnDown(num=10):
    countList =[]
    for num in range(num,-1,-1):
        countList.append(num)
    print(countList)
coutnDown(5)
coutnDown()

#2:Print and Return - Create a function that will receive a list with two numbers.
# Print the first value and return the second.
#Example: print_and_return([1,2]) should print 1 and return 2

def priAndRet(ar=[1,2]):
    print(ar[0])
    return ar[1]
priAndRet([2,3])
priAndRet()

#3: First Plus Length - Create a function that accepts a list and returns the sum
# of the first value in the list plus the list's length.
#Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def fstPlsLng(df=[1,2,3]):
    f = df[0]
    return f + len(df)
print(fstPlsLng())
print(fstPlsLng([2,3,4]))

#4: Values Greater than Second - Write a function that accepts a list and creates
# a new list containing only the values from the original list that are greater
# than its 2nd value.  Print how many values this is and then return the new list.
# If the list has less than 2 elements, have the function return False
#Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
#Example: values_greater_than_second([3]) should return False

def valGtrThnSec(lis=[2,3,4,5,6]):
    newLis = []
    if len(lis) < 2:
        return False
    else:
        for n in range(0,len(lis)):
            if lis[n] > lis[1]:
                newLis.append(lis[n])
    print(len(newLis))
    return newLis
print(valGtrThnSec())

#5: This Length, That Value - Write a function that accepts two integers as parameters:
# size and value. The function should create and return a list whose length is equal to the
# given size, and whose values are all the given value.
#Example: length_and_value(4,7) should return [7,7,7,7]
#Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def lngtAndVal(length=2, value=3):
    lst = []
    for n in range(length):
        lst.append(value)
    return lst
print(lngtAndVal())
print(lngtAndVal(3,2))