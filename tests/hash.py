# -*- coding: UTF-8 -*-

import numpy as np
import cv2
import collections

def flatten(x):
    result = []
    for el in x:
        if isinstance(x, collections.Iterable) and not isinstance(el, str):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result

#均值哈希算法
def aHash(img):
    # 缩放为8*8
    img = cv2.resize(img, (8, 8), interpolation=cv2.INTER_CUBIC)
    # 转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # s为像素和初值为0，hash_str为hash值初值为''
    s = 0
    hash_str = ''
    # 遍历累加求像素和
    for i in range(8):
        for j in range(8):
            s = s + gray[i, j]
    # 求平均灰度
    avg = s / 64
    # 灰度大于平均值为1相反为0生成图片的hash值
    for i in range(8):
        for j in range(8):
            if gray[i, j] > avg:
                hash_str = hash_str + '1'
            else:
                hash_str = hash_str + '0'
    return hash_str
#差值感知算法
def dHash(img):
    #缩放8*8
    img=cv2.resize(img,(9,8),interpolation=cv2.INTER_CUBIC)
    #转换灰度图
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    hash_str=''
    #每行前一个像素大于后一个像素为1，相反为0，生成哈希
    for i in range(8):
        for j in range(8):
            if   gray[i,j]>gray[i,j+1]:
                hash_str=hash_str+'1'
            else:
                hash_str=hash_str+'0'
    return hash_str
# 感知哈希
def pHash(img):
	"""get image pHash value"""
	#加载并调整图片为32x32灰度图片
	# img=cv2.imread(imgfile, cv2.CV_LOAD_IMAGE_GRAYSCALE)
	img=cv2.resize(img,(32,32),interpolation=cv2.INTER_CUBIC)
 
        #创建二维列表
	h, w = img.shape[:2]
	vis0 = np.zeros((h,w), np.float32)
	vis0[:h,:w] = img       #填充数据
 
	#二维Dct变换
	vis1 = cv2.dct(cv2.dct(vis0))
	#cv.SaveImage('a.jpg',cv.fromarray(vis0)) #保存图片
	vis1.resize(8,8)
 
	#把二维list变成一维list
	img_list=flatten(vis1.tolist()) 
 
	#计算均值
	avg = sum(img_list)*1./len(img_list)
	avg_list = ['0' if i<avg else '1' for i in img_list]
 
	#得到哈希值
	return ''.join(['%x' % int(''.join(avg_list[x:x+4]),2) for x in range(0,64,4)])

#Hash值对比 汉明距离
def cmpHash(hash1,hash2):
    n=0
    #hash长度不同则返回-1代表传参出错
    if len(hash1)!=len(hash2):
        return -1
    #遍历判断
    for i in range(len(hash1)):
        #不相等则n计数+1，n最终为相似度
        if hash1[i]!=hash2[i]:
            n=n+1
    return n

def getAHash(img1,img2):
    img1=cv2.imread(img1)
    img2=cv2.imread(img2)
    hash1= aHash(img1)
    hash2= aHash(img2)
    # print(hash1)
    # print(hash2)
    n=cmpHash(hash1,hash2)
    print ('均值哈希算法相似度：'+ str(n))
    return 1

def getDHash(img1,img2):
    img1=cv2.imread(img1)
    img2=cv2.imread(img2)
    hash1= dHash(img1)
    hash2= dHash(img2)
    # print(hash1)
    # print(hash2)
    n=cmpHash(hash1,hash2)
    print ('差值哈希算法相似度：'+ str(n))
    return 1    

def getPHash(img1,img2):
    img1=cv2.imread(img1, cv2.IMREAD_GRAYSCALE)
    img2=cv2.imread(img2, cv2.IMREAD_GRAYSCALE)
    hash1= pHash(img1)
    hash2= pHash(img2)
    # print(hash1)
    # print(hash2)
    n=cmpHash(hash1,hash2)
    print ('感知哈希算法相似度：'+ str(n))
    return 1 

print ('相似度越小，说明两张图片越相似')

print ('---------均值哈希------------')

print ('a 和 b 对比，b复制的')
getAHash ('/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/a.jpg','/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/b.jpg')

print ('a 和 c 对比，c是裁剪的')
getAHash ('/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/a.jpg','/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/c.jpg')

print ('a 和 d 对比，d裁剪部分')
getAHash ('/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/a.jpg','/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/d.jpg')

print ('a 和 ah 对比，图片内容完全不一致')
getAHash ('/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/a.jpg','/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/ah.jpg')


print ('---------差值哈希------------')

print ('a 和 b 对比，b复制的')
getDHash ('/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/a.jpg','/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/b.jpg')

print ('a 和 c 对比，c是裁剪的')
getDHash ('/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/a.jpg','/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/c.jpg')

print ('a 和 d 对比，d裁剪部分')
getDHash ('/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/a.jpg','/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/d.jpg')

print ('a 和 ah 对比，图片内容完全不一致')
getDHash ('/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/a.jpg','/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/ah.jpg')

print ('---------感知哈希------------')

print ('a 和 b 对比，b复制的')
getPHash ('/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/a.jpg','/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/b.jpg')

print ('a 和 c 对比，c是裁剪的')
getPHash ('/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/a.jpg','/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/c.jpg')

print ('a 和 d 对比，d裁剪部分')
getPHash ('/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/a.jpg','/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/d.jpg')

print ('a 和 ah 对比，图片内容完全不一致')
getPHash ('/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/a.jpg','/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/ah.jpg')
