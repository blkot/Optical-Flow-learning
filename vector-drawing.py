# -*- coding: utf-8 -*-
"""
Created on Fri Apr 01 17:45:50 2016

@author: Orange
"""
from numpy import *
import cv2

def draw_flow(im,flow,step=16):
    h,w = im.shape[:2]
    y,x = mgrid[step/2:h:step,step/2:w:step].reshape(2,-1)
    fx,fy = flow[y,x].T
    lines = vstack([x,y,x+fx,y+fy]).T.reshape(-1,2,2)
    lines = int32(lines)
    
    vis = cv2.cvtColor(im,cv2.COLOR_GRAY2BGR)
    for (x1,y1),(x2,y2) in lines:
        cv2.line(vis,(x1,y1),(x2,y2),(0,255,0),1)
        cv2.circle(vis,(x1,y1),1,(0,255,0),-1)##"""图像，圆心，半径，颜色绿，？？？"""
    return vis
    
cap = cv2.VideoCapture(0)

ret,im = cap.read()
prev_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

while True:
    ret,im = cap.read()
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    
    flow = cv2.calcOpticalFlowFarneback(prev_gray,gray,None,0.5,3,15,3,5,1.2,0)
    prev_gray = gray
    
    cv2.imshow('Optical Flow Test',draw_flow(gray,flow))
    k = cv2.waitKey(30) & 0xff
    if k == 27:
          break
    elif k == ord('s'):
        cv2.imwrite('resultgreen.png',draw_flow(gray,flow))