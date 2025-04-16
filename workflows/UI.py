import cv2
import numpy as np

def update(x):
    brightness = cv2.getTrackbarPos('Brightness', 'Editor') - 100
    contrast = cv2.getTrackbarPos('Contrast', 'Editor') / 100
    sat = cv2.getTrackbarPos('Saturation', 'Editor')

    temp = cv2.convertScaleAbs(img, alpha=contrast, beta=brightness)
    hsv = cv2.cvtColor(temp, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    s = np.clip(s + sat, 0, 255)
    edited = cv2.cvtColor(cv2.merge((h, s, v)), cv2.COLOR_HSV2BGR)
    
    cv2.imshow('Editor', edited)

# Load image
img = cv2.imread('../resources/image.jpg')

cv2.namedWindow('Editor')
cv2.createTrackbar('Brightness', 'Editor', 100, 200, update)
cv2.createTrackbar('Contrast', 'Editor', 100, 300, update)
cv2.createTrackbar('Saturation', 'Editor', 0, 100, update)

update(0)  # Initialize display

cv2.waitKey(0)
cv2.destroyAllWindows()


