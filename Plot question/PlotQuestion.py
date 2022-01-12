'''
PlotQuestion.py

See the README for the full description of the desired plot.


TOTAL POINTS AVAILABLE: 10 

10 points - desired plot is generated and code is efficient 

6-9 points - desired plot is generated, but code could be 
improved (e.g., the students used unnecessary if statements)

4-6 points - plot is generated but it has some errors

1-4 points - no plot is generated, but some effort was made to generate one

0 points - no effort made to answer question





'''
# Write a Python script that reads in the text file `data.txt`, in the folder Data, and generates 
# one plot as shown in image.png
# 
# Read the text file (hint: the delimiter in the 
# file is `','`) and notice that there are 9 columns. The first column represents the time of the 
# measurement, whereas the other columns represent data collected 
# at that specific time. To get maximum marks you need to be sure that the code you write can be executed on a computer different than yours (meaning, do not use
# absolute paths when opening and closing directories).
# 
# - Plot the data contained in the 6th column against the data contained in the 1st column (i.e., 
#   data in the 6th column on the y axis, data in the 1st column on the x axis). 
# - Plot the data contained in the 3rd column against the data contained in the 1st column (i.e., 
#   data in the 3rd column on the y axis, data in the 1st column on the x axis). 
# - Add an xlabel as "Time [s]" and a ylabel as "Speed [m/s]"
#

import matplotlib.pyplot as plt
import os
import numpy as np

# locating the Data file within the directory Plot Question
os.chdir("Plot question")
os.chdir("Data")

# opening the data.txt file
data_file = open("data.txt","r")

# readlines takes each line and converts it into a string
dataString = data_file.read()

data_file.close()

data_list = dataString.split()

dataArray = np.array(data_list)
dataArray = dataArray.reshape(10000,7)

first_column = []
sixth_column = []
third_column = []

for i in range(0,10000):

    first_column.append(float(dataArray[i][0]))

for j in range(0,10000):

    sixth_column.append(float(dataArray[j][5]))

for k in range(0,10000):

    third_column.append(float(dataArray[k][2]))

# plotting the arrays
plt.plot(first_column,sixth_column)

plt.plot(first_column,third_column)

# adding labels
plt.xlabel("Time [s]")
plt.ylabel("Speed [m/s]")

# displaying the graph
plt.show()



