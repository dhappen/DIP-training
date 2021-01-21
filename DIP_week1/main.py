import cv2
import os
import numpy as np
import math

class intensityTF:
    def __init__(self,img,output,imgname):
        self.img = img
        self.height = img.shape[0]
        self.width = img.shape[1]
        self.output = output
        self.imgname = imgname

    def negative(self):
        imgtf = 255 - self.img
        cv2.imshow('negativeimg',imgtf)
        cv2.imshow('negativeimg_original',self.img)
        cv2.imwrite(self.output+'IntensityTF_ImageNegative.tif',imgtf)
        cv2.imwrite(self.output+'IntensityTF_ImageNegative_original.tif',self.img)
        print("negativetransform complete")
    
    def logtransform(self):

        c = 1
        imgtf = c * np.log10(1+self.img).astype(np.uint8)
        cv2.imshow('logtransform',imgtf)
        cv2.imshow('logtransform_original',self.img)
        cv2.imwrite(self.output+'IntensityTF_logtransform.tif',imgtf)
        cv2.imwrite(self.output+'IntensityTF_logtransform_original.tif',self.img)
        print("logtransform complete")

    def gammatransform(self, r):
        c = 1
        imgtf = []
        for y in range(self.height):
            for x in range(self.width):
                k = self.img[y,x]
                s = c * 255 * ((k/255) ** r)
                imgtf.append(s)
        imgtf = np.array(imgtf)
        print(imgtf)
        imgtf = imgtf.reshape(self.height,self.width)
        imgtf = imgtf.astype(np.uint8)
        cv2.imshow('gammatransform',imgtf)
        cv2.imshow('gammatransform_original',self.img)
        cv2.imwrite(self.output+'[{0}]IntensityTF_gammatransform[{1}].tif'.format(self.imgname,r),imgtf)
        cv2.imwrite(self.output+'[{0}]IntensityTF_gammatransform_original.tif'.format(self.imgname),self.img)
        print("gammatransform complete")

    def contrast(self):
        imgtf = []
        intmax = np.max(self.img)
        intmin = np.min(self.img)
        for y in range(self.height):
            for x in range(self.width):
                k = self.img[y,x]
                s = 255 * k / (intmax - intmin) - 255 * intmin/ (intmax - intmin)
                imgtf.append(s)
        imgtf = np.array(imgtf)
        imgtf = imgtf.reshape(self.height,self.width)
        imgtf = imgtf.astype(np.uint8)
        cv2.imshow('contrast',imgtf)
        cv2.imshow('contrast_original',self.img)
        cv2.imwrite(self.output+'[{0}]IntensityTF_contrast.tif'.format(self.imgname),imgtf)
        cv2.imwrite(self.output+'[{0}]IntensityTF_contrast_original.tif'.format(self.imgname),self.img)
        print("contrast complete")

    def thresholding(self):
        imgtf = []
        mean = np.mean(self.img)
        for y in range(self.height):
            for x in range(self.width):
                k = self.img[y,x]
                if k >= mean:
                    s = 255
                else:
                    s = 0
                imgtf.append(s)
        imgtf = np.array(imgtf)
        imgtf = imgtf.reshape(self.height,self.width)
        imgtf = imgtf.astype(np.uint8)
        cv2.imshow('thresholding',imgtf)
        cv2.imshow('thresholding_original',self.img)
        cv2.imwrite(self.output+'[{0}]IntensityTF_thresholding.tif'.format(self.imgname),imgtf)
        cv2.imwrite(self.output+'[{0}]IntensityTF_thresholding_original.tif'.format(self.imgname),self.img)
        print("thresholding complete")

    def slicing(self):
        imgtf = []
        imgtf2 = []
        for y in range(self.height):
            for x in range(self.width):
                k = self.img[y,x]
                if 150<= k <= 230:
                    s = 230
                else:
                    s = 10
                imgtf.append(s)
        for y in range(self.height):
            for x in range(self.width):
                k = self.img[y,x]
                if 70<= k <= 140:
                    s = 0
                else:
                    s = k
                imgtf2.append(s)
        imgtf = np.array(imgtf)
        imgtf = imgtf.reshape(self.height,self.width)
        imgtf = imgtf.astype(np.uint8)
        imgtf2 = np.array(imgtf2)
        imgtf2 = imgtf2.reshape(self.height,self.width)
        imgtf2 = imgtf2.astype(np.uint8)
        cv2.imshow('slicing',imgtf)
        cv2.imshow('slicing2',imgtf2)
        cv2.imshow('slicing_original',self.img)
        cv2.imwrite(self.output+'[{0}]IntensityTF_slicing_a.tif'.format(self.imgname),imgtf)
        cv2.imwrite(self.output+'[{0}]IntensityTF_slicing_b.tif'.format(self.imgname),imgtf2)
        cv2.imwrite(self.output+'[{0}]IntensityTF_slicing_original.tif'.format(self.imgname),self.img)
        print("slicing complete")

    def bitplane(self):
        imgtf = np.array()
        mean = np.mean(self.img)
        # for x in range(8):
        #     imgtf[x] =  
        imgtf = np.array(imgtf)
        imgtf = imgtf.reshape(self.height,self.width)
        imgtf = imgtf.astype(np.uint8)
        cv2.imshow('bitplane',imgtf)
        cv2.imshow('bitplane_original',self.img)
        cv2.imwrite(self.output+'[{0}]IntensityTF_bitplane.tif'.format(self.imgname),imgtf)
        cv2.imwrite(self.output+'[{0}]IntensityTF_bitplane_original.tif'.format(self.imgname),self.img)
        print("bitplane complete")



folder="C:/Users/mmi-yonghyun/Desktop/DIP/DIP_week1/picture/"
output="C:/Users/mmi-yonghyun/Desktop/DIP/DIP_week1/output/"
breast = "Fig0304(a)(breast_digital_Xray).tif"
fourier = "Fig0305(a)(DFT_no_log).tif"
ramp = "Fig0307(a)(intensity_ramp).tif"
MRI = "Fig0308(a)(fractured_spine).tif"
Aerial = "Fig0309(a)(washed_out_aerial_image).tif"
contrast = "Fig0310(b)(washed_out_pollen_image).tif"
kidney = "Fig0312(a)(kidney).tif"
dollor = "Fig0314(a)(100-dollars).tif"
# breast_img = cv2.imread(folder+breast,cv2.IMREAD_GRAYSCALE)
# fourier_img = cv2.imread(folder+fourier,cv2.IMREAD_GRAYSCALE)
# ramp_img = cv2.imread(folder+ramp,cv2.IMREAD_GRAYSCALE)
# MRI_img = cv2.imread(folder+MRI,cv2.IMREAD_GRAYSCALE)
Aerial_img = cv2.imread(folder+Aerial,cv2.IMREAD_GRAYSCALE)
contrast_img = cv2.imread(folder+contrast,cv2.IMREAD_GRAYSCALE)
kidney_img = cv2.imread(folder+kidney,cv2.IMREAD_GRAYSCALE)
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
# print(type(img[0][0]))
# print(type(neg_img[0][0]))
# cv2.imshow('image',img)
# cv2.imshow('negativeimg',neg_img)
if cv2.waitKey(0) == ord('q'):
    pass

cv2.destroyAllWindows()