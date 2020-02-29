# -*- coding: UTF-8 -*-
import sys
import cv2
import numpy as np

lowThreshold = 0
max_lowThreshold = 100
ratio = 3
kernel_size = 3


def CannyThreshold(lowThreshold):
    detected_edges = cv2.GaussianBlur(gray,(3,3),0)
    detected_edges = cv2.Canny(detected_edges,
                               lowThreshold,
                               lowThreshold*ratio,
                               apertureSize = kernel_size)
    dst = cv2.bitwise_and(img,img,mask = detected_edges)  # just add some colours to edges from original image.
    cv2.imshow('canny demo',dst)

img = cv2.imread('tests/feature/a.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

def a(imgPath1):
    
    cv2.namedWindow('canny demo')
    
    cv2.createTrackbar('Min threshold','canny demo',lowThreshold, max_lowThreshold, CannyThreshold)
    
    CannyThreshold(0)  # initialization

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    print ('---------检测斑点------------')
    a("tests/feature/a.jpg")