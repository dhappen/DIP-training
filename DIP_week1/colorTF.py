import cv2
import os
import numpy as np
import math
import sys, time
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
            temp = temp * temp_mask + temp_mask_more - temp_mask_less
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
            H = (img[:,:,0]).astype(np.float64)
            S = (img[:,:,1]).astype(np.float64)
            I = (img[:,:,2]).astype(np.float64)
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
            cv2.imshow(self.out + "[{0}color]".format(self.type),newimg)
            cv2.imshow(self.out + "[{0}color_[H]".format(self.type),newimg[:,:,0])
            cv2.imshow(self.out + "[{0}color_[S]".format(self.type),newimg[:,:,1])
            cv2.imshow(self.out + "[{0}color_[I]".format(self.type),newimg[:,:,2])
            cv2.imwrite(self.out + "[{0}color.tif]".format(self.type),newimg)
            cv2.imwrite(self.out + "[{0}color_[H].tif".format(self.type),newimg[:,:,0])
            cv2.imwrite(self.out + "[{0}color_[S].tif".format(self.type),newimg[:,:,1])
            cv2.imwrite(self.out + "[{0}color_[I].tif".format(self.type),newimg[:,:,2])
        elif self.type == "HSI2RGB":
            newimg = HSI2RGB()
            cv2.imshow(self.out + "[{0}color]".format(self.type),newimg)
            cv2.imshow(self.out + "[{0}color_[B]".format(self.type),newimg[:,:,0])
            cv2.imshow(self.out + "[{0}color_[G]".format(self.type),newimg[:,:,1])
            cv2.imshow(self.out + "[{0}color_[R]".format(self.type),newimg[:,:,2])            
            cv2.imwrite(self.out + "[{0}color.tif]".format(self.type),newimg)
            cv2.imwrite(self.out + "[{0}color_[B].tif".format(self.type),newimg[:,:,0])
            cv2.imwrite(self.out + "[{0}color_[G].tif".format(self.type),newimg[:,:,1])
            cv2.imwrite(self.out + "[{0}color_[R].tif".format(self.type),newimg[:,:,2])
        
        return newimg