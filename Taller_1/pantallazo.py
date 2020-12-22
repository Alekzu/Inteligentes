
import numpy as np
import cv2
import pyautogui
from tablero import get
import pytesseract
#pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

def sudoku_matrix():
    board_location = pyautogui.locateOnScreen('selector2.png', confidence=0.6)
    imagen = pyautogui.screenshot(region=board_location)
    imagen = cv2.cvtColor(np.array(imagen),cv2.COLOR_RGB2BGR)

    tableroSudoku = get(imagen)
    return tableroSudoku
