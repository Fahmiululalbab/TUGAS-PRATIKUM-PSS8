# masking.py
import numpy as np
import argparse
import cv2

# Membaca argumen gambar
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to the image")
args = vars(ap.parse_args())

# Membaca gambar dari disk
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Membuat mask kosong berukuran sama dengan gambar
mask = np.zeros(image.shape[:2], dtype="uint8")

# Gambar lingkaran putih di tengah mask
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)
cv2.circle(mask, (cX, cY), 100, 255, -1)

cv2.imshow("Mask", mask)

# Terapkan mask ke gambar
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Masked Image", masked)

cv2.waitKey(0)
cv2.destroyAllWindows()




