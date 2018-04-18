import cv2
import numpy as np
import os

def load_image(file_path):
    """Takes in a file path and returns a numpy array containing a list of pixel values
    for each band in the list"""

    im = cv2.imread(file_path)

    channels = cv2.split(im)
    res = []

    for channel in channels:
        if sum(channel)[0] > 0:
            res.append(cv2.equalizeHist(channel))

    equalized = np.zeros((im.shape[0], im.shape[1], len(res)))

    for i in range(equalized.shape[2]):
        equalized[:,:,i] = res[i]

    return equalized

def merge_bands(red_file_name, blue_file_name, green_file_name, output_name):
    """Takes in three images at he specified paths (assumed to be grayscale) and
    saves a fourth image with the output name to /results (which is listed in
    .gitignore)"""

    red_values = load_image(red_file_name)
    blue_values = load_image(blue_file_name)
    green_values = load_image(green_file_name)

    merged = cv2.merge((red_values[:,:,0], blue_values[:,:,0], green_values[:,:,0]))

    cv2.imwrite(output_name, merged)


if __name__ == '__main__':
    data_folder = '/home/aiden/Final_Project_Image_Repo/images/'

    name_1 = data_folder + 'band_1.png'
    name_2 = data_folder + 'band_2.png'
    name_3 = data_folder + 'band_3.png'
    name_4 = data_folder + 'band_4.png'
    name_5 = data_folder + 'band_5.png'
    name_6 = data_folder + 'band_6.png'
    name_7 = data_folder + 'band_7.png'

    merge_bands(name_2, name_3, name_4, 'new_color.jpg')
