import cv2
import os
import numpy as np
import math
# from intensityTF import intensityTF

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
# class interpolation:
#     def __init__(self,int_type,img):
#         self.int_type = int_type
#         self.img = img
#     def excute(self,pixel):
#         p = 0
#         if self.int_type == "nearest":
#             if pixel >= 0:
#                 p = self.img(pixel(1, 0), pixel(0, 0))
#             else:
#                 p = 0
#         elif self.int_type == "bilinear":
#             if pixel >= 0:
#                 p = self.img(pixel(1, 0), pixel(0, 0))
#             else:
#                 p = 0
#
#         elif self.int_type == "bicubic":
#             if pixel >= 0:
#                 p = self.img(pixel(1, 0), pixel(0, 0))
#             else:
#                 p = 0
#
#         return p

class inverseAffine:
    def __init__(self,img,output,imgname,int_type):
        self.img = img
        self.output = output
        self.imgname = imgname
        self.height = img.shape[0]
        self.width = img.shape[1]
        self.int_type = int_type
    def affine(self,type,k,j,theta):
        def interpolation(type,img,pixel):
            cubicmat = np.array([0,2,0,0,-1,0,1,0,2,-5,4,-1,-1,3,-3,1]).reshape((4,4))
            def linear(i1,i2,kpixel):
                m = int(kpixel)
                return i1 * (m+1-kpixel) + i2 * (kpixel - m)
            def cubic(i1,i2,i3,i4,kpixel):
                m = kpixel - int(kpixel)
                t = np.array([1,m,m*m,m*m*m],dtype=np.float64)
                f = np.array([i1,i2,i3,i4]).reshape((4,1))
                tm = np.dot(t,cubicmat)
                pt = np.dot(tm,f)
                return pt/2
            p = 0

            kx = pixel[0][0]
            ky = pixel[1][0]
            a = int(kx)
            b = int(ky)

            if type == "nearest":
                if (0<=pixel).all and a < img.shape[1]-1 and b < img.shape[0]-1:
                    p = img[int(ky+0.5)][int(kx+0.5)]
                else:
                    p = 0
            elif type == "bilinear":
                if (0<=pixel).all and a < img.shape[1]-1 and b < img.shape[0]-1:
                    x1 = linear(img[b][a],img[b][a+1],kx)
                    x2 = linear(img[b+1][a],img[b+1][a+1],kx)
                    y = linear(x1,x2,ky)
                    p = y
                else:
                    p = 0
            elif type == "bicubic":
                if (0<pixel).all and a < img.shape[1]-2 and b < img.shape[0]-2:
                    b1 = cubic(img[b-1][a-1],img[b-1][a],img[b-1][a+1],img[b-1][a+2],kx)
                    b2 = cubic(img[b][a-1],img[b][a],img[b][a+1],img[b][a+2],kx)
                    b3 = cubic(img[b+1][a-1],img[b+1][a],img[b+1][a+1],img[b+1][a+2],kx)
                    b4 = cubic(img[b+2][a-1],img[b+2][a],img[b+2][a+1],img[b+2][a+2],kx)
                    p = int(cubic(b1,b2,b3,b4,ky))

                else:
                    p = 0
            return p

        a = self.width / 2
        b = self.height / 2
        m = np.eye(3)
        v = np.array([1, 1, 1]).reshape(3, 1)
        w = np.array([1, 1, 1]).reshape(3, 1)
        if type == "zoom" or type == "shirink":
            m[0][0] = 1/k
            m[1][1] = 1/j

        elif type == "rotation":
            m[0][0] = np.cos(theta * math.pi / 180)
            m[0][1] = np.sin(theta * math.pi / 180)
            m[1][0] = -np.sin(theta * math.pi / 180)
            m[1][1] = np.cos(theta * math.pi / 180)
            m[0][2] = a - a * np.cos(theta * math.pi / 180) \
                      - b * np.sin(theta * math.pi / 180)
            m[1][2] = b - b * np.cos(theta * math.pi / 180) \
                      + a * np.sin(theta * math.pi / 180)

        elif type == "trans":
            m[0][2] = -k
            m[1][2] = -j
        elif type == "shear":
            m[0][0] = -1/(k*j-1)
            m[0][1] = j/(k*j-1)
            m[1][0] = k/(k*j-1)
            m[1][1] = -1/(k*j-1)
        else:
            print("type이 잘 못 되었습니다.")
        '''출력 이미지 size 측정 및 출력 후 이미지 위치 조정'''
        m_inv = np.linalg.inv(m)
        v[0][0] = 0
        v[1][0] = 0
        w1 = np.dot(m_inv,v)
        v[0][0] = 2 * a
        v[1][0] = 0
        w2 = np.dot(m_inv,v)
        v[0][0] = 0
        v[1][0] = 2 * b
        w3 = np.dot(m_inv,v)
        v[0][0] = 2 * a
        v[1][0] = 2 * b
        w4 = np.dot(m_inv,v)
        #################################################

        l0 = np.zeros((3, 1))
        l = np.hstack([w1, w2, w3, w4,l0])
        lx = int(np.max(l[0][0:]) - np.min(l[0][0:]))
        ly = int(np.max(l[1][0:]) - np.min(l[1][0:]))
        imgtf = np.zeros((int(ly), int(lx))).astype(np.uint8)
        if np.min(l[0][0:]) < 0:
            adj_x = np.min(l[0][0:])
        else:
            adj_x = 0
        if np.min(l[1][0:]) <0:
            adj_y = np.min(l[1][0:])
        else:
            adj_y = 0
        for yy in range(ly):
            for xx in range(lx):
                v[0][0] = int(xx + adj_x)
                v[1][0] = int(yy + adj_y)
                w = np.dot(m, v)
                if yy == 1 and xx == 1:
                    print(w)
                imgtf[yy][xx] = interpolation(self.int_type,self.img,w)


        cv2.imshow("affine[{0}]".format(self.int_type), imgtf)

        cv2.imwrite(self.output + '[{0}]inverseAffineTF.tif'.format(self.imgname), imgtf)
        cv2.imshow("affine_original", self.img)









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
# forwardaffineTF(T_img, output, "T").TF("rotation",2,30)
inverseAffine(T_img,output,"T","bicubic").affine("rotation",2,1.5,30)
# inverseAffine(T_img,output,"T","nearest").affine("zoom",2,1.5,30)
'''nearest or bilinear or bicubic '''
# print(type(img[0][0]))
# print(type(neg_img[0][0]))
# cv2.imshow('image',img)
# cv2.imshow('negativeimg',neg_img)
if cv2.waitKey(0) == ord('q'):
    pass

cv2.destroyAllWindows()