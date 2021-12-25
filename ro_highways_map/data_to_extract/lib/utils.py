from pprintpp import pprint


def print_img_properties(img, print_matrix=False):
    print(f'Image shape: {img.shape}')
    print(f'Image size: {img.size}')
    if print_matrix:
        pprint(img.tolist(), width=10000)
        print(len(img), len(img[0]), len(img[0][0]))
