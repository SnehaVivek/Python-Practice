# Line graphs using matplotlib practice notes

# Import the libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Background color of the graphs 
plt.style.use('dark_background')

# Linear dataset for the line graph
rollno = [1,2,3,4,5,6,7]
marks=[10,20,30,40,50,60,70]

# Graphs the line plot
plt.plot(rollno,marks,'r-')
plt.show()

# Line style examples dot, dash etc
plt.plot(rollno,marks, linestyle='-')

# Color of the line 
plt.plot(rollno,marks,linestyle='--',color='#728569')
plt.show()

# Multiple plots on same figure
study_hours =[2,3,4,5,6,7,8]
marks =[10,39,57,89,46,37,89]

# Size of the graph
plt.figure(figsize=(8,8))
plt.xticks(np.arange(0,15,1))
plt.yticks(np.arange(0,100,5))

# Graph for mutliple plots
plt.plot(study_hours,marks,'r-')
plt.plot(rollno,marks,'r-', color='#728569')

# Label of the axis
plt.xlabel('Study hours')
plt.ylabel('Marks')
plt.show()

