import cv2 as cv
import numpy as np
from get_colors import get_limits , get_color_from_user
from PIL import Image as ig
cam = cv.VideoCapture(0)
c_1, c_2, c_3 = get_color_from_user()
n = [c_1,c_2,c_3]
while True:
    success , img = cam.read()
    
    hsvImg =   cv.cvtColor(img , cv.COLOR_BGR2HSV)
    lower_limit , upper_limit =  get_limits(color= n)
    mask = cv.inRange(hsvImg , lower_limit,upper_limit)
    new_mask = ig.fromarray(mask)
    bound_box = new_mask.getbbox()
    if bound_box is not None:
        x1,y1,x2,y2 = bound_box
        cv.rectangle(img,(x1,y1),(x2,y2),(250,0,0),5)
    cv.imshow("window" ,img)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
