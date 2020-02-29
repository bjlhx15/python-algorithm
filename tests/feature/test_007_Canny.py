# -*- coding: UTF-8 -*-
import sys
import cv2
import numpy as np

def a(imgPath1):     
    original_img = cv2.imread(imgPath1, 0)

    # canny(): 边缘检测
    img1 = cv2.GaussianBlur(original_img,(3,3),0)
    canny = cv2.Canny(img1, 50, 150)

    # 形态学：边缘检测
    _,Thr_img = cv2.threshold(original_img,210,255,cv2.THRESH_BINARY)#设定红色通道阈值210（阈值影响梯度运算效果）
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))         #定义矩形结构元素
    gradient = cv2.morphologyEx(Thr_img, cv2.MORPH_GRADIENT, kernel) #梯度

    cv2.imshow("original_img", original_img) 
    cv2.imshow("gradient", gradient) 
    cv2.imshow('canny', canny)
    cv2.imwrite('tests/feature/img_feature/test_canny_original_img.png',original_img)
    cv2.imwrite('tests/feature/img_feature/test_canny_gradient.png',gradient)
    cv2.imwrite('tests/feature/img_feature/test_canny_canny.png',canny)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    print ('---------检测斑点------------')
    a("tests/feature/a.jpg")