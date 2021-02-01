import cv2
import numpy as np
import math
import sys, time
import os

# os.chdir("DIP_week1")    ##학교 컴퓨터일때
# folder="picture/"
# output="output/"
# T = "Fig0309(a)(washed_out_aerial_image).tif"
# # Read image
# img = cv2.imread(folder+T,cv2.IMREAD_GRAYSCALE)
# # img1 = img[:,:,0]
# mask1 = img > 170
# mask1 = mask1.astype(np.uint8)

# mask2 = img < 240
# mask2 = mask2.astype(np.uint8)
# print(np.arccos())
# # Scale factor
# ratio = 2
# # Coefficient
# a = -1/2

# # dst = bicubic(img, ratio, a)
# print('Completed!')
# cv2.imshow("x",mask)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

mask = np.arange([5,10,3])
mask2= np.array([1,3,5])
print(mask.shape,mask2.shape)
print(mask*mask2)
print(mask)