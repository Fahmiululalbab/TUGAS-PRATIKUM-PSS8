# smoothing.py
import argparse
import cv2
import numpy as np

# --- membaca argumen gambar ---
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path ke gambar")
args = vars(ap.parse_args())

# --- membaca gambar dari path ---
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# -------- 1. AVERAGING BLUR --------
# Setiap piksel diganti dengan rata-rata piksel sekitar (kernel)
blurred_avg = cv2.blur(image, (11, 11))
cv2.imshow("Averaged (11x11)", blurred_avg)

# -------- 2. GAUSSIAN BLUR --------
# Bobot pixel ditentukan oleh distribusi Gaussian (lebih halus & realistis)
blurred_gaussian = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Gaussian (11x11)", blurred_gaussian)

# -------- 3. MEDIAN BLUR --------
# Mengambil median dari piksel di sekitar (efektif untuk menghilangkan noise garam-merica)
blurred_median = cv2.medianBlur(image, 11)
cv2.imshow("Median (11)", blurred_median)

# -------- 4. BILATERAL BLUR --------
# Menghaluskan gambar tapi tetap menjaga tepi tajam
blurred_bilateral = cv2.bilateralFilter(image, 11, 75, 75)
cv2.imshow("Bilateral (11, 75, 75)", blurred_bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()

