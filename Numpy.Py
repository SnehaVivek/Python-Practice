# Practice of Numpy module in Python

# To import the Numpy module
import numpy as np

# 1D Array in Numpy
print("1D Array")
a = np.array([1,2,3,4,5])
print(a)

# 2D Array in Numpy
print("2D Array")
b = np.array([[1,2,3],[4,5,6]])
print(b)

# 3D Array in Numpy
print("3D Array")
c = np.array([[[1,2,3],[4,5,7],[8,9,10]]])
print(c)

type(a)
type(b)
type(c)

# Number of elements in the array.
print(a.size)
print(b.size)
print(c.size)

# Shape of the array.
print(a.shape)
print(b.shape)
print(c.shape)

# Type of data present in the array.
print(a.dtype)
print(b.dtype)
print(c.dtype)

d = np.array ([[1,2.3,4.67],[4.6,7.98,2.34]])
print(d.dtype)

# Invert the rows and columns of the array.
print("Transpose of the arrays")
print(a.transpose())
print(b.transpose())
print(c.transpose())
print(d.transpose())


# Functions in Numpy

# Generate an array of random numbers with shape (4,4) and data type int.
x=np.empty((4,4), dtype=int)
print(x)

# Generate an array of ones with shape (3,3) and data type float.
y=np.ones((3))
z=np.ones((4,4))
print(y)
print(z)

# Generate an array of zeros with shape (2,2) and data type int.
w=np.zeros((2,2), dtype=int)
print(w)

# Generate array with series of numbers
e= np.arange(1,20)
print(e)

# Generate an array of numbers from 1 to 10 with a step size of 2.
f=np.arange(1,20,2)
print(f)

# Resaphe teh array to a new shape (2,5)
g=f.reshape(2,5)
print(g)

# Converts the 3d array to 1d array.
c=c.flatten()
print(c)
x=x.ravel()
print(x)

# Slicing an array
m=np.arange(1,51)
n=m.reshape(10,5)
print(n)

# Printing the first row
print(n[0])
# Print first element of the first row
print(n[0,0])
# Print element at 3 row and 4 column
print(n[2,3])
# Print from 2 to 4 rows
print(n[1:3])
# Printing all the rows and first 3 colums
print(n[:,2])
# Print certain rows and columns
print(n[0:3,1:4])
# Print all rows and all colums
print(n[:,:])

