# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 11:26:13 2022

@author: tinky
"""


Activities = ['Communication', 'Planning', 'Design', 'Construction', 'Testing']
Activities.sort()
print(Activities)
print(Activities[-1])


#Write a program in python using if condition. Input the temperature (user input). Check if
#the temperature is less than 98 display the result as cold. Otherwise, if the temperature more than
#98, display the result as Hot. Otherwise, display them as normal

#temp=float(input("What is the temperature"))
#if temp < 98:
 #   print( "cold")
#elif temp > 98:
#    print("hot")
#else:
 #   print("Normal")
    
#Q3. Find median of n Numbers using Math module Function and print the result
import statistics as stat
nums = {20,7,8,9,10}
print(stat.median(nums))
favorite_languages = {
'jen': 'HTML',
'sarah': 'c',
'edward': 'ruby',
'phil': 'C#',
}    
#Change the value from C# to Python for the key phil
# Add an item in the dictionary
# Remove an item from the dictionary
# List all the values in the dictionary

favorite_languages['phil']="Python"
favorite_languages['Sam']="c++"
del favorite_languages['edward']
print(favorite_languages)

filled_dict = {"one": 1, "two": 2, "three": 3}
filled_dict["one"]=100
filled_dict['four']=4
print(filled_dict)

#Q 6. Create a For loop to print 15 random numbers from 1 to 30
import random as ran

listOfNum ={}
for i in range(0,14,1) :
    listOfNum[i]=ran.randint(1, 30)
    print(listOfNum[i])
    i+=1
    
#Create a python dictionary called student. Include student name, age, subject, semester,
#grade and lab keys. Include the value for each key accordingly. Display keys separately and
#values separately in the print statement.

student = {'Name':'Tinky',
           'age': 18,
           'subject': 3408,
           'semester':'fall',
           'geade':'A+',
           'lab':6}

print('\n')
print('Key is: ')
for i in student.keys():
   print(i)
print('\n')
print('Value is: ')
for i in student.values():
   print(i)
   
 #Using Pandas library, produce the following output. Using pandas data frame organize the
#data into rows and columns

import pandas as pd
data={
'subject_id' : [1,2,3,4],
'Name':['Tinky','Chloe','Samuel','Ian'],
'course':[3408,'software','engineering','technician']
}

df=pd.DataFrame(data,index=[ 'Monday', 'Tuesday', 'Wednesday','Thursday'])
print(df)