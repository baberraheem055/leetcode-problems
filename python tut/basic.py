"""
name = "Brook"
print("Hello " + name)

#calculation
print(5+3)
print(5/3)

print("++++++++++++++++++++++++++++++++++++++++++++")
import math

result = math.sqrt(9)
print(result)

#or
result = 9 ** 0.5
print(result)

#if else commands

age= 32
if age>23:
    print("you are eliable")
elif age==23:
    print("not eligable")
"""
#++++++++++++++++++++++++++++++++++++++++++++++++++++
    #funtions in python
# 1.In Python a function is defined using the "def" keyword:
def my_print():
    print("this is my first function in python")

#funtioncall
my_print()

#aurgument pass 

def stu(name):
    print(name + " khan")
    
stu("baber")
stu("shayan")

#if the number of aurgements is unknown at the start
def characteristics(*ch):
    print("ali is "+ ch[0])
    print("ali is "+ ch[1])
    print("ali is "+ ch[2])

characteristics("good","antelligent","sincer")

#defalut parameters
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#passing list to funtion as an argumet
def sumf(arr1):
    for i in arr1:
        print(i)

arr=["ali","baber","tayyab"]
arr1={2,3,4,4,5}
sumf(arr1)

#division 

print(50/3)            #result 16.6666666
#to get floor value use double divison sign "//" i,e
print(50//3)            #result 16
print(int(50/3))        #result 16

#reminder
print(49%7)             #reminder 0

#to calculate power i.e 5^3
print(5**3)

#STRINGS
print('hello world')
print("i don't have")
print('Yes, he said \n ali repaly') #backlash \n for newline
print('C:\some\name')               #this line of code will not print correctly due to "\n"
print(r'C:\some\name')              #here byusing "r" before 'C:\some\name' will avoid this logical error

#i. string concatenation
f_name='baber'
print (f_name + 'khan')
print('baber''raheem')

#ii. string index
name='ali'
print(name[0])
print(name[1])
print(name[-1])      #[-1] will always print the last element of the array

#length of the list
array=['a','n']
len(array)

#for loop 
array=['a','n','b','v']
for i in array:
    print(i)

#rang() It generates arithmetic progressions
arr1=[1,2,3,4,5,6]
for i in range(9):
    print(i)

#to print the indices plus the element at that indices #problem
    ''' caution: Use a list when you need to maintain the order of elements, and when you might have duplicates, or when you need to access elements by their index.
        Use a set when you need to ensure uniqueness of elements or when you need to perform fast membership tests.'''

arr2={'baber','raheem','shayan','zeshan','shah zaid'}
#to change baraket to list
list_arr2=list(range(5))
list(arr2)
for i in range(list_arr2):
    print(i,list_arr2[i])


#explicit conversion - when code is written to manually convert one data type to another using a data type conversion function:

'''str() - converts a value (often numeric) to a string data type

int() - converts a value (usually a float) to an integer data type

float() - converts a value (usually an integer) to a float data type
'''
