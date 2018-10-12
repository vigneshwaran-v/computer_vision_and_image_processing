# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 17:13:03 2018

@author: Vicky
"""

import cv2
import numpy as np
import time
from PIL import Image 


l_dmap= cv2.imread('outputs\\left_depth_map_3x3.png', 0) 
l_dmap_9=cv2.imread('outputs\\left_depth_map_9x9.png', 0) 
l_dmap_c= cv2.imread('outputs\\left_consistency_3x3.png', 0) 
l_dmap_9_c=cv2.imread('outputs\\left_consistency_9x9.png', 0) 
l_dmap_gt=cv2.imread('outputs\\disp1.png',0)

r_dmap = cv2.imread('outputs\\right_depth_map_3x3.png', 0)
r_dmap_9 = cv2.imread('outputs\\right_depth_map_9x9.png', 0)
r_dmap_c = cv2.imread('outputs\\right_consistency_3x3.png', 0)
r_dmap_9_c = cv2.imread('outputs\\right_consistency_9x9.png', 0)
r_dmap_gt=cv2.imread('outputs\\disp5.png',0)


l_dmap=l_dmap.astype(float) 
l_dmap_c=l_dmap_c.astype(float)
l_dmap_9=l_dmap_9.astype(float)
l_dmap_9_c=l_dmap_9_c.astype(float)
l_dmap_gt=l_dmap_gt.astype(float)
  
r_dmap=r_dmap.astype(float)
r_dmap_c=r_dmap_c.astype(float)
r_dmap_9=r_dmap_9.astype(float)
r_dmap_9_c=r_dmap_9_c.astype(float) 
r_dmap_gt=r_dmap_gt.astype(float) 

N=l_dmap.shape[0]
M=l_dmap.shape[1]

ldsub=np.subtract(l_dmap,l_dmap_gt)
ldsquare=np.square(ldsub)
mse=np.mean(ldsquare)
print('left depth map 3x3 MSE= '+str(mse))

mse=np.mean(np.square(np.subtract(l_dmap_9,l_dmap_gt)))
print('left depth map 9x9 MSE= '+str(mse))


mse=np.mean(np.square(np.subtract(r_dmap,r_dmap_gt)))
print('right depth map 3x3 MSE= '+str(mse))

mse=np.mean(np.square(np.subtract(r_dmap_9,r_dmap_gt)))
print('right depth map 9x9 MSE= '+str(mse))


mean_den=N*M
mean_left_c_3=0
mean_right_c_3=0
mean_left_c_9=0
mean_right_c_9=0


for i in range(0,N):
    for j in range(0,M):
        if(int(l_dmap_c[i,j])==0):
           l_dmap_c[i,j]=np.nan
        if(int(l_dmap_9_c[i,j])==0):
           l_dmap_9_c[i,j]=np.nan
        if(int(r_dmap_c[i,j])==0):
            r_dmap_c[i,j]=np.nan
        if(int(r_dmap_9_c[i,j])==0):
            r_dmap_9_c[i,j]=np.nan

    
mse=np.nanmean(np.square(np.subtract(l_dmap_c,l_dmap_gt)))
print('left cosnistency depth map 3x3 MSE= '+str(mse))

mse=np.nanmean(np.square(np.subtract(l_dmap_9_c,l_dmap_gt)))
print('left cosnistency depth map 9x9 MSE= '+str(mse))


mse=np.nanmean(np.square(np.subtract(r_dmap_c,r_dmap_gt)))
print('right cosnistency depth map 3x3 MSE= '+str(mse))

mse=np.nanmean(np.square(np.subtract(r_dmap_9_c,r_dmap_gt)))
print('right cosnistency depth map 9x9 MSE= '+str(mse))









