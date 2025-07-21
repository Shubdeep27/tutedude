#Asignment 3 Task 1

x = int(input("Enter a number: " ))
def factorial(x):
   
    if x < 0:
       return ("factorial does not exist")
    elif x <= 1:
       return(1)
    else:
       return (x * (factorial(x-1)))

result = factorial(x)
print ("Factorial of",x , "is :", result)

#Assignment 3 Task 2
import math

p=float(input("Enter a number: "))
print ("Square Root:", math.sqrt(p))
print("Logarithm :", math.log(p))
print ("Sine :", math.sin(p))

#Assignment 3 task 2 second way taught
from math import *

print ("Square Root:", sqrt(p))
print("Logarithm :", log(p))
print ("Sine :", sin(p))
