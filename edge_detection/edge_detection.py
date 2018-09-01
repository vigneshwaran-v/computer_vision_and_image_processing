# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 03:43:24 2018

@author: Vicky
"""

import numpy as np
import cv2 
import time

source=cv2.imread("lena_gray.jpg",0)
image_matrix=np.asarray(source)
image_padded=np.pad(image_matrix,1,mode='constant')

#creating sobel filters
sobel_filter_x=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
sobel_filter_y=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])

sobel_filter_x_1=np.array([[1],[2],[1]])
sobel_filter_x_2=np.array([[-1,0,1]])

sobel_filter_y_1=np.array([[-1],[0],[1]])
sobel_filter_y_2=np.array([[1,2,1]])

#2d convolution function
def convolution_2d(image,filter):
    image_height=image.shape[0]
    image_width=image.shape[1]
    filter_height=filter.shape[0]
    filter_width=filter.shape[1]
    tmp=np.zeros([image_height-filter_height+1,image_width-filter_width+1])
    offset_i=int((filter_height-1)/2)
    offset_j=int((filter_width-1)/2)
    for i in range(offset_i,image_height-offset_i):
        for j in range(offset_j,image_width-offset_j):
            tmp[i-offset_i,j-offset_j]=np.sum(np.multiply(filter,image[i-offset_i:i+offset_i+1,j-offset_j:j+offset_j+1]))
    return tmp

#1d convolution function
def convolution_1d(image,filter1,filter2):
    image_height=image.shape[0]
    image_width=image.shape[1]
    filter1_height=filter1.shape[0]
    filter2_width=filter2.shape[1]
    offset_i=int((filter1_height-1)/2)
    offset_j=int((filter2_width-1)/2)
    tmp_mat=np.zeros(image.shape)
    tmp=np.zeros([image_height-filter1_height+1,image_width-filter2_width+1])
    for i in range(offset_i,image_height-offset_i):
        for j in range(offset_j,image_width-offset_j):
            tmp_mat[i,j]=np.sum(np.multiply(filter1,image[i-offset_i:i+offset_i+1,j:j+1]))
    for i in range(offset_i,image_height-offset_i):
        for j in range(offset_j,image_width-offset_j):
            tmp[i-offset_i,j-offset_j]=np.sum(np.multiply(filter2,tmp_mat[i:i+1,j-offset_j:j+offset_j+1]))
    return tmp


#performing 2d convolution
start_time_2d=time.time()
g_x_2d=convolution_2d(image_padded,sobel_filter_x)
g_y_2d=convolution_2d(image_padded,sobel_filter_y)
g_2d=np.sqrt(g_x_2d*g_x_2d+g_y_2d*g_y_2d)
end_time_2d=time.time()
print("Execution time for 2d convolution: "+ str(end_time_2d-start_time_2d) +" seconds")


#performing 1d convolution
start_time_1d=time.time()
g_x_1d=convolution_1d(image_padded,sobel_filter_x_1,sobel_filter_x_2)
g_y_1d=convolution_1d(image_padded,sobel_filter_y_1,sobel_filter_y_2)
g_1d=np.sqrt(g_x_1d*g_x_1d+g_y_1d*g_y_1d)
end_time_1d=time.time()
print("Execution time for 1d convolution: "+ str(end_time_1d-start_time_1d) +" seconds")

g_x_2d=g_x_2d/255
g_y_2d=g_y_2d/255
g_2d=g_2d/255
g_x_1d=g_x_1d/255
g_y_1d=g_y_1d/255
g_1d=g_1d/255


#displaying the convolution outputs
cv2.imshow('Gx_2d',g_x_2d)
cv2.imshow('Gy_2d',g_y_2d)
cv2.imshow('G_2d',g_2d)
cv2.imshow('Gx_1d',g_x_1d)
cv2.imshow('Gy_1d',g_y_1d)
cv2.imshow('G_1d',g_1d)
cv2.waitKey(0)
cv2.destroyAllWindows()