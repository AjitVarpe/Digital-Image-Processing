pip install opencv-python
import cv2 as cv
filename = # path to the image file
img = cv.imread(filename,0)
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))

# Top Hat Transform
topHat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
# Black Hat Transform
blackHat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)

res = img + topHat - blackHat