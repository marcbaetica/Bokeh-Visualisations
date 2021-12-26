from lib.image_manipulator import ImageManipulator


IMG_FOLDER = 'map_pictures'
FILES = ['romanianhighwaymap_en.jpg', 'ro_motorways_and_expressways.png',
         'Romania_Motorways_DE_1.svg', 'icon_test.png']

img_manipulator = ImageManipulator(IMG_FOLDER, FILES[1], 'ro_highways')
img_manipulator.render_image_and_log_pixel_colors()
