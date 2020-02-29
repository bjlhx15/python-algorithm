# -*- coding: UTF-8 -*-
import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt



def a(imgPath):
    img = cv2.imread(imgPath,0)

    fast = cv2.FastFeatureDetector_create()
 
    keypoints = fast.detect(img,None)
    imgs = cv2.drawKeypoints(img,keypoints,outImage=img,color=(0,0,255))
 
    print("Thereshold:",fast.getThreshold())
    print("nonmaxSuppression:",fast.getNonmaxSuppression())
    print("neighborhood:",fast.getType())
    print("Total keypoints with nonmaxSuppression:",len(keypoints))
 
    cv2.imshow('test_FAST',imgs)
    cv2.imwrite('tests/feature/img_feature/test_FAST.png',imgs)


    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print ('---------检测斑点------------')
    a("tests/feature/a.jpg")