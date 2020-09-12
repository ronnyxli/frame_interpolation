
import numpy as np
import cv2

import pdb





def main():

    fp = '/Users/ronnyli/Downloads/IMG_8635/IMG_8635.mov'

    pdb.set_trace()

    frames = []
    vid_cap = cv2.VideoCapture(fp)

    while True:
        ret_val, img = vid_cap.read()
        frames.append(img)

    pdb.set_trace()



if __name__ == '__main__':
    main()
