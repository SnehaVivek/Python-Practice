# Matplot Library Practice notes

# To import the library as plt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# To make the background style 
plt.style.use('dark_background')


# Scatter Chart

# Defining the data 
rollno=[1,2,3,4,5,6,7,8,9,10]
marks =[20,34,56,78,94,6,34,65,84,47]

# Plot a simple scatter chart
plt.scatter(rollno,marks)
# to show the chart

# Change the color of the ploted points
plt.scatter(rollno,marks,color='green')

# Change the markers of the graphs like star, circles etc
plt.scatter(rollno,marks, marker='*')

# Two plots in same figue and to change the size of the graphs
plt.figure(figsize=(12,8))
plt.scatter(rollno,marks,color='green',marker='^')
plt.show()

# Multiple plots on same graph
# Data for mutliple
temperature_pune=[25,34,21,45,28,6,43,18,7,2]
humidity_pune=[28, 25,29,20, 26, 50, 19, 29, 52, 55]
temperature_bangalore = [34,35,36,37,28,27,26,25,31,20]
humidity_bangalore=[40, 38, 36, 35, 42, 44, 41, 40, 34, 45]

# Defining the axis to desirable
plt.xticks(np.arange(0,60,5))
plt.yticks(np.arange(10,60,5))

# Ploting both on same graphs and alpa is used for transpance
plt.plot(temperature_pune,humidity_pune,'ro')
plt.plot(temperature_bangalore,humidity_bangalore,'bo')

# Labels for the axis
plt.xlabel('Temperature')
plt.ylabel('Humidity')
plt.show()