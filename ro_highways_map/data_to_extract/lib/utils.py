import cv2
from pprintpp import pprint


def print_img_properties(img, print_matrix=False):
    print(f'Image shape: {img.shape}')
    print(f'Image size: {img.size}')
    if print_matrix:
        pprint(img.tolist(), width=10000)
        print(len(img), len(img[0]), len(img[0][0]))


def log_pixel_color(event, x, y, flags, image):
    if event == cv2.EVENT_LBUTTONDOWN:
        # print(event, x, y, flags, param)
        print(f'Click detected at x={x}, y={y}. Pixel color: {image[y][x]}')
