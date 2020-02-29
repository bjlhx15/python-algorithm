# -*- coding: UTF-8 -*-
import cv2
import numpy as np

def a(imgPath):
    img = cv2.imread(imgPath)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)
    dst = cv2.dilate(dst,None)
    img[dst>0.01 * dst.max()] = [0,0,255]
    cv2.imshow('test_ Harris',img)
    cv2.imwrite('tests/feature/img_feature/test_ Harris.png',img)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()

if __name__ == "__main__":
    print ('---------检测角点------------')
    a("tests/feature/a.jpg")