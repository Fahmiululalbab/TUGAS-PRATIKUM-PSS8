# flipping.py
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Flip horizontal
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

# Flip vertikal
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

# Flip horizontal + vertikal
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Both", flipped)
cv2.waitKey(0)
