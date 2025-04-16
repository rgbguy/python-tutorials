import cv2
import numpy as np

img = cv2.imread('../resources/image.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

# Increase saturation (clip to 255)
s = np.clip(s + 50, 0, 255)

final_hsv = cv2.merge((h, s, v))
saturated_img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
cv2.imwrite('../output/saturated.jpg', saturated_img)


