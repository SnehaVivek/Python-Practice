# Hist chart using matplotlib 


# Import the libraries 
import matplotlib.pyplot as plt
import numpy as np 

# Background setup into dark
plt.style.use('dark_background')

# Dataset generate 
mark_50_students = np.random.randint(0,100,(50))
print(mark_50_students)
b = np.arange(0,100,5)

# Plot the histogram 
plt.hist(mark_50_students)
plt.show()

# Ploting with the figure size and axis size
plt.figure(figsize=(6,6))
plt.hist(mark_50_students,bins = b)
plt.xticks(np.arange(0,100,5))
plt.show()

# Change the color of the histogram
plt.hist(mark_50_students,bins=b,color='orange')
plt.xticks(np.arange(0,100,5))
plt.title('Marks of group of students')
plt.xlabel('Marks')
plt.ylabel('Number of students')
plt.show()

# Horizontal histogram chart
plt.hist(mark_50_students,color='red',orientation='horizontal')
plt.yticks(np.arange(0,100,5))
plt.show()

# Line histogram horizontal chart
plt.hist(mark_50_students,color='red',orientation='horizontal',histtype='step')
plt.yticks(np.arange(0,100,5))
plt.title('Horizontal marks distribution')
plt.xlabel('Number of students')
plt.ylabel('Marks')
plt.show()
