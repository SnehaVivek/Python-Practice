# Image using matplotlib in python

# Import the matplotlib for image
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# Reading the image
img = mpimg.imread('C:/Users/HP/Downloads/UpGrad Python Practice/Matplotlib/Charts/Line Chart.png')
plt.imshow(img)
plt.show()


# Displaying multiple images in one single plot

# Images set used for the ploting dashboard
img1=mpimg.imread('C:/Users/HP/Downloads/UpGrad Python Practice/Matplotlib/Charts/Pie Chart.png')
img2=mpimg.imread('C:/Users/HP/Downloads/UpGrad Python Practice/Matplotlib/Charts/Horizontal bar graph.png')
img3=mpimg.imread('C:/Users/HP/Downloads/UpGrad Python Practice/Matplotlib/Charts/Scatter Chart.png')

# Ploting the dashboard
plt.figure()
plt.subplot(2,2,1)
plt.imshow(img)

plt.subplot(2,2,2)
plt.imshow(img1)

plt.subplot(2,2,3)
plt.imshow(img2)

plt.subplot(2,2,4)
plt.imshow(img3)

plt.show()

# Colorbar which mentions the colors that image is using
plt.imshow(img,aspect=1.5)
plt.colorbar()
plt.show()

# To change the colorbar into black and white
plt.imshow(img,cmap='gray')
plt.colorbar()
plt.show()