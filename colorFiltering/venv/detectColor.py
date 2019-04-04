from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="path to the image")
args = vars(ap.parse_args())

#image array for the testing pictures
images = ["1-6_ph.jpg", "1_ph.jpg", "2_ph.jpg", "3_ph.jpg", "4_ph.jpg", "6_ph.jpg"]

# low and high values for pink, yellow, dark grey, and light green
boundaries = [
	([97, 141, 150], [104, 149, 172]),
    ([150, 160, 155], [159, 177, 165]),
    ([171, 177, 160], [179, 189, 171]),
    ([130, 78, 145], [150,145,216])
]

# loop through all the images in the array
for image in images:
    # load the image
    img = cv2.imread(image)
    img = cv2.resize(img, (360, 480))

    # this part is still in progress, but it construct the histogram for the
    # rgb colors in the pictures
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("gray_img", gray)
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
    plt.figure()
    plt.title("Histogram")
    plt.xlabel("Bins")
    plt.ylabel("#Pixels")
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()
    cv2.waitKey(0)

    # loop through all the (low, high) values in the boundaries array
    for (low, high) in boundaries:

        low = np.array(low)
        high = np.array(high)

        mask = cv2.inRange(img, low, high)
        output = cv2.bitwise_and(img, img, mask=mask)

        cv2.imshow("images", np.hstack([img, output]))
        cv2.waitKey(0)
