# arithmetic.py
import cv2
import numpy as np
import argparse

# Baca argumen gambar
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path ke gambar pertama")
args = vars(ap.parse_args())

# Baca gambar utama
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Contoh: buat versi lebih terang dan lebih gelap
M = np.ones(image.shape, dtype="uint8") * 75  # nilai penambah kecerahan

# Tambahkan nilai untuk mencerahkan
added = cv2.add(image, M)
cv2.imshow("Lebih Terang", added)

# Kurangi nilai untuk menggelapkan
subtracted = cv2.subtract(image, M)
cv2.imshow("Lebih Gelap", subtracted)

cv2.waitKey(0)
cv2.destroyAllWindows()
