import cv2 as cv
import sys
import numpy as np


img1 = cv.imread(cv.samples.findFile("goebbels.jpg"))
img2 = cv.cvtColor(img1, cv.COLOR_RGB2BGR)

gauss = cv.GaussianBlur(img1, (111, 111), 0)
img3 = cv.bitwise_or(img2, gauss)
cv.imshow("3", img3)
k = cv.waitKey(0)

