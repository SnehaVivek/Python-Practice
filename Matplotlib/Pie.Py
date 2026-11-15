# Pie chart using matplotlib in python

# Import the libraries 
import matplotlib.pyplot as plt

# Dataset for the chart
classes=['Physics','Chemistry','Maths','Science','Computers']
marks=[78,98,70,89,97]

# plot the pie chart
plt.pie(marks, labels=classes)
plt.show()

# Change the color of the pie chart 
colour=['red','blue','green','#9803fc','#03c2fc']
plt.pie(marks,labels=classes,colors=colour)

# Percentage label on the pie chart
plt.pie(marks,labels=classes,autopct='%0.2f%%')

# Exploded/ pop out of pie chart 
values = [0.2,0,0,0,0]
plt.pie(marks,labels=classes,autopct='%0.2f%%',explode=values, shadow=True)
plt.show()

# Text and border of the pie chart
plt.figure(figsize=(8,8))
textprops={'fontsize':14,'color':'k'}
wedgeprops={'linewidth':3,'linestyle':'--','edgecolor':'white'}
plt.pie(marks,labels = classes,colors=colour,autopct='%0.1f%%',radius=1,textprops=textprops,wedgeprops=wedgeprops)
plt.title('Subjects and Average Scores')
plt.legend()
plt.show()

