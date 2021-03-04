import cv2 #opencv读取的格式是BGR
import numpy as np
import matplotlib.pyplot as plt#Matplotlib是RGB

def cv_show(img,name):
    cv2.imshow(name,img)
    cv2.waitKey()
    cv2.destroyAllWindows()

img = cv2.imread('./img/huawei/17.jpg',cv2.IMREAD_GRAYSCALE)

v1=cv2.Canny(img,80,150)

cv_show(v1,'v1')
