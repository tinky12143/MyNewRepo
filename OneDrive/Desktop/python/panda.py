# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 21:58:20 2021

@author: Centennial
"""

import pandas as pd

data = {
    'Scrum meeting Hours': [3, 2, 1, 1], 
    'Client meeting hours ': [0, 3, 0, 2]
}
meeting_hours = pd.DataFrame(data)
print(meeting_hours)
print('\n****************************************************')

meeting_hours = pd.DataFrame(data, index=[ 'Monday', 'Tuesday', 'Wednesday','Thursday'])
print(meeting_hours)
print('\n****************************************************')

wed = meeting_hours.loc['Wednesday']
print(wed)
print('\n****************************************************')
total_hours=meeting_hours.sum()
print(total_hours)
print('\n****************************************************')
import os 
print(os.getcwd()) 
print('\n****************************************************')
curDir = os.getcwd()
print(curDir)
print('\n****************************************************')
print(os.name)
print('\n****************************************************')
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
print('\n****************************************************')
print('Text: %r' % 'Hello') 
print('Text: %s' % 'Hello')

