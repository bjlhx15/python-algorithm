# -*- coding: UTF-8 -*-
import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt
# import matplotlib.pyplot as plt



# def cv_show(name,img):
#     cv2.imshow(name,img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
 
# cv_show('img1',img1)
# cv_show('img2',img2)
def a(imgPath1,imgPath2):     
    img2 = cv2.imread(imgPath2,cv2.IMREAD_GRAYSCALE)
    img1 = cv2.imread(imgPath1,cv2.IMREAD_GRAYSCALE)

    orb = cv2.ORB_create()
    kp1,des1 = orb.detectAndCompute(img1,None)
    kp2,des2 = orb.detectAndCompute(img2,None)

 
    #暴力匹配
    bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
    matches = bf.match(des1,des2)
    matches = sorted(matches,key=lambda x:x.distance)
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:40],img2,flags=2)

    cv2.imshow('test_ORB_bt',img3)
    cv2.imwrite('tests/feature/img_feature/test_ORB_bt.png',img3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print ('---------检测斑点------------')
    a("tests/feature/a.jpg","tests/feature/b.jpg")