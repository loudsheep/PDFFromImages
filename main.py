import os
from bgcolors import BgColors
from pdf import *

IMAGE_EXT = ['.jpg', '.jpeg', '.png', '.bmp']


def file_is_image(file_path):
    ext = os.path.splitext(file_path)[-1]
    for i in IMAGE_EXT:
        if ext == i:
            return True
    return False


def get_images_in_directory(dir_path):
    result = []
    for f in os.listdir(dir_path):
        if file_is_image(f):
            result.append(os.path.join(dir_path, f))
    return result


if __name__ == '__main__':
    path = input('Enter path: ')

    if not os.path.isdir(path):
        print(BgColors.FAIL + "Path is not a directory!")
        quit(0)

    images = get_images_in_directory(path)
    if len(images) == 0:
        print(BgColors.FAIL + "No images in directory!")
        quit(0)

    print(BgColors.OKGREEN + "Found", str(len(images)), "images, generating PDF file" + BgColors.ENDC)

    generate_pdf_from_images(os.path.join(path, "generated.pdf"), images)
    input("Press anything to exit...")
