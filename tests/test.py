# import the necessary packages
import cv2
import numpy as np

# # Read file
image_file = './tests/cat.png'
image = cv2.imread(image_file)
image = cv2.resize(image, (600, 600))
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # apply binary thresholding
ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)

# # visualize the image
cv2.imshow('Binary image', image)
cv2.waitKey(0)
# cv2.imwrite('image_thres.jpg', thresh)

# # detect the contours on the binary image
contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE,
                                        method=cv2.CHAIN_APPROX_SIMPLE)
# # draw contours on the original image
image_copy = image.copy()

# # # draw contours that match a specified geometric criteria
threshold_perimeter = 100
count = 0
for i, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, closed=True)
    # if area > threshold_area:
    if perimeter > threshold_perimeter:
        count += 1
        cv2.drawContours(image=image_copy, contours=contour, contourIdx=-1,
                        color=(255, 0, 0), thickness=2, lineType=cv2.LINE_AA)

# see the results
cv2.imshow('Contours on image', image_copy)
cv2.waitKey(0)
# cv2.imwrite('./tests/image_copy.jpg', image_copy)
# cv2.destroyAllWindows()
