# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 15:09:03 2018

@author: Vicky
"""

import cv2
import numpy as np

left_img = cv2.imread('inputs\\view1.png',0)  #read it as a grayscale image
right_img = cv2.imread('inputs\\view5.png',0)


#Disparity Computation for Left Image
dl=np.zeros(left_img.shape)
dr=np.zeros(right_img.shape)
OcclusionCost = 20 #(You can adjust this, depending on how much threshold you want to give for noise)


LR=left_img.shape[0]
LC=left_img.shape[1]

RR=right_img.shape[0]
RC=right_img.shape[1]


#For Dynamic Programming you have build a cost matrix. Its dimension will be numcols x numcols
#(This is important in Dynamic Programming. You need to know which direction you need traverse)
C = np.zeros([LC,LC])
M = np.zeros([LC,LC])
    
#We first populate the first row and column values of Cost Matrix
for i in range(0,LC):
    C[i][0]=i*OcclusionCost
    C[0][i]=i*OcclusionCost


# Now, its time to populate the whole Cost Matrix and DirectionMatrix
for r in range(0,LR):
    for i in range(1,LC):
        for j in range(1,LC):
            min1=C[i-1,j-1]+np.abs(int(left_img[r,i]-right_img[r,j]))
            min2=C[i-1,j]+OcclusionCost
            min3=C[i,j-1]+OcclusionCost
            cmin=np.min((min1,min2,min3))
            C[i,j]=cmin
            if min1==cmin:
                M[i,j]=1
            if min2==cmin:
                M[i,j]=2
            if min3==cmin:
                M[i,j]=3


# Use the pseudocode from "A Maximum likelihood Stereo Algorithm" paper given as reference
    p=LC-1
    q=LC-1



    while p!=0 and q!=0:
        if M[p,q]==1:
            dl[r,p] = np.abs(p-q)
            dr[r,q] = np.abs(p-q)
            p-=1
            q-=1
        elif M[p,q]==2:
            p-=1
        elif M[p,q]==3:
            q-=1


cv2.imwrite('dl_dp.jpg', dl)
cv2.imwrite('dr_dp.jpg', dr)




