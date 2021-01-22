import cv2
import os
import numpy as np
import math
from intensityTF import intensityTF

class forwardaffineTF:
    def __init__(self,img,output,imgname):
        self.img = img
        self.height = img.shape[0]
        self.width = img.shape[1]
        self.output = output
        self.imgname = imgname

    def TF(self,type,x,y):
        m = np.eye(3)
        v = np.array([1,1,1]).reshape(3,1)
        w = np.array([1,1,1]).reshape(3,1)
        if type == "zoom" or type == "shirink":
            m[0][0] = x
            m[1][1] = y

        elif type == "rotation":
            m[0][0] = np.cos(y * math.pi / 180)
            m[0][1] = -np.sin(y * math.pi / 180)
            m[1][0] = np.sin(y * math.pi / 180)
            m[1][1] = np.cos(y * math.pi / 180)
            m[0][2] = self.width/2 * (-np.cos(y * math.pi / 180)+1) + self.height/2 * np.sin(y * math.pi / 180)
            m[1][2] = self.width/2 * (-np.sin(y * math.pi / 180)) + self.height/2 * (-np.cos(y * math.pi / 180)+1)
        
        elif type == "trans":
            m[0][2] = x * np.cos(y)
            m[1][2] = x * np.sin(y)
        elif type == "shear":
            m[0][1] = y
            m[1][0] = x
        else:
            print("type이 잘 못 되었습니다.")
        
        # lx = self.width
        # ly = self.height
        v[0][0] = 0
        v[1][0] = 0
        w1 = np.dot(m,v)
        v[0][0] = self.width
        v[1][0] = 0        
        w2 = np.dot(m,v)
        v[0][0] = 0
        v[1][0] = self.height        
        w3 = np.dot(m,v)
        v[0][0] = self.width
        v[1][0] = self.height        
        w4 = np.dot(m,v)
        
        if type == "rotation":
            l = np.hstack([w1,w2,w3,w4])
            lx = np.max(l[0][0:]) - np.min(l[0][0:])
            ly = np.max(l[1][0:]) - np.min(l[1][0:])
            
            k = -int(np.min(l[0][0:]))
            j = -int(np.min(l[1][0:]))
            imgtf = np.zeros((int(ly),int(lx)))
            for yy in range(self.height):
                for xx in range(self.width):
                    v[0][0] = xx  
                    v[1][0] = yy
                    w = np.dot(m,v)
                    if 0<= w[1][0] + j < ly and 0<= w[0][0] + k < lx :
                        imgtf[int(w[1][0]+j)][int(w[0][0]+k)] = self.img[yy][xx]
        
        else:
            l7 = np.zeros((3,1))
            l = np.hstack([w1,w2,w3,w4,l7])
            lx = np.max(l[0][0:]) - np.min(l[0][0:])
            ly = np.max(l[1][0:]) - np.min(l[1][0:])
            imgtf = np.zeros((int(ly),int(lx)))
            for yy in range(self.height):
                for xx in range(self.width):
                    v[0][0] = xx  
                    v[1][0] = yy
                    w = np.dot(m,v).astype(np.int64)
                    imgtf[w[1][0]][w[0][0]] = self.img[yy][xx]
        
        cv2.imshow("affine",imgtf)
        cv2.imshow("affine_original",self.img)
        cv2.imwrite(self.output+'[{0}]forwardAffineTF.tif'.format(self.imgname),imgtf)

                


        


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
T = "Fig0236(a)(letter_T).tif"
# breast_img = cv2.imread(folder+breast,cv2.IMREAD_GRAYSCALE)
# fourier_img = cv2.imread(folder+fourier,cv2.IMREAD_GRAYSCALE)
# ramp_img = cv2.imread(folder+ramp,cv2.IMREAD_GRAYSCALE)
# MRI_img = cv2.imread(folder+MRI,cv2.IMREAD_GRAYSCALE)
Aerial_img = cv2.imread(folder+Aerial,cv2.IMREAD_GRAYSCALE)
contrast_img = cv2.imread(folder+contrast,cv2.IMREAD_GRAYSCALE)
kidney_img = cv2.imread(folder+kidney,cv2.IMREAD_GRAYSCALE)
dollor_img = cv2.imread(folder+dollor,cv2.IMREAD_GRAYSCALE)
T_img = cv2.imread(folder+T,cv2.IMREAD_GRAYSCALE)
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
forwardaffineTF(T_img, output, "T").TF("rotation",2,30)
# print(type(img[0][0]))
# print(type(neg_img[0][0]))
# cv2.imshow('image',img)
# cv2.imshow('negativeimg',neg_img)
if cv2.waitKey(0) == ord('q'):
    pass

cv2.destroyAllWindows()