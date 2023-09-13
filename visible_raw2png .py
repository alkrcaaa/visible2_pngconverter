import cv2 as cv
import numpy as np
import os

def visibleBGR_to_img( img ):
    """Applies color channel conversions"""
    if len(img.shape) == 2: #visible ise siyah beyaz olmaz
        raise Exception("Unexpected data - 2channel data sent to visibleBGR_to_img (OH)")
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)     
    return img

folder_path = "/home/local/Desktop/k_Pnrm/1"
rows, cols = (4860, 6464)
for path in os.listdir(folder_path):    
    save_path = folder_path + "/" + path + ".png"
    with open(folder_path + "/" + path, 'rb') as f:
        raw_Bayer = np.fromfile(f, dtype=np.uint8,count=rows*cols).reshape((rows, cols))
    img = cv.cvtColor(raw_Bayer, cv.COLOR_BayerBG2BGR)    
    # cv.imshow("out", img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()
    cv.imwrite(save_path, img)
    # img = visibleBGR_to_img(img)