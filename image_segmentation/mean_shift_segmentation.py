# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 00:58:37 2018

@author: Vicky
"""
import cv2
import numpy as np
import random

input_image=cv2.imread('Images\\Butterfly.jpg')
input_image_x=input_image.shape[0]
input_image_y=input_image.shape[1]
N=input_image_x*input_image_y
M=5
F=np.zeros((N,M))
segmented_img=np.zeros(input_image.shape)

counter=0

for i in range(0,input_image_x):
    for j in range(0,input_image_y):
        F[counter][0]=input_image[i,j,0]
        F[counter][1]=input_image[i,j,1]
        F[counter][2]=input_image[i,j,2]
        F[counter][3]=i
        F[counter][4]=j
        counter+=1
        
h=30
iter=20
mean_vector_shift=0
labeled_pixels=[]


while len(labeled_pixels)<N:
    print('labeled pixel length='+str(len(labeled_pixels)))
    if mean_vector_shift!=1:
        initial_mode=random.randint(0,N-1)
        #cc=0
        while(initial_mode in labeled_pixels):
            #print("while"+str(cc))
            initial_mode=random.randint(0,N-1)
            #cc+=1
        mode_r=F[initial_mode][0]
        mode_g=F[initial_mode][1]
        mode_b=F[initial_mode][2]
        mode_x=F[initial_mode][3]
        mode_y=F[initial_mode][4]
            
    
    cluster=[]
    
    for i in range(0,N):
        dist=np.sqrt(((mode_r-F[i][0])**2)+((mode_g-F[i][1])**2)+((mode_b-F[i][2])**2)+((mode_x-F[i][3])**2)+((mode_y-F[i][4])**2))
        if dist<h:
            cluster.append(i)
                
    avg_r=0
    avg_g=0
    avg_b=0
    avg_x=0
    avg_y=0
        
    for i in range(0,len(cluster)):
        avg_r+=F[cluster[i]][0]
        avg_g+=F[cluster[i]][1]
        avg_b+=F[cluster[i]][2]
        avg_x+=F[cluster[i]][3]
        avg_y+=F[cluster[i]][4]
        
    if(len(cluster)>0):
        new_mean_r=int(avg_r/len(cluster))
        new_mean_g=int(avg_g/len(cluster))
        new_mean_b=int(avg_b/len(cluster))
        new_mean_x=int(avg_x/len(cluster))
        new_mean_y=int(avg_y/len(cluster))
    
    
        mean_shift=np.sqrt((new_mean_r-mode_r)**2+(new_mean_g-mode_g)**2+(new_mean_b-mode_b)**2+(new_mean_x-mode_x)**2+(new_mean_y-mode_y)**2)
        print("mean_shift="+str(mean_shift))
        if(mean_shift<iter):
            for i in range(0,len(cluster)):
                    x=int(F[cluster[i]][3])
                    y=int(F[cluster[i]][4])
                    segmented_img[x,y,0] = new_mean_r
                    segmented_img[x,y,1] = new_mean_g
                    segmented_img[x,y,2] = new_mean_b
                    mean_vector_shift=0
                    labeled_pixels.append(cluster[i])
                    #print(len(labeled_pixels))
        
        else:
            mean_vector_shift=1
            mode_r=F[new_mean_r][0]
            mode_g=F[new_mean_g][1]
            mode_b=F[new_mean_b][2]
            mode_x=F[new_mean_x][3]
            mode_y=F[new_mean_y][4]
            
    

  
cv2.imwrite('segmented_img_MS.png',segmented_img)
segmented_view=segmented_img/255
cv2.imshow('segmented img',segmented_view)
cv2.waitKey(0)
cv2.destroyAllWindows()    
