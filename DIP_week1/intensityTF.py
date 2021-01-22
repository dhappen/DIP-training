import cv2
import numpy as np

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
        imgtf = np.zeros((8,self.height,self.width))
        for x in range(8):
            imgtf[x] = self.img & 2**x
            cv2.imshow('bitplane[{0}]'.format(x),imgtf[x])
            cv2.imwrite(self.output+'[{0}]IntensityTF_bitplane[{1}].jpg'.format(self.imgname,x),imgtf[x])

        cv2.imshow('bitplane_original',self.img)
        cv2.imwrite(self.output+'[{0}]IntensityTF_bitplane_original.tif'.format(self.imgname),self.img)
        print("bitplane complete")
