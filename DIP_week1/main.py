import cv2
import os
import numpy as np
import math
import sys, time
from intensityTF import intensityTF
from affineTF import forwardaffineTF, inverseAffine
from colorTF import colorTF

pi = math.pi

os.chdir("DIP_week1")    ##학교 컴퓨터일때
folder="picture/"
output="output/"
breast = "Fig0304(a)(breast_digital_Xray).tif"
fourier = "Fig0305(a)(DFT_no_log).tif"
ramp = "Fig0307(a)(intensity_ramp).tif"
MRI = "Fig0308(a)(fractured_spine).tif"
Aerial = "Fig0309(a)(washed_out_aerial_image).tif"
contrast = "Fig0310(b)(washed_out_pollen_image).tif"
kidney = "Fig0312(a)(kidney).tif"
dollor = "Fig0314(a)(100-dollars).tif"
T = "Fig0236(a)(letter_T).tif"
watch = "Fig0220(a)(chronometer 3692x2812  2pt25 inch 1250 dpi).tif"
color = "Fig0608(RGB-full-color-cube).tif"
# breast_img = cv2.imread(folder+breast,cv2.IMREAD_GRAYSCALE)
fourier_img = cv2.imread(folder+fourier,cv2.IMREAD_GRAYSCALE)
# ramp_img = cv2.imread(folder+ramp,cv2.IMREAD_GRAYSCALE)
# MRI_img = cv2.imread(folder+MRI,cv2.IMREAD_GRAYSCALE)
Aerial_img = cv2.imread(folder+Aerial,cv2.IMREAD_GRAYSCALE)
contrast_img = cv2.imread(folder+contrast,cv2.IMREAD_GRAYSCALE)
kidney_img = cv2.imread(folder+kidney,cv2.IMREAD_GRAYSCALE)
dollor_img = cv2.imread(folder+dollor,cv2.IMREAD_GRAYSCALE)
T_img = cv2.imread(folder+T,cv2.IMREAD_GRAYSCALE)
watch_img = cv2.imread(folder+watch,cv2.IMREAD_GRAYSCALE)
color_img = cv2.imread(folder+color,cv2.IMREAD_COLOR)
# intensityTF(breast_img,output,"breast").negative()
# intensityTF(fourier_img,output,"fourier").logtransform()
# intensityTF(ramp_img,output,"ramp").gammatransform(2.5)
# intensityTF(MRI_img,output,"MRI").gammatransform(0.6)
# intensityTF(MRI_img,output,"MRI").gammatransform(0.4)
# intensityTF(MRI_img,output,"MRI").gammatransform(0.3)
# intensityTF(Aerial_img,output,"Aerial").gammatransform(3)
# intensityTF(Aerial_img,output,"Aerial").gammatransform(4)
# intensityTF(Aerial_img,output,"Aerial").gammatransform(5)
# intensityTF(contrast_img,output,"contrast").contrast()
# intensityTF(contrast_img,output,"thresholding").thresholding()
# intensityTF(kidney_img,output,"slicing").slicing()
# intensityTF(dollor_img,output,"dollor").bitplane()
# forwardaffineTF(T_img, output, "T").TF("rotation",2,30)
# inverseAffine(Aerial_img,output,"Aerial","nearest").affine("rotation",2,2,30)
# inverseAffine(T_img,output,"T","bicubic").affine("rotation",2,1.5,30)
# inverseAffine(T_img,output,"T","bilinear").affine("rotation",2,1.5,30)
# # inverseAffine(T_img,output,"T","nearest").affine("rotation",2,1.5,30)
# inverseAffine(watch_img,output,"watch","bicubic").affine("zoom",1.2,1.2,30)
# inverseAffine(watch_img,output,"watch","bilinear").affine("zoom",1.2,1.2,30)
# inverseAffine(watch_img,output,"watch","nearest").affine("zoom",1.2,1.2,30)

'''nearest or bilinear or bicubic '''
# print(type(img[0][0]))
# print(type(neg_img[0][0]))
'''color transform'''
x = color_img[:,:,0]
y = colorTF(color_img,"RGB2HSI",output).TF()
z = colorTF(y,"HSI2RGB",output).TF()
cv2.imshow('original_image',color_img)

# cv2.imshow('negativeimg',neg_img)
if cv2.waitKey(0) == ord('q'):
    pass

cv2.destroyAllWindows()