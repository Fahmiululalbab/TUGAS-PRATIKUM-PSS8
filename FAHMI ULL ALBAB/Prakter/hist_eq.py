# hist_eq.py
import argparse
import cv2
import matplotlib.pyplot as plt

# --- membaca argumen gambar ---
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path ke gambar")
args = vars(ap.parse_args())

# --- membaca gambar dari path ---
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# --- ubah ke grayscale ---
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)

# --- equalize histogram (meningkatkan kontras) ---
equalized = cv2.equalizeHist(gray)
cv2.imshow("Histogram Equalized", equalized)

# --- hitung histogram sebelum dan sesudah ---
hist_gray = cv2.calcHist([gray], [0], None, [256], [0, 256])
hist_eq = cv2.calcHist([equalized], [0], None, [256], [0, 256])

# --- tampilkan grafik histogram dengan Matplotlib ---
plt.figure(figsize=(10,5))

plt.subplot(1, 2, 1)
plt.title("Before Equalization")
plt.xlabel("Intensitas Piksel")
plt.ylabel("Jumlah Piksel")
plt.plot(hist_gray)
plt.xlim([0, 256])

plt.subplot(1, 2, 2)
plt.title("After Equalization")
plt.xlabel("Intensitas Piksel")
plt.ylabel("Jumlah Piksel")
plt.plot(hist_eq)
plt.xlim([0, 256])

plt.tight_layout()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
