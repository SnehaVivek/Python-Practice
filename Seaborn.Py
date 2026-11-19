# Seaborn Problem solving

# Import the seaborn library
import seaborn as sns
# Other libraries 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Dataset for the ploting
roll=[1,2,3,4,5,6,7,8,9,10]
marks=[46,57,89,64,74,83,93,65,46,57]

# Converting to DataFrame
sample_df = pd.DataFrame({"Roll_no":roll,"Marks":marks})
sample_df.head()

# Ploting the Line graph
sns.lineplot(data =sample_df,x='Roll_no',y='Marks' )
plt.title('Student Marks')

# Hue = 'Department' is use to segrate the requirment
# Style = 'Department' is use to group the department
# Legend =False will allow to remove the legend colum from the chart
# Pallete = 'Blue' change the line graph color into blue shades
# Alpha = 0.5 for the transperancy of the chart 

# Ploting the Dist Plot
sns.displot(data=sample_df,x='Roll_no',y='Marks')
plt.title('student marks')
plt.show()

# Plotting the Scatter plot
sns.scatterplot(x='Roll_no',y='Marks',data=sample_df)
plt.title('Student marks scatter chart')
plt.show()

# Plotting the bar plot 
sns.barplot(x='Roll_no',y='Marks',data=sample_df)
plt.title('Student marks')
plt.show()

# Ploting the heatmaps
# Dataset for the heatmap
map=pd.read_csv(f'C:/Users/HP/Downloads/UpGrad Python Practice/Datasets/hr_data.csv')
print(map.head())
# Plotting the heatmaps using the dataset
map_load = map.pivot_table(
    index='department',
    columns='number_project',
    values='average_montly_hours',
    aggfunc='mean'
)
print(map.head())
sns.heatmap(map_load, annot=True, cmap='coolwarm', fmt='.1f')
plt.title('Average no. of hours spend for each project by deparments')
plt.show()