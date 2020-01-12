import cv2
import numpy as np
import csv
import glob
import os

with open('data.csv', 'w') as csvfile:
    fw = csv.writer(csvfile, delimiter=',')
    i = 0
    for img_path in os.listdir('imgs'):
        print(img_path)
        img = cv2.imread('imgs/' + img_path)
        r = cv2.selectROI(img)
        print(r)
        fw.writerow([i, r[0], r[1], r[0]+r[2], r[1]+r[3]])
        i += 1


