# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 13:17:46 2019
#shanti gunna commenting 
@author: Vasanthi
"""

#for i in range(1000):print(i%3//2*'Fizz'+i%5//4*'Buzz'or i+1)
'''
sum = 0
for i in range(1, 1000):
    if i % 15 == 0:
        sum += i
    elif i % 3 == 0:
        sum += i
    elif i % 5 == 0:
       sum += i
print(i) 
print(sum)

'''
# Input

#import numpy as np

#np.set_printoptions(precision=2)
#a = np.arange(10,86,5).reshape(4,4)
#print(a)
# Solution 1: Using np.clip
#np.clip(a, a_min=10, a_max=30)

# Solution 2: Using np.where
#print(np.where(a < 10, 10, np.where(a > 30, 30, a)))
#> [ 27.63  14.64  21.8   30.    10.    10.    30.    30.    10.    29.18  30.
#>   11.25  10.08  10.    11.77  30.    30.    10.    30.    14.43]

#isHappyNumber() will determine whether a number is happy or not  
def isHappyNumber(num):  
    rem = sum = 0;  
      
    #Calculates the sum of squares of digits  
    while(num > 0):  
        rem = num%10;  
        sum = sum + (rem*rem);  
        num = num//10;  
    return sum;  
          
#Displays all happy numbers between 1 and 100  
n = int(input())  
count  = 0
print("The Happy Numbers between 1 and",n,"are")
for i in range(1, n):  
    result = i;  
      
    #Happy number always ends with 1 and   
    #unhappy number ends in a cycle of repeating numbers which contains 4  
    while(result != 1 and result != 4):  
        result = isHappyNumber(result);  
      
    if(result == 1):  
        count +=1
        print(i, end = ' ')
print("Total Happy Numbers are ",count)
        
