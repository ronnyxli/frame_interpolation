
"""

Usage:
  create_frames.py <mov_dir> <interp_factor>

Options:
  -h, --help            Show this screen
  <mov_dir>             Folder containing live photo video files in .move format
  <interp_factor>       Interpolation factor (frame rate multiplier)

 Create python3 virtual environment: python3 -m venv env
 Activate virtual environment: source env/bin/activate
 Install requirements: pip install -r requirements.txt

"""

from docopt import docopt
import os
import glob

import numpy as np
import cv2

from matplotlib import pyplot as plt

import pdb


def get_video_params():
    pdb.set_trace()


def create_gif(fr, t_sec):
    '''
    Create gif from frame sequence (fr) with duration of t_sec seconds
    '''
    fps = len(fr)/t_sec
    pdb.set_trace()




def main(args):

    files = glob.glob(os.path.join(args['<mov_dir>'], '*MOV'))
    print('Found ' + str(len(files)) + ' .mov files')

    for fp in files:

        # get frames
        print('Loading frames for ' + fp + '...')
        frames = []
        vid_cap = cv2.VideoCapture(fp)
        while True:
            ret_val, img = vid_cap.read()
            if not ret_val:
                break
            frames.append(np.rot90(img,k=-1))

        plt.subplot(121)
        plt.imshow(frames[0])
        plt.subplot(122)
        plt.imshow(frames[-1])
        plt.show()
        pdb.set_trace()

        create_gif(frames, 1)

if __name__ == "__main__":
    main(docopt(__doc__))
