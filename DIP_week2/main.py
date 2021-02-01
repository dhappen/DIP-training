import cv2
import os
import numpy as np
import math
import sys, time

os.chdir("DIP_week2")
folder="picture/"
output="output/"

class convolution:
    def __init__(self,img,kernel,padding):
        self.img = img
        self.mask = kernel
        self.padding = padding
        self.height = img.shape[0]
        self.width = img.shape[1]

    def convolv(self):
        padded_img = np.zeros((self.height+2,self.width+2))
        if self.padding == "zero":
            pass
        elif self.padding == "mirror":
            padded_img[1:-1,0] = self.img[:,0]
            padded_img[1:-1,-2] = self.img[:,-2]
            padded_img[0,1:-1] = self.img[:,0]
            padded_img[-2,1:-1] = self.img[:,0]
            padded_img[0,0] = self.img[0,0]
            padded_img[0,-2] = self.img[0,-2]
            padded_img[-2,0] = self.img[-2,0]
            padded_img[-2,-2] = self.img[-2,-2]

        padded_img[1:-1,1:-1] = self.img
        output = np.zeros((self.height,self.width))
        kernel = np.flipud(np.fliplr(self.mask))

        for y in range(self.height):
            for x in range(self.width):
                output[y,x]= (kernel * padded_img[y:y+3,x:x+3]).sum()
        
        return output

class smooth(convolution):







if cv2.waitKey(0) == ord('q'):
    pass

cv2.destroyAllWindows()