import cv2
import numpy as np
import random
import os

def add_shadow(img_url,result_img_url):
    orimg = cv2.imread(img_url,cv2.IMREAD_GRAYSCALE)
    maskurl = "mask/"+str(int(random.random()*10))+".png"
    maskimg = cv2.imread(maskurl,cv2.IMREAD_GRAYSCALE)

    orimg_resize = cv2.resize(orimg,(256,256))
    maskimg_resize= cv2.resize(maskimg,(256,256))

    mask = np.zeros([258,258],np.uint8)
    cv2.floodFill(orimg_resize,mask,(0,0),255,1,0,flags=4|(255<<8)|cv2.FLOODFILL_FIXED_RANGE)
    mask = mask[1:257,1:257]
    # cv2 .namedWindow("input image",cv2.WINDOW_AUTOSIZE)
    # cv2.imshow("temp result",mask)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    mask_no = cv2.bitwise_not(mask)
    maskimg_resize = cv2.bitwise_and(mask_no,maskimg_resize)

    resultimg = cv2.bitwise_and(orimg_resize,maskimg_resize)
    resultimg = cv2.bitwise_or(resultimg,mask)
    # cv2 .namedWindow("input image",cv2.WINDOW_AUTOSIZE)
    # cv2.imshow("temp result",resultimg)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    cv2.imwrite(result_img_url,resultimg)

def add_a_lot_shadow(file_url,result_url):
    file_dir = os.listdir(file_url)
    for file in file_dir:
        filename = file_url+file
        resultname = result_url+file
        add_shadow(filename,resultname)
        print(file)
if __name__ == "__main__":
    add_a_lot_shadow("dataresult/","maskresult/")