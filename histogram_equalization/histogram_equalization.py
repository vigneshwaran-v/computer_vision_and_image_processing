# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 14:35:31 2018

@author: Vicky
"""

import numpy as np
import cv2 
import matplotlib.pyplot as plt
from PIL import Image


#loading the input image
source=cv2.imread("lena_gray.jpg",0)
image_matrix=cv2.imread("lena_gray.jpg",0)


N=image_matrix.shape[0]
M=image_matrix.shape[1]
enhanced_image=np.zeros(image_matrix.shape)

max_value=0

#finding out the maximum gray value in the input image
for i in range(0,N):
    for j in range(0,M):
        if image_matrix[i,j]>max_value:
            max_value=image_matrix[i][j]
            

        
#creating the histogram array
H=np.zeros(max_value+1)
H_E=np.zeros(max_value+1)

for i in range(0,N):
    for j in range(0,M):
        H[image_matrix[i][j]]+=1
        
#creating the cumulative histogram array
H_C=np.zeros(max_value+1)

H_C[0]=H[0]

for i in range(1,max_value+1):
    H_C[i]=H_C[i-1]+H[i]
    

#Pixel Transformation   
G=max_value+1
intermediate_value=(G-1)/(N*M)

T=np.zeros(max_value+1)

for i in range(1,max_value+1):
    T[i]=round(intermediate_value * H_C[i])

for i in range(0,N):
    for j in range(0,M):
        image_matrix[i][j]=T[image_matrix[i][j]]
        H_E[image_matrix[i][j]]+=1
        
#histogram - input image
plt.xlabel("Pixel intensity value")
plt.ylabel("Number of pixel")
plt.title("Histogram (input image)")
x=np.arange(max_value+1)
plt.bar(x,H,align='center')
plt.xticks(np.arange(0,max_value+1,25))
plt.show()

#cumulative histogram
plt.xlabel("Pixel intensity value")
plt.ylabel("Number of pixels")
plt.title("Cumulative Histogram")
x=np.arange(max_value+1)
plt.bar(x,H_C,align='center')
plt.xticks(np.arange(0,max_value+1,25))
plt.show()


#Transformation Function
plt.xlabel("Original Pixel Intensity value")
plt.ylabel("New Pixel Intensity value")
plt.title("Transformation Function")
plt.plot(T)
plt.show()

#histogram - equalized - output image
plt.xlabel("Pixel intensity value")
plt.ylabel("Number of pixels")
plt.title("Equalized_Histogram (output image)")
x=np.arange(max_value+1)
plt.bar(x,H_E,align='center')
plt.xticks(np.arange(0,max_value+1,25))
plt.show()

'''
gx=Image.fromarray(image_matrix)
if gx.mode!= 'RGB':
    gx=gx.convert('RGB')
gx.save('histogram_equalized_image.png')
'''

cv2.imshow('input_image',source)
cv2.imshow('enhanced_image',image_matrix)
cv2.waitKey(0)
cv2.destroyAllWindows()
