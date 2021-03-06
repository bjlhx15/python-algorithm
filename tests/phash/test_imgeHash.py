# -*- coding: UTF-8 -*-

# pip install imagehash

from PIL import Image
import imagehash

def getPHash(img1,img2):
    highfreq_factor = 1
    hash_size = 8
    # img_size = hash_size * highfreq_factor
    hash1 = imagehash.phash(Image.open(img1),hash_size=hash_size,highfreq_factor=highfreq_factor)
    hash2 = imagehash.phash(Image.open(img2),hash_size=hash_size,highfreq_factor=highfreq_factor)
    # print(hash1)
    # print(hash2)
    # return 1 - (hash1 - hash2)/len(hash1.hash)**2
    return hash1-hash2

def getAHash(img1,img2):
    hash_size = 6
    hash1 = imagehash.average_hash(Image.open(img1),hash_size=hash_size)
    hash2 = imagehash.average_hash(Image.open(img2),hash_size=hash_size)
    # print(hash1)
    # print(hash2)
    # return 1 - (hash1 - hash2)/len(hash1.hash)**2
    return hash1-hash2

def getDHash(img1,img2):
    hash_size = 10
    hash1 = imagehash.dhash(Image.open(img1),hash_size=hash_size)
    hash2 = imagehash.dhash(Image.open(img2),hash_size=hash_size)
    # print(hash1)
    # print(hash2)
    # return 1 - (hash1 - hash2)/len(hash1.hash)**2
    return hash1-hash2

def getWHash(img1,img2):
    hash_size = 8
    mode = 'db4'
    image_scale = 64
    hash1 = imagehash.whash(Image.open(img1),image_scale=image_scale,hash_size=hash_size,mode = mode)
    hash2 = imagehash.whash(Image.open(img2),image_scale=image_scale,hash_size=hash_size,mode = mode)
    # print(hash1)
    # print(hash2)
    # return 1 - (hash1 - hash2)/len(hash1.hash)**2
    return hash1-hash2

print ('---------感知哈希------------')

imgA='/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/phash/a.jpg'
imgB='/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/phash/b.jpg'
imgC='/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/phash/c.jpg'
imgD='/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/phash/d.jpg'
imgAH='/Users/lihongxu6/IdeaProjectsGit/python-algorithm/tests/phash/ah.jpg'

result=getPHash (imgA,imgB)
print ('a 和 b 对比，b复制的:'+str(result))

result=getPHash (imgA,imgC)
print ('a 和 c 对比，c是裁剪的:'+str(result))

result=getPHash (imgA,imgD)
print ('a 和 d 对比，d裁剪部分:'+str(result))

result=getPHash (imgA,imgAH)
print ('a 和 ah 对比，图片内容完全不一致:'+str(result))


print ('---------均值哈希------------')

result=getAHash (imgA,imgB)
print ('a 和 b 对比，b复制的:'+str(result))

result=getAHash (imgA,imgC)
print ('a 和 c 对比，c是裁剪的:'+str(result))

result=getAHash (imgA,imgD)
print ('a 和 d 对比，d裁剪部分:'+str(result))

result=getAHash (imgA,imgAH)
print ('a 和 ah 对比，图片内容完全不一致:'+str(result))

print ('---------差值哈希------------')

result=getDHash (imgA,imgB)
print ('a 和 b 对比，b复制的:'+str(result))

result=getDHash (imgA,imgC)
print ('a 和 c 对比，c是裁剪的:'+str(result))

result=getDHash (imgA,imgD)
print ('a 和 d 对比，d裁剪部分:'+str(result))

result=getDHash (imgA,imgAH)
print ('a 和 ah 对比，图片内容完全不一致:'+str(result))

print ('---------小波哈希------------')

result=getWHash (imgA,imgB)
print ('a 和 b 对比，b复制的:'+str(result))

result=getWHash (imgA,imgC)
print ('a 和 c 对比，c是裁剪的:'+str(result))

result=getWHash (imgA,imgD)
print ('a 和 d 对比，d裁剪部分:'+str(result))

result=getWHash (imgA,imgAH)
print ('a 和 ah 对比，图片内容完全不一致:'+str(result))