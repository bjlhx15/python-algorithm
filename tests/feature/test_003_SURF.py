# -*- coding: UTF-8 -*-
import sys
import cv2
import numpy as np

def fd(algorithm):
    if algorithm == 'SIFT':
        return cv2.xfeatures2d.SIFT_create()
    if algorithm == 'SURF':
        return cv2.xfeatures2d.SURF_create()

def a(imgPath):
    img = cv2.imread(imgPath)
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    algorithm = input("请输入你的处理方法：SIFT or SURF:")
    fd_flag = fd(algorithm)
    keypoints,descriptor = fd_flag.detectAndCompute(gray,None)
    
    img = cv2.drawKeypoints(image=img,outImage=img,keypoints=keypoints,flags=4,color=(0,0,255))
    
    cv2.imshow('test_SURF',img)
    cv2.imwrite('tests/feature/img_feature/test_SURF.png',img)

    # cv2.namedWindow('test_SURF')
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print ('---------检测斑点------------')
    a("tests/feature/a.jpg")