# gray_hist.py
import argparse
import cv2
import matplotlib.pyplot as plt

# --- membaca argumen gambar ---
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path ke gambar")
args = vars(ap.parse_args())

# --- membaca gambar dan ubah ke grayscale ---
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Grayscale", gray)

# --- hitung histogram grayscale ---
# cv2.calcHist(images, channels, mask, histSize, ranges)
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# --- tampilkan grafik histogram menggunakan matplotlib ---
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Intensitas Piksel (0 = gelap, 255 = terang)")
plt.ylabel("Jumlah Piksel")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
