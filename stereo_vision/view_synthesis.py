# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 03:39:25 2018

@author: Vicky
"""

import cv2
import numpy as np
from PIL import Image

left_img = cv2.imread('inputs\\view1.png') 
right_img = cv2.imread('inputs\\view5.png',1) 
left_depth_map=cv2.imread('inputs\\disp1.png',0) 
right_depth_map=cv2.imread('inputs\\disp5.png',0) 



synthesized_img=np.zeros(left_img.shape)


N=left_depth_map.shape[0]
M=left_depth_map.shape[1]


#print(left_depth_map[1,2])


for i in range(0,N):
    for j in range(0,M):
        disparity=left_depth_map[i,j]
        disparity=int(disparity/2)
        if (j-disparity)>0:
            synthesized_img[i,j-disparity]=left_img[i,j]
            synthesized_img[i,j-disparity,0]=left_img[i,j,0]
            synthesized_img[i,j-disparity,1]=left_img[i,j,1]
            synthesized_img[i,j-disparity,2]=left_img[i,j,2]
            
for i in range(0,N):
    for j in range(0,M):
        if synthesized_img[i,j,0]==0:
            disparity=right_depth_map[i,j]
            disparity_half=int(disparity/2)
            if(j-disparity_half)>0 and j<=(int(M/1.093)):
                synthesized_img[i,j]=right_img[i,j-disparity_half]
                synthesized_img[i,j,0]=right_img[i,j-disparity_half,0]
                synthesized_img[i,j,1]=right_img[i,j-disparity_half,1]
                synthesized_img[i,j,2]=right_img[i,j-disparity_half,2]
            elif (j-disparity)>0 and j>(int(M/1.093)):
                synthesized_img[i,j]=right_img[i,j-disparity]
                synthesized_img[i,j,0]=right_img[i,j-disparity,0]
                synthesized_img[i,j,1]=right_img[i,j-disparity,1]
                synthesized_img[i,j,2]=right_img[i,j-disparity,2]
                
            

synthesized_view=synthesized_img/255

#sysnthesized_save=synthesized_img.astype(np.uint8)
#sysnthesized_save=cv2.cvtColor(sysnthesized_save,cv2.COLOR_GRAY2BGR)
cv2.imwrite('synthesized_img.png',synthesized_img)
'''
gx=Image.fromarray(sysnthesized_save)
if gx.mode!= 'RGB':
    gx=gx.convert('RGB')
gx.save('synthesized_img.png')
'''
cv2.imshow('synthesized_view',synthesized_view)
#cv2.imshow('synthesized_view_color',synthesized_view)

cv2.waitKey(0)
cv2.destroyAllWindows()    

