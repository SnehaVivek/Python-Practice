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

# Ploting the Dist Plot
sns.displot(data=sample_df,x='Roll_no',y='Marks')
plt.title('student marks')
plt.show()
