import cv2
import os
import numpy as np
import math
import sys, time
from spatial import smoothing,sharpening
os.chdir("DIP_week2")
folder="picture/"

pi = math.pi


folder = "picture/"

'''B smoothing'''
letter_a = "Fig0333(a)(test_pattern_blurring_orig).tif"
letter_a_img = cv2.imread(folder+letter_a,cv2.IMREAD_GRAYSCALE)
# smoothing(letter_a_img,"box",3,"zero","letter_a").filter(0)
# smoothing(letter_a_img,"box",13,"zero","letter_a").filter(0)
# smoothing(letter_a_img,"box",25,"zero","letter_a").filter(0)
# smoothing(letter_a_img,"box",3,"mirror","letter_a").filter(0)
# smoothing(letter_a_img,"box",13,"mirror","letter_a").filter(0)
# smoothing(letter_a_img,"box",25,"mirror","letter_a").filter(0)
# smoothing(letter_a_img,"box",3,"replication","letter_a").filter(0)
# smoothing(letter_a_img,"box",13,"replication","letter_a").filter(0)
# smoothing(letter_a_img,"box",25,"replication","letter_a").filter(0)

# smoothing(letter_a_img,"gaussian",7,"zero","letter_a").filter(1)
# smoothing(letter_a_img,"gaussian",21,"zero","letter_a").filter(3.5)
# smoothing(letter_a_img,"gaussian",43,"zero","letter_a").filter(7)
# smoothing(letter_a_img,"gaussian",7,"mirror","letter_a").filter(1)
# smoothing(letter_a_img,"gaussian",21,"mirror","letter_a").filter(3.5)
# smoothing(letter_a_img,"gaussian",43,"mirror","letter_a").filter(7)
# smoothing(letter_a_img,"gaussian",7,"replication","letter_a").filter(1)
# smoothing(letter_a_img,"gaussian",21,"replication","letter_a").filter(3.5)
# smoothing(letter_a_img,"gaussian",43,"replication","letter_a").filter(7)

'''################################################################'''

'''C sharpening'''
moon = "Fig0338(a)(blurry_moon).tif"
moon_img = cv2.imread(folder+moon,cv2.IMREAD_GRAYSCALE)
dip_xe = "Fig0340(a)(dipxe_text).tif"
dip_xe_img = cv2.imread(folder+dip_xe,cv2.IMREAD_GRAYSCALE)
# sharpening(moon_img,"laplacian",3,"zero","moon").laplacian()
sharpening(dip_xe_img,"unsharp",5,"mirror","dip_xe").unsharp(1)
'''################################################################'''












if cv2.waitKey(0) == ord('q'):
    pass

cv2.destroyAllWindows()