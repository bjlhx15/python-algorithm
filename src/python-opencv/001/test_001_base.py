# -*- coding: UTF-8 -*-
import numpy as np
import cv2

# -----------------------------直接读取--------------------------------
def direct_read(imgPath):
    img = cv2.imread(imgPath,0)    #读取图像（直接读取）

    # img = cv2.imread(imgPath,cv2.IMREAD_COLOR)   #读取图像（BGR，忽略alpha通道）
    # img = cv2.imread(imgPath,cv2.IMREAD_GRAYSCALE)   #读取图像（读入灰度图片）
    # img = cv2.imread(imgPath,cv2.IMREAD_UNCHANGED)   #读取图像（完整图片，包括alpha通道）
    
    # -----------------------------图片的属性 （长、宽、通道数）--------------------------------

    """
    输出：
        图片形状： (366, 445, 3)
        图片大小： 488610
        图片类型： uint8
    """
    print ("图片形状：",img.shape)
    print ("图片大小：",img.size)
    print ("图片类型：",img.dtype)

    cv2.imshow('image',img)         #显示图像
    k = cv2.waitKey(0)
    if k == 27:                     # 按 Esc 退出（关闭显示窗口）
        cv2.destroyAllWindows()
    elif k == ord('s'):             # 按 's' 保存并退出 （关闭显示窗口）
        cv2.imwrite('test.png',img)
        cv2.destroyAllWindows() 

# -----------------------------保存------------------------

"""
写入（保存）图片选取参数：
	cv2.imwrite(file，img，num)
	file：文件名
	img： 图像
	num： 可选参数（针对特定的格式）：
		  对于JPEG，表示图像的质量，用0-100的整数表示，默认95，越高画质越好，文件越大
		  对于png， 表示压缩级别。范围0到9，默认3，越高文件越小，画质越差
"""
def write(imgPath):
    grayImage = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)
    cv2.imwrite('test.png', grayImage) 
    cv2.imwrite('test.jpeg', grayImage , (cv2.IMWRITE_JPEG_QUALITY, 80))
    cv2.imwrite('test.png', grayImage , (cv2.IMWRITE_PNG_COMPRESSION, 5))

if __name__ == "__main__":
    imgPath = 'src/python-opencv/a.jpg'
    direct_read(imgPath)