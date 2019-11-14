import cv2
import numpy as np
import os

def cut_imgs(file_url,saved_file_url):
    file_dir = os.listdir(file_url)
    for file in file_dir:
        filename = file_url+file
        img = cv2.imread(filename)
        cropped = img[0:511,512:1023]
        cv2.imwrite(saved_file_url+file,cropped)
        print(file)

if __name__ == "__main__":
    cut_imgs("data/","dataresult/")


