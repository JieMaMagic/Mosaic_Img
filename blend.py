# -*- coding:utf-8 -*-
from PIL import Image
import cv2

def blend_two_images2(path1, path2):
    img1 = Image.open(path1)
    img1 = img1.convert('RGBA')
    img1_sz = img1.size
    img2 = Image.open(path2)
    img2 = img2.resize(img1_sz, Image.BICUBIC)
    img2 = img2.convert('RGBA')
    r, g, b, alpha = img2.split()
    alpha = alpha.point(lambda i: i>0 and 55)
    img = Image.composite(img2, img1, alpha)
    img.show()
    img.save( "mosaic.png")
    return

if __name__ == '__main__':
    img1_path = '/home/magic/Desktop/MosaicImg-master/TestImage.jpg'
    img2_path = '/home/magic/Desktop/MosaicImg-master/crop.jpg'
    img = cv2.imread(img2_path)
    print(img.shape)
    cropped = img[0:865, 0:865]
    cv2.imwrite("/home/magic/Desktop/MosaicImg-master/1.jpg",cropped)
    img3_path = '/home/magic/Desktop/MosaicImg-master/1.jpg'
    blend_two_images2( img1_path,img3_path)