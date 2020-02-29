# -*- coding: UTF-8 -*-
import sys
import cv2
import numpy as np


def a(imgPath):
    img = cv2.imread(imgPath)
    #png to gray所有都需要做这一步
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #创建一个sift对象，并计算灰度图像
    sift = cv2.xfeatures2d.SIFT_create()
    #计算关键点信息和描述符
    keypoints,descriptor = sift.detectAndCompute(gray,None)
    #显示出关键点
    img = cv2.drawKeypoints(image=img,outImage=img,keypoints=keypoints,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,color=(0,0,255))
    cv2.imshow('test_SIFT',img)
    cv2.imwrite('tests/feature/img_feature/test_SIFT.png',img)
    
    if cv2.waitKey(0) & 0xff == ord("q"):
        cv2.destroyAllWindows()

if __name__ == "__main__":
    print ('---------检测斑点------------')
    a("tests/feature/a.jpg")