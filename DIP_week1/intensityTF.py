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
        
        # imgtf = (c * 255 * np.log10(1+self.img/255)).astype(np.uint8)
        # imgtf = (c * 255 * np.log10(1+self.img)).astype(np.uint8)
        imgtf = c * np.log10(1+self.img.astype(np.float64))
        print(np.max(imgtf))
        print(np.min(imgtf))
        imgtf = 255 * ((imgtf) / (np.max(imgtf)-np.min(imgtf)))
        imgtf = imgtf.astype(np.uint8)
        cv2.imshow('logtransform',imgtf)
        cv2.imshow('logtransform_original',self.img)
        cv2.imwrite(self.output+'IntensityTF_logtransform.tif',imgtf)
        cv2.imwrite(self.output+'IntensityTF_logtransform_original.tif',self.img)
        print("logtransform complete")

    def gammatransform(self, r):
        c = 1
        imgtf = []
        img = self.img
        img = (img / 255).astype(np.float64)
        imgtf = c * (img ** r)
        imgtf = 255 *((imgtf - np.min(imgtf))/(np.max(imgtf)-np.min(imgtf)) + np.min(imgtf))
        
        imgtf = imgtf.astype(np.uint8)
        cv2.imshow('[{0}]IntensityTF_gammatransform[{1}].tif'.format(self.imgname,r),imgtf)
        cv2.imshow('[{0}]IntensityTF_gammatransform_original.tif'.format(self.imgname),self.img)
        cv2.imwrite(self.output+'[{0}]IntensityTF_gammatransform[{1}].tif'.format(self.imgname,r),imgtf)
        cv2.imwrite(self.output+'[{0}]IntensityTF_gammatransform_original.tif'.format(self.imgname),self.img)
        print("gammatransform complete")

    def contrast(self,r1,r2):
        a = 0
        b = 255
        img = self.img
        img_mask1 = (img <= r2).astype(np.float64)
        img_mask2 = (img >= r1).astype(np.float64)
        img_mask = img_mask1 * img_mask2
        not_img_mask1 = 1 - img_mask1   # img > r2
        not_img_mask2 = 1 - img_mask2   # img < r1
        
        img_range = img_mask * img
        not_img_range1 = not_img_mask1 * img
        not_img_range2 = not_img_mask2 * img
        img_range = (img_range - r2) * (b - a) / (r2 - r1) + b
        not_img_range1 = (img_range - 255) * (255 - b) / (255 - r2) + 255
        not_img_range2 = a * not_img_range2 / r1
        imgtf = img_range + not_img_mask1 + not_img_mask2

        imgtf = imgtf.astype(np.uint8)
        cv2.imshow('contrast',imgtf)
        cv2.imshow('contrast_original',self.img)
        cv2.imwrite(self.output+'[{0}]IntensityTF_contrast.tif'.format(self.imgname),imgtf)
        cv2.imwrite(self.output+'[{0}]IntensityTF_contrast_original.tif'.format(self.imgname),self.img)
        print("contrast complete")

    def thresholding(self):
        img = self.img
        median = np.median(self.img)
        mean_mask = (img >= median).astype(np.uint8)
        
        imgtf = 255 * mean_mask
        cv2.imshow('thresholding',imgtf)
        cv2.imshow('thresholding_original',self.img)
        cv2.imwrite(self.output+'[{0}]IntensityTF_thresholding.tif'.format(self.imgname),imgtf)
        cv2.imwrite(self.output+'[{0}]IntensityTF_thresholding_original.tif'.format(self.imgname),self.img)
        print("thresholding complete")

    def slicing(self):
        img = self.img
        img_mask_a_1 = (img <= 230).astype(np.uint8) * (img >= 150).astype(np.uint8)
        img_mask_a_2 = 1 - img_mask_a_1
        img_a = 230 * img_mask_a_1 + 10 * img_mask_a_2

        img_mask_b_1 = (img <= 140).astype(np.uint8) * (img >= 70).astype(np.uint8)
        img_mask_b_2 = 1 - img_mask_b_1
        img_b = 0 * img_mask_b_1 + img * img_mask_b_2

        cv2.imshow('slicing',img_a)
        cv2.imshow('slicing2',img_b)
        cv2.imshow('slicing_original',self.img)
        cv2.imwrite(self.output+'[{0}]IntensityTF_slicing_a.tif'.format(self.imgname),img_a)
        cv2.imwrite(self.output+'[{0}]IntensityTF_slicing_b.tif'.format(self.imgname),img_b)
        cv2.imwrite(self.output+'[{0}]IntensityTF_slicing_original.tif'.format(self.imgname),self.img)
        print("slicing complete")

    def bitplane(self):
        imgtf = np.zeros((8,self.height,self.width))
        for x in range(8):
            imgtf[x] = self.img & 2**x
            cv2.imshow('bitplane[{0}]'.format(x),imgtf[x])
            cv2.imwrite(self.output+'[{0}]IntensityTF_bitplane[{1}].png'.format(self.imgname,x),imgtf[x])

        cv2.imshow('bitplane_original',self.img)
        cv2.imwrite(self.output+'[{0}]IntensityTF_bitplane_original.tif'.format(self.imgname),self.img)
        print("bitplane complete")
