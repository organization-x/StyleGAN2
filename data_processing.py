import glob
import cv2
import os
import imageio
import numpy as np

input_dir = "./raw_data"
out_dir = "./processed_data"
files = glob.glob("./raw_data/images/*")
IMG_SIZE = 256

try:
    os.mkdir('./processed_data')
except Exception:
    print('processed data directory found')

counter = 0
for j in range(len(files)):
    for file in glob.glob(files[j] + "/*.jpg")[0:25]:
        raw_img = cv2.imread(file)
        processed_img = cv2.resize(raw_img, (IMG_SIZE, IMG_SIZE), interpolation=cv2.INTER_AREA)
        cv2.imwrite(out_dir + "/{:08d}.png".format(counter), processed_img)
        counter += 1