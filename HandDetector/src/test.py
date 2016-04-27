#coding=utf-8
'''
Created on 2014年10月24日

@author: Yang
'''
from Tkinter import *
import Tkinter
import cv2
import cv2.cv as cv
import numpy as np
#from numpy.matrixlib.defmatrix import matrix
#from cv2 import CV_32SC1


#merged_frame = cv.CreateMat(640, 960, CV_32SC1)
#a = np.asarray(merged_frame)

#show a blank_image
#blank_image = np.zeros((640,960,3), np.uint8)
#cv2.namedWindow("Video2",cv2.CV_WINDOW_AUTOSIZE)
#cv2.imshow('Video2', blank_image)

#draw a circle 
# im = np.zeros((640,960,3), np.uint8)
# cv2.circle(im,(308,105),5,(0,0,255),-1)
# cv2.imshow("image", im)
# 
# """
# cnt = (389.9033,334.3815),(30.04781,40.26132),-65.77225
# box = cv2.cv.BoxPoints(cnt)
# box = np.int0(box)
# im = np.zeros((640,960,3), np.uint8)
# cv2.drawContours(im,[box],0,(0,0,255),2)
# cv2.namedWindow("image",cv2.CV_WINDOW_AUTOSIZE)
# cv2.imshow("image", im)
# """
# 
# k = cv2.waitKey(0) & 0xFF

# root = Tk()
#   
# w = Canvas(root, width=1000, height=1000, bd = 10, bg = 'white')
# w.pack()
#   
# b = Button(width = 10, height = 2, text = 'Button1')
# b.grid(row = 1, column = 0)
# b2 = Button(width = 10, height = 2, text = 'Button2')
# b2.grid(row = 1,column = 1)
#   
# #cv2.namedWindow("video",cv2.CV_WINDOW_AUTOSIZE)
# cap1 = cv2.VideoCapture("D:\CUHK_Project\HandDetector\sample1\d.AVI") 
#   
# while True:
#     #im = cv2.imread("d:\cat.jpg")
#     #.create_image(0,0,image=im)
#     #cv2.imshow('video',im)
#     if cv.WaitKey(10) == 27:
#         break
#   
# root.mainloop()
def deco(func):
    def _deco(a, b):
        print("before myfunc() called.")
        ret = func(a, b)
        print("  after myfunc() called. result: %s" % ret)
        return ret
    return _deco
 
@deco
def myfunc(a, b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a + b
 
myfunc(1, 2)
myfunc(3, 4)

