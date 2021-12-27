import cv2
import numpy as np
from pprintpp import pprint


class ImageManipulator:
    def __init__(self, folder, file, name):
        self.img_path = f'{folder}/{file}'
        self.folder = folder
        self.file = file
        self.name = name
        self.image = None
        self._load_base_image()

    def _load_base_image(self):
        # TODO: If rgb_img is None raise exception for failing to load.
        rgb_img = cv2.imread(self.img_path)
        self.image = rgb_img

    def render_image_and_log_pixel_colors_on_click(self):
        cv2.imshow(self.name, self.image)
        cv2.setMouseCallback(self.name, self._log_pixel_colors, self.image)
        cv2.waitKey(0)

    def _log_pixel_colors(self, event, x, y, flags, image):
        if event == cv2.EVENT_LBUTTONDOWN:
            # print(event, x, y, flags, param)
            print(f'Click detected at pixel x={x}, y={y}. '
                  f'RGB color: {image[y][x]}. HSV color: {self._convert_pixel_rgb_to_hsv(image[y][x])}.')

    @staticmethod
    def _convert_pixel_rgb_to_hsv(pixel_rgb):
        hsv_color_values = cv2.cvtColor(np.uint8([[pixel_rgb]]), cv2.COLOR_BGR2HSV)
        return hsv_color_values[0][0]  # Converts back from 3D matrix to 1D.

    def print_img_properties(self, print_matrix=False):
        print(f'Image shape: {self.image.shape}')
        print(f'Image size: {self.image.size}')
        if print_matrix:
            pprint(self.image.tolist(), width=10000)
            print(len(self.image), len(self.image[0]), len(self.image[0][0]))

    def isolate_img_features(self, lower_hsv_bound, upper_hsv_bound, render=False):
        # Convert image to HSV and generate mask based on bounds.
        mask_img = self.generate_mask_from_hsv_bounds(lower_hsv_bound, upper_hsv_bound)
        cv2.imwrite(f'{self.folder}/mask_{self.file}', mask_img)
        # Merge mask with rgb image to mask all areas of disinterest.
        isolated_features_img = cv2.bitwise_and(self.image, self.image, mask=mask_img)
        cv2.imwrite(f'{self.folder}/processed_{self.file}', isolated_features_img)
        if render:
            cv2.imshow('isolated_features_img', isolated_features_img)
            cv2.waitKey(0)

    def generate_mask_from_hsv_bounds(self, lower_hsv_bound, upper_hsv_bound):
        hsv_img = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        lower_hsv_bound = np.uint8(lower_hsv_bound)
        upper_hsv_bound = np.uint8(upper_hsv_bound)
        return cv2.inRange(hsv_img, lower_hsv_bound, upper_hsv_bound)

