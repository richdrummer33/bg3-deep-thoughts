import pytesseract
from PIL import ImageGrab

class ScreenReader:
    def __init__(self):
        self.pytesseract = pytesseract

    def read_screen(self):
        screenshot = ImageGrab.grab()
        text = self.pytesseract.image_to_string(screenshot)
        return text
