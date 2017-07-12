# Import the modules
import cv2
from skimage import io
import numpy as np
import json
import sys


def make_request_json(file_path, output_json):
    with open(output_json, 'w') as ff:
        # Read the input image
        im = io.imread(file_path)

        # crop the image as workaround for the bug where cv2.resize fails when height != width of image
        x = [im.shape[0], im.shape[1]]
        if x[0] != x[1]:
            y = min(x)
            im = im[0:y, 0:y]

        # Convert to grayscale and apply Gaussian filtering
        im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        im_gray = cv2.GaussianBlur(im_gray, (5, 5), 0)

        # Threshold the image
        ret, im_th = cv2.threshold(im_gray, 90, 255, cv2.THRESH_BINARY_INV)

        # Find contours in the image
        _ , ctrs, hier = cv2.findContours(im_th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Get rectangles contains each contour
        rects = [cv2.boundingRect(ctr) for ctr in ctrs]

        # For each rectangular region, calculate HOG features and predict
        # the digit using Linear SVM.
        for rect in rects:
            # Draw the rectangles
            cv2.rectangle(im, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 3)
            # Make the rectangular region around the digit
            leng = int(rect[3] * 1.6)
            pt1 = int(rect[1] + rect[3] // 2 - leng // 2)
            pt2 = int(rect[0] + rect[2] // 2 - leng // 2)
            roi = im_th[pt1:pt1+leng, pt2:pt2+leng]
            # Resize the image
            roi = cv2.resize(roi, (28, 28), interpolation=cv2.INTER_AREA)
            roi = cv2.dilate(roi, (3, 3))
            roi = roi/255.0
        row = json.dumps({"inputs":np.ndarray.flatten(roi).tolist()})
        ff.write(row)
