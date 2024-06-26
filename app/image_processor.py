import pytesseract
from PIL import Image

def read_image(file_path: str) -> str:
    # Open the image file
    img = Image.open(file_path)
    
    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(img)
    
    return text
