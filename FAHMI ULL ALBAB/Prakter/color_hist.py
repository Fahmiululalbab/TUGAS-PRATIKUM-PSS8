# color_hist.py
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

# --- menghitung histogram untuk setiap channel (B, G, R) ---
colors = ("b", "g", "r")

plt.figure()
plt.title("Color Histogram")
plt.xlabel("Intensitas Piksel (0–255)")
plt.ylabel("Jumlah Piksel")

for (channel, color) in enumerate(colors):
    hist = cv2.calcHist([image], [channel], None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
