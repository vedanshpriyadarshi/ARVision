# importing libraries
import cv2

class SimplePreprocessor:
    def __init__(self, width, height, inter=cv2.INTER_AREA):
        # store the target image width, height, and interpolation
        self.width = width
        self.height = height
        self.inter = inter

    def preprocess(self, image):
        # resize the image to fixed size ignoring aspect ratio
        return cv2.resize(image, (self.width, self.height), interpolation=self.inter)
