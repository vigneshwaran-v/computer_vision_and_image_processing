# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 03:38:53 2018

@author: Vicky
"""

import cv2
import numpy as np

l_dmap= cv2.imread('inputs\\left_depth_map_3x3.png', 0) 
r_dmap = cv2.imread('inputs\\right_depth_map_3x3.png', 0)
l_dmap_9= cv2.imread('inputs\\left_depth_map_9x9.png', 0) 
r_dmap_9 = cv2.imread('inputs\\right_depth_map_9x9.png', 0) 

l_dmap_c=cv2.imread('inputs\\left_depth_map_3x3.png', 0) 
r_dmap_c= cv2.imread('inputs\\right_depth_map_3x3.png', 0)
l_dmap_9_c= cv2.imread('inputs\\left_depth_map_9x9.png', 0) 
r_dmap_9_c= cv2.imread('inputs\\right_depth_map_9x9.png', 0)

N=l_dmap.shape[0]
M=l_dmap.shape[1]

for i in range(0,N):
    for j in range(0,M):
        left_disp=l_dmap[i,j]
        right_disp=r_dmap[i,j]
        left_disp_9=l_dmap_9[i,j]
        right_disp_9=r_dmap_9[i,j]
        if l_dmap[i,j]!=r_dmap[i,j-left_disp]:
            l_dmap_c[i,j]=0
        if r_dmap[i,j]!=l_dmap[i,j+right_disp]:
            r_dmap_c[i,j]=0
        if l_dmap_9[i,j]!=r_dmap_9[i,j-left_disp_9]:
            l_dmap_9_c[i,j]=0
        if r_dmap_9[i,j]!=l_dmap_9[i,j+right_disp_9]:
            r_dmap_9_c[i,j]=0
                     
cv2.imwrite('left_consistency_3x3.png',l_dmap_c) 
cv2.imwrite('right_consistency_3x3.png',r_dmap_c)
cv2.imwrite('left_consistency_9x9.png',l_dmap_9_c) 
cv2.imwrite('right_consistency_9x9.png',r_dmap_9_c)  

                   
l_dmap_c_view=l_dmap_c/255
r_dmap_c_view=r_dmap_c/255
l_dmap_9_c_view=l_dmap_9_c/255
r_dmap_9_c_view=r_dmap_9_c/255

cv2.imshow('left consistency check dmap',l_dmap_c_view)
cv2.imshow('right consistency check dmap',r_dmap_c_view)
cv2.imshow('left consistency check dmap 9x9',l_dmap_9_c_view)
cv2.imshow('right consistency check dmap 9x9',r_dmap_9_c_view)
cv2.waitKey(0)
cv2.destroyAllWindows()                

        

