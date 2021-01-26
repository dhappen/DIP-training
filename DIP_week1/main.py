import cv2
import os
import numpy as np
import math
import sys, time
from intensityTF import intensityTF
from affineTF import forwardaffineTF, inverseAffine

pi = math.pi
class colorTF:
    def __init__(self,img,type,output):
        self.img = img
        self.type = type
        self.output = output
    def TF(self):
        
        def RGB2HSI():
            img = self.img
            B = (img[:,:,0] / 255.0)
            G = (img[:,:,1] / 255.0)
            R = (img[:,:,2] / 255.0)

            S = 1.0 - 3.0 * np.minimum(R,np.minimum(B,G))/(R+G+B)
            I = (R+G+B) / 3.0
            
            sqrt1 = (2.0 * R - G - B)/2.0
            sqrt2 = np.sqrt((R - G) * (R - G) + (R - B) * (G - B))
            sqrt2_mask_zero = (sqrt2 == 0.0).astype(np.float64)
            sqrt2_mask_nonzero = (sqrt2 > 0.0).astype(np.float64)
            # cv2.imshow("sqrt2_mask_zero",sqrt2_mask_zero)
            # cv2.imshow("sqrt2_mask_nonzero",sqrt2_mask_nonzero)
            sqrt1 = sqrt1 * sqrt2_mask_nonzero
            sqrt2 = sqrt2 + sqrt2_mask_zero
            temp = (sqrt1/sqrt2)
            temp_mask1 = (temp <= 1).astype(np.float64)
            temp_mask2 = (temp >= -1).astype(np.float64)
            temp_mask = temp_mask1 * temp_mask2
            temp_mask_more = (temp > 1.0).astype(np.float64)
            temp_mask_less = (temp < -1.0).astype(np.float64)
            temp = temp * temp_mask + temp_mask_more + temp_mask_less
            theta = np.arccos(temp)
            smallBmask = (B <= G).astype(np.float64)
            bigBmask = (B > G).astype(np.float64)
            S = S.reshape((366,409,1))
            I = I.reshape((366,409,1))
            H1 = theta * smallBmask
            H2_temp = 2 * pi * bigBmask
            H2 = H2_temp.astype(np.float64) - theta * bigBmask
            H = ((H1 + H2)/(2*pi)).reshape((366,409,1))

            return np.concatenate([H,S,I],axis=2)
        def HSI2RGB():
            img = self.img
            H = (img[:,:,0]/255).astype(np.float64)
            S = (img[:,:,1]/255).astype(np.float64)
            I = (img[:,:,2]/255).astype(np.float64)
            H = H * 2 * pi
            H1 = (H < pi * 2 / 3).astype(np.float64)
            H21 = (pi * 2 / 3 <= H).astype(np.float64)
            H22 = (H < pi * 4/3).astype(np.float64)
            H2 = H21 * H22
            H3 = (pi * 4/3 <= H).astype(np.float64) 

            S1 = S * H1
            I1 = I * H1
            H1 = H * H1
            S2 = S * H2
            I2 = I * H2
            H2 = H * H2 - 2 * pi / 3
            S3 = S * H3
            I3 = I * H3
            H3 = H * H3 - 4 * pi / 3
            
            B1 = I1 * (1-S1)
            R1 = I1 * (1+S1*np.cos(H1)/np.cos(pi/3 - H1))
            G1 = 3 * I1 - (R1 + B1)

            R2 = I2 * (1 - S2)
            G2 = I2 * (1+S2*np.cos(H2)/np.cos(pi/3 - H2))
            B2 = 3 * I2 - (R2 + G2)

            G3 = I3 * (1 - S3)
            B3 = I3 * (1+S3*np.cos(H3)/np.cos(pi/3 - H3))
            R3 = 3 * I3 - (G3 + B3)

            B = B1 + B2 + B3
            G = G1 + G2 + G3
            R = R1 + R2 + R3
            B = (255 * B).reshape((366,409,1))
            G = (255 * G).reshape((366,409,1))
            R = (255 * R).reshape((366,409,1))
            fin = np.concatenate([B,G,R],axis=2)
        
            return fin.astype(np.uint8)

        if self.type == "RGB2HSI":
            newimg = RGB2HSI()
        elif self.type == "HSI2RGB":
            newimg = HSI2RGB()
        
        return newimg


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
x = color_img[:,:,0]
y = colorTF(color_img,"RGB2HSI",output).TF()
z = colorTF(y,"HSI2RGB",output).TF()

cv2.imshow('RGB2HSI',y)
cv2.imshow('HSI2RGB',z)
cv2.imshow('original_image',color_img)
cv2.imshow('H',y[:,:,0])
cv2.imshow('S',y[:,:,1])
cv2.imshow('I',y[:,:,2])
# cv2.imshow('negativeimg',neg_img)
if cv2.waitKey(0) == ord('q'):
    pass

cv2.destroyAllWindows()