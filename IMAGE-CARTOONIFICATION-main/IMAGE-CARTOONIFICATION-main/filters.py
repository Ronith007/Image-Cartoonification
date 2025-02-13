

import cv2
import numpy as np

def caart(img, intensity=1):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 7)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 10)
    color = cv2.bilateralFilter(img, 9, 300, 300)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

def pencil_sketch(img, intensity=1):
    gray, sketch = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
    return sketch

def cel_shading(img, intensity=1):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Laplacian(gray, cv2.CV_8U, ksize=5)
    ret, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)
    quantized = cv2.bilateralFilter(img, 9, 75, 75)
    quantized = cv2.convertScaleAbs(quantized, alpha=(intensity + 1)/10)
    cel_shaded = cv2.bitwise_and(quantized, quantized, mask=mask)
    return cel_shaded

def sketch(img, intensity=1):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inv = cv2.bitwise_not(gray)
    blur = cv2.GaussianBlur(inv, (21, 21), 0)
    inv_blur = cv2.bitwise_not(blur)
    sketch = cv2.divide(gray, inv_blur, scale=256.0)
    return sketch

def halftone(img, intensity=1):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inv = cv2.bitwise_not(gray)
    circles = cv2.HoughCircles(inv, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=5, maxRadius=30)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            cv2.circle(img, (i[0], i[1]), i[2], (255, 255, 255), 3)
    return img

def toon(img, intensity=1):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(img, 9, 75, 75)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

def watercolor(img, intensity=1):
    img = cv2.edgePreservingFilter(img, flags=1, sigma_s=60, sigma_r=0.4)
    for i in range(2):
        img = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)
    return img

def comic_book(img, intensity=1):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    inverted_edges = cv2.bitwise_not(edges)
    return inverted_edges

def manga(img, intensity=1):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    ret, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)
    manga = cv2.bitwise_and(img, img, mask=mask)
    return manga

def caricature(img, intensity=1):
    rows, cols, _ = img.shape
    center_x, center_y = int(cols / 2), int(rows / 2)
    for i in range(rows):
        for j in range(cols):
            offset_x = int((i - center_y) * (i - center_y) / center_y)
            offset_y = int((j - center_x) * (j - center_x) / center_x)
            img[i, j] = img[min(rows - 1, i + offset_x), min(cols - 1, j + offset_y)]
    return img

def cartoon_3d(img, intensity=1):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    return cv2.addWeighted(img, 0.8, edges, 0.2, 0)

def flat_design(img, intensity=1):
    Z = img.reshape((-1, 3))
    Z = np.float32(Z)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 8
    _, labels, centers = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    res = centers[labels.flatten()]
    return res.reshape((img.shape))

def ink_wash(img, intensity=1):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
    return cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)

def pop_art(img, intensity=1):
    Z = img.reshape((-1, 3))
    Z = np.float32(Z)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 4
    _, labels, centers = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    res = centers[labels.flatten()]
    return res.reshape((img.shape))

def vector_art(img, intensity=1):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    return cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

def pixel_art(img, intensity=1):
    height, width = img.shape[:2]
    temp = cv2.resize(img, (width // 10, height // 10), interpolation=cv2.INTER_NEAREST)
    return cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

def silhouette(img, intensity=1):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, silhouette = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    return cv2.cvtColor(silhouette, cv2.COLOR_GRAY2BGR)

FILTER_MAP = {
    "Cartoon": caart,
    "Pencil Sketch": pencil_sketch,
    "Cel Shading": cel_shading,
    "Sketch": sketch,
    "Halftone": halftone,
    "Toon": toon,
    "Watercolor": watercolor,
    "Comic Book": comic_book,
    "Manga": manga,
    "Caricature": caricature,
    "3D Cartoon": cartoon_3d,
    "Flat Design": flat_design,
    "Ink Wash": ink_wash,
    "Pop Art": pop_art,
    "Vector Art": vector_art,
    "Pixel Art": pixel_art,
    "Silhouette": silhouette,
}
