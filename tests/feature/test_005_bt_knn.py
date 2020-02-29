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
    img2 = cv2.imread(imgPath2,0)
    img1 = cv2.imread(imgPath1,0)

    sift = cv2.xfeatures2d.SIFT_create()
 
    kp1,des1 = sift.detectAndCompute(img1,None)
    kp2,des2 = sift.detectAndCompute(img2,None)
 
    check = input("请输入你的匹配方式：1 or k:")
    if check == '1':
        bf = cv2.BFMatcher(crossCheck=True)
        # 1对1匹配
        matches = bf.match(des1,des2)
        matches = sorted(matches,key=lambda x:x.distance)
        img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None,flags=2)
        # cv_show('img3',img3)
    elif check == 'k':
        #k对最佳匹配
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1,des2,k=2)
        good = []
        
        for m,n in matches:
            if m.distance < 0.75*n.distance:
                good.append([m])
        
        img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
        # cv_show('img3',img3)

    cv2.imshow('test_bt_knn_'+check,img3)
    cv2.imwrite('tests/feature/img_feature/test_bt_knn_'+check+'.png',img3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print ('---------检测斑点------------')
    a("tests/feature/a.jpg","tests/feature/b.jpg")