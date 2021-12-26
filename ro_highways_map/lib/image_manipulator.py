import cv2
import numpy as np
from pprintpp import pprint


class ImageManipulator:
    def __init__(self, folder, file, name):
        self.img_path = f'{folder}/{file}'
        self.file = file
        self.name = name
        self.images = []
        self._load_base_image()

    def _load_base_image(self):
        rgb_img = cv2.imread(self.img_path)
        self.images.append(rgb_img)
        # hsv = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2HSV)
        # self.images.append(hsv)

    def render_image_and_log_pixel_colors_on_click(self):
        for image in self.images:
            cv2.imshow(self.name, image)
        cv2.setMouseCallback(self.name, self._log_pixel_colors, self.images[0])
        cv2.waitKey(0)

    def _log_pixel_colors(self, event, x, y, flags, image):
        if event == cv2.EVENT_LBUTTONDOWN:
            # print(event, x, y, flags, param)
            print(f'Click detected at pixel x={x}, y={y}. '
                  f'RGB color: {image[y][x]}. HSV color: {self._convert_pixel_rgb_to_hsv(image[y][x])}.')

    @staticmethod
    def _convert_pixel_rgb_to_hsv(pixel_rgb):
        hsv_color_values = cv2.cvtColor(np.uint8([[pixel_rgb]]), cv2.COLOR_BGR2HSV)
        return hsv_color_values[0][0]

    def print_img_properties(self, print_matrix=False):
        for image in self.images:
            print(f'Image shape: {image.shape}')
            print(f'Image size: {image.size}')
            if print_matrix:
                pprint(image.tolist(), width=10000)
                print(len(image), len(image[0]), len(image[0][0]))