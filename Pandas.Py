# Pandas library in Python for data analysis and manipulation

# To import the Pandas module
import pandas as pd

# Panda Series with Python Lists
a1=[1,2,3,4,5,6,7]
print(a1)
b = pd.Series(a1)
print(b)
print(type(b))

# Series with Indexing
a2 = pd.Series(['p','y','t','h','o','n'], index = [1,2,3,4,5,6])
print(a2)

# Providing Index Lables 
a3 = pd.Series(['p','y','t','h','e','w'], index = [10,11,12,13,14,15], name = 'alphabets')
print(a3)

# Scalar series with indexing
a4= pd.Series(0.5, index = [1,2,3])
print(a4)

# Pandas series with dictionary
a5 = pd.Series({'p':1,'q':2,'r':3,'s':4})
print(a5)


# Maximum value from the series
print(max(a5))

# Matrix style and mutilpe colums series
a6 = pd.Series({'p':[1,2,3],'q':[5,6,7],'r':[10,23,57],'s':[45,2,7]})
print(a6)