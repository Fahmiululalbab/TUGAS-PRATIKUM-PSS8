# getting_and_setting.py
from __future__ import print_function
import argparse
import cv2

# Membaca argumen path gambar
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to the image")
args = vars(ap.parse_args())

# Membaca gambar dari disk
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# --- Akses pixel tunggal ---
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# Ubah warna pixel di (0,0)
image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# --- Cropping menggunakan slicing ---
corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)

# --- Warnai bagian atas kiri menjadi hijau ---
image[0:100, 0:100] = (0, 255, 0)
cv2.imshow("Updated", image)
cv2.waitKey(0)

