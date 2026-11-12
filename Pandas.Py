# Pandas library in Python for data analysis and manipulation

# To import the Pandas module
import pandas as pd


# Types of series

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

# DataFrames using Pandas
b1 = [1,2,3,4,5,6]
df1 = pd.DataFrame(b1)
print(df1)

# Muti-dimensional DataFrames
b2 = [[1,2,3,4],[5,6,6,7]]
df2= pd.DataFrame(b2)
print(df2)

# Data Frames using Dictionary
b3=[{'a':1,'b':2,'c':4},{'a':3,'b':6,'c':7}]
df3=pd.DataFrame(b3)
print(df3)


# Importing excel csv file and reading the dataset

# Reading CSV 
df4=pd.read_csv(r'C:\Users\HP\Downloads\UpGrad Python Practice\IMDb+movies+Data+and+ERD+final(names).csv', encoding="latin1")

# Only the columns from the data file
print(df4.columns)

# Number of cells in the csv file
print(df4.size)

# Numbers of rows and columns
print(df4.shape)

# First five rows in the csv file
print(df4.head())  # First 5 rows by default
print(df4.head(2))  # First 2 rows

# Last rows in the csv file
print(df4.tail())  # Last 5 rows by default
print(df4.tail(3)) # Last 3 rows

# Description of the numerical data of the csv file
print(df4.describe())

# Basic information of the csv file data
print(df4.info())


# Handling null values and missing values from the dataset

# Dataset for the Null values
o=pd.read_csv(r'C:\Users\HP\Downloads\UpGrad Python Practice\Missing and Null values.csv')
print(o.head())

# Check the data having null values
print(o.isnull())

# Number of null values in the dataset
print(o.isnull().sum())

# Drop the rows which consist of null values
print(o.shape)
o1=o.dropna()     # drop rows by default
print(o1.shape)   # How many rows dropped

# Dropping the columns with null values
o2=o.dropna(axis=1)
print(o2.shape)

# If all the row values in null than drop
o3=o.dropna(how='all')

# To replace the null values from the dataset permanently
o4=o.dropna(inplace = True)
print(o4)

