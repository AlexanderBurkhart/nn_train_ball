import cv2
import numpy as np
import glob
 
imgs = []
for path in glob.glob('imgs/*.png'):
    img = cv2.imread(path)
    height, width, layers = img.shape
    size = (width,height)
    imgs.append(img)
 
 
out = cv2.VideoWriter('test.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
 
for i in range(len(imgs)):
    out.write(imgs[i])
out.release()
