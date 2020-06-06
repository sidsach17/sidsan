# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 14:40:05 2020

@author: siddhant.khare
"""
print("sanchi")

# A Python program to demonstrate use of  
# generator object with next()  
  
# A generator function 
def simpleGeneratorFun(): 
    yield 1
    yield 2
    yield 3
   
# x is a generator object 
x = simpleGeneratorFun() 
  
# Iterating over the generator object using next 
print(x.__next__()) # In Python 3, __next__() 
print(x.__next__()) 
print(x.__next__()) 

print(type(x))


class Fraction(object):
    def __init__(self, num, denom):
        self.numerator = num
        self.denominator = denom

def main():
    f = Fraction(1, 3)
    print(type(f))

if __name__ == "__main__":
    main()
    
print(isinstance(f, Fraction)) 
# Python program explaining 
# vstack() function 

import numpy as np 

# input array 
in_arr1 = np.array([ 1, 2, 3] ) 
print ("1st Input array : \n", in_arr1) 

in_arr2 = np.array([ 4, 5, 6] ) 
print ("2nd Input array : \n", in_arr2) 

# Stacking the two arrays vertically 
out_arr = np.vstack((in_arr1, in_arr2)) 
print ("Output vertically stacked array:\n ", out_arr) 

import types
types.GeneratorType

isinstance(x, types.GeneratorType)
isinstance(f, types.GeneratorType)


class sid(x):
    def __init__(self, num, denom):
        self.numerator = num
        self.denominator = denom
   

z=sid(5,6)
print(z)
type(z)


# Python code for isinstance() 
class Test: 
	a = 5
	
TestInstance = Test() 

print(isinstance(TestInstance, Test)) 
print(isinstance(TestInstance, (list, tuple))) 
print(isinstance(TestInstance, (list, tuple, Test))) 

    
data = []
data.append("A")
data.append("B")
data.append("C")
data.append("D")

lst = [1,2,3,4]
x = (n for n in lst)
print(x)
print(type(x))





import time
start_time = time.time()
x = 6
y = x+1
print("--- %s minutes ---" % ((time.time()/60) - (start_time/60)))
print(time.time.process_time)