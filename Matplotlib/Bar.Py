# Bar Graphs using Matplotblib

# Import the libraries 
import matplotlib.pyplot as plt
import numpy as np

# Dataset for the bar graphs
subjects=['Maths','English','Science','Computers']
marks=[89,90,67,99]
marks2=[67,89,90,78]


# Vertical bar chart

# Plot the bar graphs 
plt.bar(subjects,marks)
plt.show()

# Change the color of the bars in the graphs
plt.bar(subjects,marks,color='green')
colour=['blue','green','red','yellow']
plt.bar(subjects,marks,color=colour)        # For mutilpe colors of the bar

# Width of the bar graphs
plt.bar(subjects,marks,width=0.3)

# Provide borders to the bars 
plt.bar(subjects,marks,edgecolor='white')

# Provide the border line width
plt.bar(subjects,marks,edgecolor='white',linewidth=3)


# Horizontal bar chart

# Ploting the horizontal bar chart
plt.figure(figsize=(8,8))
plt.xticks(np.arange(0,100,5))
plt.barh(subjects,marks,color=colour)
plt.xlabel('Marks')
plt.ylabel('Subjects')

# Mutiple chats in one
plt.figure(figsize=(6,6))
plt.xticks(np.arange(0,100,5))

# To avoid overlap of two bar charts 
subject_len=np.arange(len(subjects))
w=0.4

# Ploting the graphs without overlapping
plt.barh(subject_len,marks,color='red',height=0.4)       # For vertical it will be width
plt.barh(subject_len+w,marks2,color='blue',height=0.4)   # For horizontal it will be height
plt.xlabel('Marks')
plt.ylabel('Subjects')
plt.show()
