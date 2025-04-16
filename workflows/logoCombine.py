import cv2
import numpy as np

# Load images
base = cv2.imread('../resources/image.jpg')
logo = cv2.imread('../resources/logo.png', cv2.IMREAD_UNCHANGED)  # logo must have alpha channel

# Resize logo
logo = cv2.resize(logo, (100, 100))

# Define region on base image
x, y = base.shape[1] - 110, base.shape[0] - 110
roi = base[y:y+100, x:x+100]

# Split logo channels
b, g, r, a = cv2.split(logo)
overlay_color = cv2.merge((b, g, r))

# Create mask and inverse mask
mask = cv2.merge((a, a, a)) / 255.0
inv_mask = 1.0 - mask

# Blend logo and base image
roi = (overlay_color * mask + roi * inv_mask).astype(np.uint8)
base[y:y+100, x:x+100] = roi

cv2.imwrite('../output/with_logo.jpg', base)


