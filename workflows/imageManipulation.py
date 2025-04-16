import cv2
import numpy as np

img = cv2.imread('../resources/image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('../output/bw_image.jpg', gray)
