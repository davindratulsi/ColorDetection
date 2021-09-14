# import the necessary packages
import cv2
import numpy as np
frames = [str(num).zfill(5) for num in range(1,1001)]
trial = '000'
sequence = 'A4B4'

for frame in frames:
    image = cv2.imread('./examples/images/' + sequence + '/route_1/' + trial + '/test.' + frame + '.bmp', 1)
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # # apply binary thresholding
    ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
    # # visualize the binary image
    # cv2.imshow('Binary image', thresh)
    # cv2.waitKey(0)
    # cv2.imwrite('image_thres.jpg', thresh)
    # # detect the contours on the binary image
    contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE,
                                           method=cv2.CHAIN_APPROX_SIMPLE)
    # # draw contours on the original image
    image_copy = image.copy()
    # # draw contours that match a specified geometric criteria
    threshold_area = 100
    threshold_perimeter = 1200
    count = 0
    for i, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, closed=True)
        # if area > threshold_area:
        if perimeter > threshold_perimeter and perimeter < 3000:
            count += 1
            print('{} {}'.format(frame, perimeter))
            # cv2.drawContours(image=image_copy, contours=contour, contourIdx=-1,
            #                 color=(255, 0, 0), thickness=2, lineType=cv2.LINE_AA)
    # print(count)
    # see the results
    # cv2.imshow('Contours on image', image_copy)
    # cv2.waitKey(0)
    # cv2.imwrite('./contours/' + sequence + '/route_1/' + trial + '/contours_on_' + frame + '.jpg', image_copy)
    # cv2.destroyAllWindows()
