# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 23:34:23 2022

@author: tinky
"""

scores = (90,80,70,40,100)
print(scores[0:2])
print(len(scores))

#function
def hello(name):
    print("Hello"+name)

hello("yo")

def add(num1,num2):
    print(num1+num2)
    return num1+num2

print(add(4,5)    )

rainy=True
num1=3
if num1==3 and rainy:
    print(True)
elif num1 >20:
    print(False)

#and or or not !=

number1=float(input("Please enter the first number: "))
op=input("Input operator")
number2=float(input("Please enter the first number: "))

if op=="+":
    print(number1+number2)
elif op=="-":
    print(number1-number2)
else:
    print("Error")    
    