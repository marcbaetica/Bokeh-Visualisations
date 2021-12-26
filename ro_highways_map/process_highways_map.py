from lib.image_manipulator import ImageManipulator


IMG_FOLDER = 'map_pictures'
FILES = ['romanianhighwaymap_en.jpg', 'ro_motorways_and_expressways.png',
         'Romania_Motorways_DE_1.svg', 'icon_test.png']

img_manipulator = ImageManipulator(IMG_FOLDER, FILES[1], 'ro_highways')
img_manipulator.print_img_properties()
# img_manipulator.render_image_and_log_pixel_colors_on_click()
img_manipulator.isolate_img_features([60, 120, 120], [71, 255, 255])  # Looking for [ 60 255 128].
