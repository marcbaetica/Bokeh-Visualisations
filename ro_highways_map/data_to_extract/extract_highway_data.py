import sys
from cv2 import cv2
from lib.utils import print_img_properties, log_pixel_color
import numpy as np
from pprintpp import pprint
from time import sleep


IMAGE_LOCATION = 'ro_motorways_and_expressways.png'
# IMAGE_LOCATION = 'icon_test.png'

rgb_img = cv2.imread(IMAGE_LOCATION)

print_img_properties(rgb_img)

hsv = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2HSV)

# lower_green = np.array([0,100,100])
# upper_green = np.array([60, 255, 255])

# https://stackoverflow.com/questions/48109650/how-to-detect-two-different-colors-using-cv2-inrange-in-python-opencv
# lower_green = np.array([60, 120, 120])
# upper_green = np.array([70, 255, 255])


lower_green = np.array([60, 120, 120])
upper_green = np.array([60, 255, 255])

mask = cv2.inRange(hsv, lower_green, upper_green)

green = np.uint8([[[0, 128, 0]]])
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
print(f'HSV conversion: {hsv_green}')

res = cv2.bitwise_and(rgb_img, rgb_img, mask=mask)

cv2.imshow('rgb_img', rgb_img)
cv2.imshow('mask', mask)
cv2.imshow('res', res)

cv2.setMouseCallback('rgb_img', log_pixel_color, rgb_img)


cv2.imwrite('ro_isolated_motorways_and_expressways.jpg', res)
cv2.waitKey(0)
# sleep(5)
