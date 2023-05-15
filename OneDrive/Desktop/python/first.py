# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


name ="Tai bin"
age=87
height=160.5
is_happy=True
is_fat=False

print("Hello \n"+name)

phase = "Hello"
print(phase.upper().isupper())
print(phase[0])
print(phase.index("o"))
print(phase.replace("H","o"))


print(8//3)
print(8%3)
number = 8
print(str(number))
print(pow(2,4))
print(max(7,5,67,333))
print(round(4.4))


answer1=input("What is your name: ")
print("hello "+answer1)
#float()

scores=[100,20,80]
friends=["taibe","bowie"]
things=["happy",90,True]
print(scores[-1])
print(scores[0:1])
scores[0] = 40
print(scores)

scores.extend(friends)
print(scores)
scores.append(30)
print(scores)
scores.insert(2,30)
print(scores)
scores.remove(20)
scores.clear()
scores.pop()
scores.sort()
scores.reverse()
print(scores.index(90))
print(scores.count(80))


