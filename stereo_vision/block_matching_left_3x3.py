# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 11:11:40 2018

@author: Vicky
"""


import cv2
import numpy as np
import time
from PIL import Image 

left_img = cv2.imread('inputs\\view1.png', 0) 
right_img = cv2.imread('inputs\\view5.png', 0)

left_depth_map=np.zeros(left_img.shape)
right_depth_map=np.zeros(right_img.shape)

left_img_padded=np.pad(left_img,1,mode='constant')
right_img_padded=np.pad(right_img,1,mode='constant')
left_img_padded=left_img_padded.astype(float)
right_img_padded=right_img_padded.astype(float)

N=left_img.shape[0]
M=left_img.shape[1]

match=0

start_time=time.time()
for i in range(1,N):
    for j in range(1,M):
        best_dist=10000000
        for k in range(1,j+1):
            dist=np.sum(np.square(np.subtract(left_img_padded[i-1:i+2,j-1:j+2],right_img_padded[i-1:i+2,k-1:k+2])))
            if(dist<best_dist): 
                disp_match=abs(j-k)
                if(disp_match<100):
                    best_dist=dist
                    match=k
        if match!=0:
            left_depth_map[i-1,j-1]=abs(j-match)
        else:
            left_depth_map[i-1,j-1]=0

end_time=time.time()
print("Execution time :"+ str(end_time-start_time) +" seconds")
print("start= "+str(start_time))  
print("end= "+str(end_time))             

left_dmap=left_depth_map/255

cv2.imshow('left disparity map',left_dmap)
cv2.waitKey(0)
cv2.destroyAllWindows()                

                
                

        
