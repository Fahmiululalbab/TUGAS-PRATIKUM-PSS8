# split_merge.py
import cv2
import numpy as np
import argparse

# --- membaca argumen gambar ---
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path ke gambar")
args = vars(ap.parse_args())

# --- membaca gambar dari path ---
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# --- memisahkan channel warna B, G, R ---
(B, G, R) = cv2.split(image)

cv2.imshow("Blue Channel (Gray)", B)
cv2.imshow("Green Channel (Gray)", G)
cv2.imshow("Red Channel (Gray)", R)

print("Ukuran masing-masing channel:")
print("Blue:", B.shape)
print("Green:", G.shape)
print("Red:", R.shape)

# --- gabungkan kembali jadi satu gambar ---
merged = cv2.merge([B, G, R])
cv2.imshow("Merged Image", merged)

# --- visualisasi channel berwarna (opsional) ---
zeroes = np.zeros(image.shape[:2], dtype="uint8")
cv2.imshow("Blue Channel (Color)", cv2.merge([B, zeroes, zeroes]))
cv2.imshow("Green Channel (Color)", cv2.merge([zeroes, G, zeroes]))
cv2.imshow("Red Channel (Color)", cv2.merge([zeroes, zeroes, R]))

cv2.waitKey(0)
cv2.destroyAllWindows()

