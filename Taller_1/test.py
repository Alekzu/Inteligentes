from cv2 import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
image = cv2.imread('maxresdefault.jpg')

text = pytesseract.image_to_string(image)
print('texto:', text)

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()