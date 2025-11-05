# color_spaces.py
import argparse
import cv2

# --- membaca argumen gambar ---
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path ke gambar")
args = vars(ap.parse_args())

# --- membaca gambar dari path ---
image = cv2.imread(args["image"])
cv2.imshow("Original (BGR)", image)

# --- ubah ke grayscale ---
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)

# --- ubah ke HSV ---
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

# --- ubah ke LAB color space ---
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("L*a*b*", lab)

# --- ubah ke RGB (urutan berbeda dengan BGR) ---
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow("RGB", rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()
