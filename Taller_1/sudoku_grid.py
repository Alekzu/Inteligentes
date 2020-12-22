import cv2
import numpy as np
import pytesseract


def get(img):
    #pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    grid = np.zeros((9, 9), dtype=int)

    stepy = round((658) / 9)
    stepx = round((658) / 9)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Applying Gaussian Blur to smooth out the noise
    gray = cv2.GaussianBlur(gray, (11, 11), 1)

    # Applying thresholding using adaptive Gaussian|Mean thresholding
    gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C | cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY, 5, 1)

    # Dilating the image to fill up the "cracks" in lines
    kernel = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], np.uint8)
    gray = cv2.dilate(gray, kernel)
    img = gray

    for i in range(0, 9):
        for j in range(0, 9):
            _x1 = (stepx * j)
            _x2 = stepx * (j + 1)
            _y1 = (stepy * i)
            _y2 = stepy * (i + 1)
            block = img[_y1 + 10:_y2 - 10, _x1 + 10:_x2 - 17]

            # Apply OCR on the cropped image
            text = pytesseract.image_to_string(
                block, config='--psm 6')

            try:
                grid[i, j] = int(text)
            except:
                pass

    return grid
