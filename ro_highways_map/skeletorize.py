import cv2
import numpy as np
from pprintpp import pprint


img = cv2.imread('map_pictures/A2_autostrada_soarelui.png', 0)
size = np.size(img)
print(size)
skel = np.zeros(img.shape, np.uint8)
pprint(skel)

ret, img = cv2.threshold(img, 127, 255, 0)
pprint(ret)
pprint(img)
cv2.imshow("skel", ret)
# cv2.imshow("skel", img)
cv2.waitKey(0)
element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
pprint(element)
cv2.imshow('element', element)
cv2.waitKey(0)
done = False

while not done:
    # cv2.imshow("skel", skel)
    # cv2.waitKey(0)
    eroded = cv2.erode(img, element)
    cv2.imshow("skel", eroded)
    cv2.waitKey(0)
    temp = cv2.dilate(eroded, element)
    cv2.imshow("skel", temp)
    cv2.waitKey(0)
    temp = cv2.subtract(img, temp)
    cv2.imshow("skel", temp)
    cv2.waitKey(0)
    skel = cv2.bitwise_or(skel, temp)
    cv2.imshow("skel", skel)
    cv2.waitKey(0)
    img = eroded.copy()

    zeros = size - cv2.countNonZero(img)
    if zeros == size:
         done = True


cv2.imshow("skel", skel)
cv2.waitKey(0)
cv2.destroyAllWindows()
