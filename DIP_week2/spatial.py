import cv2
import os
import numpy as np
import math
import sys, time
pi = math.pi
class convolution:
    def __init__(self,img,size,padding):
        self.img = img
        self.size = size
        self.padding = padding
        self.height = img.shape[0]
        self.width = img.shape[1]

    def convolv(self,kernel):
        a = int(self.size / 2)
        padded_img = np.zeros((self.height+2*a,self.width+2*a))
        if self.padding == "zero":
            padded_img[a:-a,a:-a] = self.img
        elif self.padding == "replication":
            padded_img = np.pad(self.img,((a,a),(a,a)),'symmetric')
            # padded_img[1:-1,0] = self.img[:,0]
            # padded_img[1:-1,-2] = self.img[:,-2]
            # padded_img[0,1:-1] = self.img[:,0]
            # padded_img[-2,1:-1] = self.img[:,0]
            # padded_img[0,0] = self.img[0,0]
            # padded_img[0,-2] = self.img[0,-2]
            # padded_img[-2,0] = self.img[-2,0]
            # padded_img[-2,-2] = self.img[-2,-2]
        elif self.padding == "mirror":
            padded_img = np.pad(self.img,((a,a),(a,a)),'reflect')

        
        output = np.zeros((self.height,self.width))
        kernel = np.flipud(np.fliplr(kernel))

        for y in range(self.height):
            for x in range(self.width):
                output[y,x]= (kernel * padded_img[y:y+self.size,x:x+self.size]).sum()
                # if output[y,x] > 255:
                #     output[y,x]= 255
        
        return output

    def clip(self,img):
        img_over = (img > 255).astype(np.float64)
        img_under = (img < 0).astype(np.float64)
        img_clip = img - img_over * img - img_under * img
        img_over = 255 * img_over
        img_clip = img_clip + img_over
        return img_clip

    def norm(self,img):
        img_min = img.min()
        img_max = img.max()
        img_norm = 255 * (img - img_min)/(img_max - img_min)  

        return img_norm

class smoothing(convolution):
    def __init__(self,img , type, size, padding, name):
        convolution.__init__(self, img, size,padding)
        self.type = type

        self.name = name
        print("{0} smoothing 작업을 시작합니다.".format(self.type))

    
    def filter(self,sigma):
        start_time = time.time()
        output="output/smoothing"
        kernel = np.ones((self.size,self.size))
        if self.type == "box":
            kernel = kernel / (self.size * self.size)

        elif self.type == "gaussian":
            a = int(self.size / 2)
            
            xkernel = np.linspace(-a,a,self.size)
            ykernel = xkernel.reshape(self.size,1)
            xkernel = xkernel * kernel
            ykernel = ykernel * kernel

            kernel = -1 * (xkernel**2 + ykernel**2)/(2*sigma**2)
            kernel = np.exp(kernel)
            kernel = kernel / (2 * pi * sigma**2)
        else:
            print("filter가 잘못 설정되었습니다.")

        out = self.convolv(kernel)
        out = out.astype(np.uint8)
        cv2.imshow("[{0}]smoothoutput[{1}]original".format(self.name,self.type),self.img)
        cv2.imshow("[{0}]smoothoutput[{1}]".format(self.name,self.type),out)
        cv2.imwrite(output+"[{0}]smoothoutput[{1}][{3}]_({2}x{2}).tif".format(self.name,self.type,self.size,self.padding),out)

        print("{0} smoothing 작업 완료.".format(self.type))
        print("소요시간 : {0} sec".format(time.time()-start_time))

        return out

class sharpening(smoothing):
    def __init__(self,img , type, size, padding, name):
        self.type2 = type
        print("{0} sharpening 작업을 시작합니다.".format(self.type2))
        smoothing.__init__(self,img , "box", size, padding, name)     
        
        

    def laplacian(self):
        start_time = time.time()
        output="output/sharpening/"
        kernel = np.ones((self.size,self.size))
        a = int(self.size / 2)
        kernel = -1 * kernel
        kernel[a,a] = 8

        mask = self.convolv(kernel)
        img_sharp = self.img + mask
        '''clip'''
        mask_clip = self.clip(mask)

        img_sharp_clip = self.clip(img_sharp)
        ''''''
        '''normalization'''

        mask_norm = self.norm(mask)      
        ''''''
        mask = mask.astype(np.uint8)
        mask_clip = mask_clip.astype(np.uint8)
        mask_norm = mask_norm.astype(np.uint8)

        img_sharp_clip = img_sharp_clip.astype(np.uint8)
        cv2.imshow("[{0}]sharpoutput[{1}]original".format(self.name,self.type2),self.img)
        cv2.imshow("[{0}]sharpoutput[{1}]_maskclip".format(self.name,self.type2),mask_clip)
        cv2.imshow("[{0}]sharpoutput[{1}]_masknorm".format(self.name,self.type2),mask_norm)
        cv2.imshow("[{0}]sharpoutput[{1}]_img_sharp_clip".format(self.name,self.type2),img_sharp_clip)
        cv2.imwrite(output+"[{0}]sharpoutput[{1}][{2}]_maskclip.tif".format(self.name,self.type2,self.padding),mask_clip)
        cv2.imwrite(output+"[{0}]sharpoutput[{1}][{2}]_masknorm.tif".format(self.name,self.type2,self.padding),mask_norm)
        cv2.imwrite(output+"[{0}]sharpoutput[{1}][{2}]_img_sharp_clip.tif".format(self.name,self.type2,self.padding),img_sharp_clip)
        print("{0} sharpening 작업 완료.".format(self.type2))
        print("소요시간 : {0} sec".format(time.time()-start_time))

    def unsharp(self,k):
        start_time = time.time()
        output="output/sharpening/"
        blurred_img = self.filter(3)
        blurred_img = blurred_img.astype(np.float64)
        mask = self.img - blurred_img
        mask_clip = self.clip(mask)
        # mask_over = (mask > 255).astype(np.float64)
        # mask_under = (mask < 0).astype(np.float64)
        # mask_clip = mask - mask_over * mask - mask_under * mask
        # mask_over = 255 * mask_over
        # mask_clip = mask_clip + mask_over

        img_sharp = self.img + k * mask_clip
        img_sharp_clip = self.clip(img_sharp)

        img_sharp_clip = img_sharp_clip.astype(np.uint8)
        mask_clip = mask_clip.astype(np.uint8)
        cv2.imshow("[{0}]sharpoutput[{1}]original".format(self.name,self.type2),self.img)
        cv2.imshow("[{0}]sharpoutput[{1}][k={2}]_img_sharp".format(self.name,self.type2,k),img_sharp_clip)
        cv2.imshow("[{0}]sharpoutput[{1}][k={2}]_mask".format(self.name,self.type2,k),mask_clip)
        cv2.imwrite(output+"[{0}]sharpoutput[{1}][k={3}][{2}]_img_sharp.tif".format(self.name,self.type2,self.padding,k),img_sharp_clip)
        cv2.imwrite(output+"[{0}]sharpoutput[{1}][k={3}][{2}]_mask.tif".format(self.name,self.type2,self.padding,k),mask_clip)
        print("{0} sharpening 작업 완료.".format(self.type2))
        print("소요시간 : {0} sec".format(time.time()-start_time))


