import cv2


class ImageManipulator:
    def __init__(self, folder, file, name):
        self.img_path = f'{folder}/{file}'
        self.file = file
        self.name = name
        self.image = self._load_image()

    def _load_image(self):
        rgb_img = cv2.imread(self.img_path)
        return rgb_img
        # hsv = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2HSV)
        # return hsv

    def render_image_and_log_pixel_colors(self):
        cv2.imshow(self.name, self.image)
        cv2.waitKey(0)
