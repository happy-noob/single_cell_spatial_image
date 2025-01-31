import os
import cv2
import numpy as np
import pandas as pd

np.set_printoptions(threshold=np.inf)
np.set_printoptions(suppress=True)

def seg_category_map(optical_img,category_map, output_path):

    print(optical_img.shape)
    category_map = cv2.resize(category_map, dsize=(optical_img.shape[0], optical_img.shape[1]),  interpolation= cv2.INTER_NEAREST)
    # category_map = cv2.cvtColor(category_map, cv2.COLOR_BGR2GRAY)
    print(category_map.shape)
    category_list = np.unique(category_map)
    print(category_list)

    for category in category_list:
        img = np.ones(shape=(optical_img.shape[0], optical_img.shape[1], 3), dtype=np.uint8) * 255
        if category!=0:
            pixel_x, pixel_y = np.where(category_map == category)
            for i in range(len(pixel_x)):
                img[pixel_x[i]][pixel_y[i]] = optical_img[pixel_x[i]][pixel_y[i]]
            if not os.path.exists(output_path+'/optical_segmentation/'):
                os.makedirs(output_path+'/optical_segmentation/')
            cv2.imwrite(output_path+'/optical_segmentation/category_'+str(category)+'.png', img)

# optical_img = cv2.imread('./optical_images/151507.png')
# category_map = cv2.imread('./label/151507.png')
# seg_category_map(optical_img, category_map)