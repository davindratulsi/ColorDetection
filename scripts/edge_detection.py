# # Imports
import numpy as np
import cv2

# # Read file
image_file = './tests/shapes.png'
image = cv2.imread(image_file)
image = cv2.resize(image, (600, 600))
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Filter image, blur and dilate
image_gray = cv2.GaussianBlur(image_gray, (7, 7), 0)
kernel = np.ones((11,11), 'uint8')
image_gray = cv2.dilate(image_gray, kernel, iterations=1)

# # apply thresholding
threshold = 85
blocksize = 241 # has to be odd
# if pixel value is greater than threshold, it is assigned a value of 255
ret, thresh_basic = cv2.threshold(image_gray, thresh=threshold, maxval=255, type=cv2.THRESH_BINARY)
thresh_adapt = cv2.adaptiveThreshold(image_gray, maxValue=255,
                                     adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     thresholdType=cv2.THRESH_BINARY, blockSize=blocksize,
                                     C=1)

# # visualize the image
# cv2.imshow('Original image', image)
cv2.imshow('Gray image', image_gray)
# cv2.imshow('Simple binary threshold', thresh_basic)
cv2.imshow('Adaptive binary threshold', thresh_adapt)
cv2.waitKey(0)

# # detect the contours on the binary image
contours, hierarchy = cv2.findContours(image=thresh_adapt, mode=cv2.RETR_TREE,
                                        method=cv2.CHAIN_APPROX_SIMPLE)

# # draw contours on the original image
image_copy = image.copy()
cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1,
                color=(255, 0, 0), thickness=4, lineType=cv2.LINE_AA)

# # see the results
cv2.imshow('Contours on image', image_copy)
cv2.waitKey(0)
cv2.imwrite('./tests/image_contours.jpg', image_copy)
cv2.destroyAllWindows()
