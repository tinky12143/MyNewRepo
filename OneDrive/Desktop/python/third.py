# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 00:11:10 2022

@author: tinky
"""

dic={"1":"one","2":"two","3":"three"}
print(dic["1"])

counter = 0
while counter<3:
    counter+=1
    print(counter)

for letter in "Hey How are you":
    print(letter)
    
for num in [0,1,2,3,4]:
    print(num)
print()    
    
for num1 in range(2,7):
    print(num1)

print(pow(2,6))

def power(base,pow_num):
    result = base
    for index in range(pow_num-1):
        result=result*base
    return result

power(2,4)
        