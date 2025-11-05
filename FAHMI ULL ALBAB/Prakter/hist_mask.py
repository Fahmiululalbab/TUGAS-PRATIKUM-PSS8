# hist_mask.py
import argparse
import cv2
import numpy as np
import matplotlib.pyplot as plt

# --- membaca argumen gambar ---
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path ke gambar")
args = vars(ap.parse_args())

# --- membaca gambar dari path ---
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# --- buat mask berbentuk lingkaran di tengah gambar ---
mask = np.zeros(image.shape[:2], dtype="uint8")
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)
cv2.circle(mask, (cX, cY), 100, 255, -1)

# --- tampilkan mask dan area hasil masking ---
cv2.imshow("Mask", mask)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Masked Image", masked)

# --- hitung histogram tanpa mask (seluruh gambar) ---
hist_full = cv2.calcHist([image], [0], None, [256], [0, 256])

# --- hitung histogram dengan mask ---
hist_mask = cv2.calcHist([image], [0], mask, [256], [0, 256])

# --- tampilkan kedua histogram ---
plt.figure(figsize=(10,5))
plt.subplot(1, 2, 1)
plt.title("Histogram Tanpa Mask (Full Image)")
plt.xlabel("Intensitas Piksel")
plt.ylabel("Jumlah Piksel")
plt.plot(hist_full)
plt.xlim([0, 256])

plt.subplot(1, 2, 2)
plt.title("Histogram Dengan Mask (Area Lingkaran)")
plt.xlabel("Intensitas Piksel")
plt.ylabel("Jumlah Piksel")
plt.plot(hist_mask)
plt.xlim([0, 256])

plt.tight_layout()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

